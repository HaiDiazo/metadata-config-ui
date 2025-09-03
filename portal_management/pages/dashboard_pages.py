import reflex as rx

from portal_management.state.dashboard_state import DashboardState
from portal_management.components.sidebar import sidebar_bottom_profile


def stat_card(title: str, value: str, color: str = "blue.500") -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(title, size="5", weight="bold", color="gray"),
            rx.text(value, size="2", weight="bold", color="gray"),
        ),
        bg="white",
        padding="1.5em",
        border_radius="1em",
        shadow="md",
        width="100%",
        text_align="center",
    )


def sidebar() -> rx.Component:
    return rx.vstack(
        rx.text("🏠 Dashboard", size="7", weight="bold"),
        rx.link("Standarization", href="/standarization", padding="0.5em 0"),
        rx.divider(margin="1em 0"),
        rx.link("Log out", href="/logout", padding="0.5em 0"),
        spacing="0.5em",
        padding="1em",
        bg="gray.100",
        width="220px",
        height="100vh",
    )


def timeseries_chart():
    return rx.recharts.line_chart(
        rx.recharts.line(
            data_key="value",
            stroke="#3182CE",
            stroke_width=2,
            dot=True,
        ),
        rx.recharts.x_axis(data_key="date"),
        rx.recharts.y_axis(),
        rx.recharts.tooltip(),
        rx.recharts.legend(),
        data=DashboardState.timeseries,
        width="100%",
        height=300,
    )


def dashboard_page() -> rx.Component:
    return rx.hstack(
        sidebar_bottom_profile(),
        rx.container(
            rx.box(
                rx.vstack(
                    rx.heading("Dashboard", size="7"),

                    rx.grid(
                        stat_card("Total Users", f"{DashboardState.total_users}"),
                        stat_card(
                            "Total Metadata",
                            f"{DashboardState.total_metadata:,.0f}",
                            color="green.500",
                        ),
                        columns="2",
                        spacing="2",
                        width="100%",
                    ),

                    # Chart
                    rx.box(
                        rx.heading("Data Statistic In Day", size="6", mb="1em", color="grey"),
                        timeseries_chart(),
                        bg="white",
                        padding="1.5em",
                        border_radius="1em",
                        shadow="md",
                        width="100%",
                    ),
                    spacing="4",
                    align_items="stretch",
                    width="100%",
                ),
                padding="2em",
                bg="gray.50",
                height="100vh",
                width="100%",
            ),
            padding="2em",
            bg="gray.50",
            width="100%",
            height="100vh",
        ),
        spacing="0",
        on_mount=DashboardState.load_data
    )

