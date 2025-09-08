import httpx
import reflex as rx

from loguru import logger


class TableState(rx.State):
    rows: list[dict] = []
    types: list[str] = []

    editing_row: dict | None = None
    add_row: dict | None = None

    show_modal_add: bool = False
    modal_add_open: bool = False
    show_modal: bool = False
    modal_open: bool = False

    error_message: str = ""
    auth_token: str = rx.Cookie(name="auth_token", max_age=3600)

    select_type: str = ""

    edit_type: str = ""
    edit_standarization: str = ""
    edit_query: str = ""

    async def hit_api(self, uri: str, method: str, params: dict = None):
        async with httpx.AsyncClient(timeout=5) as client:
            headers = {
                'Authorization': f"Bearer {self.auth_token}"
            }
            logger.info(params)
            resp = await client.request(
                method,
                uri,
                headers=headers,
                params=params
            )

        if resp.status_code == 200:
            data = resp.json()['data']
            logger.info("Total data get: {}", len(data))
            return data
        else:
            logger.info(resp.text)
            self.error_message = "Error Get Data"
            return []

    async def load_data(self):
        data_standarization = await self.hit_api(
            method="GET",
            uri="http://192.168.24.237:8679/metadata/get-standarization",
            params={
                "type": "level"
            }
        )
        self.rows = data_standarization

        types = await self.hit_api(
            method="GET",
            uri="http://192.168.24.237:8679/metadata/get-type-standarization"
        )

        self.types = [
            data_type['key']
            for data_type in types
        ]

    async def change_table_data(self):
        if self.select_type != "":
            data_standarization = await self.hit_api(
                method="GET",
                uri="http://192.168.24.237:8679/metadata/get-standarization",
                params={
                    "type": self.select_type
                }
            )
            self.rows = data_standarization

    def open_edit(self, row: dict):
        self.editing_row = row
        self.edit_type = row["type"]
        self.edit_standarization = row["standarization"]
        self.edit_query = row["query"]
        self.show_modal = True

    def open_modal_add(self):
        self.show_modal_add = True

    def close_modal_add(self):
        self.show_modal_add = False
        self.add_row = None

    def close_modal(self):
        self.show_modal = False
        self.editing_row = None

    def set_modal_open(self, v: bool):
        self.modal_open = v
        if not v:
            self.close_modal()

    def save_edit(self):
        if self.editing_row:
            for r in self.rows:
                if r["id"] == self.editing_row["id"]:
                    r["name"] = self.edit_name
                    r["email"] = self.edit_email
                    break
        self.close_modal()
