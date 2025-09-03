import httpx
import reflex as rx


class LoginState(rx.State):
    username: str = ""
    password: str = ""
    error_message: str = ""
    auth_token: str = rx.Cookie(name="auth_token", max_age=3600)

    async def do_login(self):
        try:
            async with httpx.AsyncClient(timeout=5) as client:
                resp = await client.post(
                    "http://192.168.24.237:8679/auth/login",
                    params={"username": self.username, "password": self.password},
                )

            if resp.status_code == 200:
                data = resp.json()
                token = data.get("token")
                if token:
                    self.auth_token = token

                    self.error_message = ""
                    yield rx.redirect("/dashboard")
                else:
                    self.error_message = "Login failed: username or password is incorrect."
            else:
                self.error_message = "Invalid username or password."
        except Exception as e:
            self.error_message = f"Error: {str(e)}"
