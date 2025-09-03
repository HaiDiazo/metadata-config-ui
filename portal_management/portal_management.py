import reflex as rx

from portal_management.pages.dashboard_pages import dashboard_page
from portal_management.pages.standarization_pages import standarization_page
from portal_management.state.login_state import LoginState


def login_default() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.center(
                rx.heading(
                    "Sign in to your account",
                    size="6",
                    as_="h2",
                    text_align="center",
                    width="100%",
                ),
                direction="column",
                spacing="5",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "Username",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    placeholder="username",
                    type="email",
                    value=LoginState.username,
                    on_change=LoginState.set_username,
                    size="3",
                    width="100%",
                ),
                justify="start",
                spacing="2",
                width="100%",
            ),
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "Password",
                        size="3",
                        weight="medium",
                    ),
                    rx.link(
                        "Forgot password?",
                        href="#",
                        size="3",
                    ),
                    justify="between",
                    width="100%",
                ),
                rx.input(
                    placeholder="Enter your password",
                    type="password",
                    value=LoginState.password,
                    on_change=LoginState.set_password,
                    size="3",
                    width="100%",
                ),
                spacing="2",
                width="100%",
            ),
            rx.button("Sign in", size="3", width="100%", on_click=LoginState.do_login),
            rx.cond(
                LoginState.error_message != "",
                rx.text(LoginState.error_message, color="red", size="4"),
            ),
            spacing="6",
            width="100%",
        ),
        size="4",
        max_width="28em",
        width="100%",
    )


def index() -> rx.Component:

    login_container = login_default()
    _main = rx.container(
        rx.center(
            rx.box(
                login_container
            ),
            height="100vh",
            width="100%",
        )
    )
    return _main


app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True
    )
)
app.add_page(index, route="/")
app.add_page(dashboard_page, route="/dashboard")
app.add_page(standarization_page, route="/standarization")
