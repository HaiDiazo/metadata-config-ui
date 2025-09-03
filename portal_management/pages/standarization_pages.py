import reflex as rx

from portal_management.components.sidebar import sidebar_bottom_profile
from portal_management.state.table_state import TableState


def edit_modal():
    return rx.dialog.root(
        rx.dialog.trigger(rx.box()),
        rx.dialog.content(
            rx.dialog.title("Edit Row"),
            rx.dialog.description("Update user info"),
            rx.vstack(
                rx.input(
                    value=TableState.edit_name,
                    placeholder="Name",
                    on_change=TableState.set_edit_name,
                ),
                rx.input(
                    value=TableState.edit_email,
                    placeholder="Email",
                    on_change=TableState.set_edit_email,
                ),
                rx.hstack(
                    rx.button("Cancel", on_click=TableState.close_modal),
                    rx.button("Save", on_click=TableState.save_edit, color_scheme="green"),
                    spacing="3",
                ),
                spacing="4",
            ),
        ),
        open=TableState.show_modal,
        on_open_change=TableState.set_modal_open
    )


def table_with_edit():
    return rx.box(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("ID"),
                    rx.table.column_header_cell("Name"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Action"),
                )
            ),
            rx.table.body(
                rx.foreach(
                    TableState.rows,
                    lambda row: rx.table.row(
                        rx.table.cell(row["id"]),
                        rx.table.cell(row["name"]),
                        rx.table.cell(row["email"]),
                        rx.table.cell(
                            rx.button(
                                "Edit",
                                size="2",
                                on_click=TableState.open_edit(row),
                            )
                        ),
                    ),
                )
            ),
        ),
        edit_modal(),
    )


def standarization_page() -> rx.Component:
    return rx.hstack(
        sidebar_bottom_profile(),
        rx.container(
            rx.vstack(
                rx.heading("Standarization", size="7"),
                table_with_edit(),
                padding="2em",
                bg="gray.50",
                height="100vh",
                width="100%",
            ),
            padding="2em",
            bg="gray.50",
            width="100%",
            height="100vh",
        )
    )
