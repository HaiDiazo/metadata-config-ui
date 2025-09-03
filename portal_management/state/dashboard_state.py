import httpx
import reflex as rx

from datetime import datetime, timedelta


class DashboardState(rx.State):
    total_users: int = 0
    total_metadata: int = 0
    timeseries: list = []
    active_users: int = 321
    revenue: float = 45230.75
    new_signups: int = 56
    auth_token: str = rx.Cookie(name="auth_token", max_age=3600)
    error_message: str = ""

    async def hit_api(self, uri: str, method: str, params: dict = None):
        async with httpx.AsyncClient(timeout=5) as client:
            headers = {
                'Authorization': f"Bearer {self.auth_token}"
            }
            print(params)
            resp = await client.request(
                method,
                uri,
                headers=headers,
                params=params
            )
            print(resp.text)

        if resp.status_code == 200:
            data = resp.json()['data']
            return data
        else:
            self.error_message = "Error Get Data"
            return []

    async def load_data(self):
        data_account = await self.hit_api(method="GET", uri="http://192.168.24.237:8679/account/get-all")
        self.total_users = len(data_account)

        total_metadata = await self.hit_api(method="GET", uri="http://192.168.24.237:8679/metadata/count")
        self.total_metadata = total_metadata['totalData']

        start_date = (datetime.now() - timedelta(days=14)).strftime("%Y-%m-%d %H:%M:%S")
        end_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        data_timeseries = await self.hit_api(
            method="GET",
            uri="http://192.168.24.237:8679/metadata/timeseries-by-source",
            params={
                "startDate": start_date,
                "endDate": end_date
            }
        )
        self.timeseries = data_timeseries

    async def before_render(self):
        if not self.auth_token:
            return rx.redirect("/")
