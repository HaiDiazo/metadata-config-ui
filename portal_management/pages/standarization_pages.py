import reflex as rx

from portal_management.components.sidebar import sidebar_bottom_profile
from portal_management.state.table_state import TableState
from portal_management.components.modal_standarization import (
    edit_modal,
    add_modal
)


def table_with_edit():
    return rx.box(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("ID"),
                    rx.table.column_header_cell("Type"),
                    rx.table.column_header_cell("Standarization"),
                    rx.table.column_header_cell("Query"),
                    rx.table.column_header_cell("Action"),
                )
            ),
            rx.table.body(
                rx.foreach(
                    TableState.rows,
                    lambda row: rx.table.row(
                        rx.table.cell(row["id"]),
                        rx.table.cell(row["type"]),
                        rx.table.cell(row["standarization"]),
                        rx.table.cell(row["query"]),
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
        bg="white",
        spacing="2",
        padding="1.5em",
        border_radius="1em",
        shadow="lg",
    )


def standarization_page() -> rx.Component:
    return rx.hstack(
        rx.box(
            sidebar_bottom_profile(),
            width="250px",
            height="100vh",
            bg="white",
            shadow="md",
        ),
        rx.box(
            rx.vstack(
                rx.heading("Standarization", size="7"),
                rx.hstack(
                    rx.select(
                        items=TableState.types,
                        placeholder="level",
                        on_change=[TableState.set_select_type, TableState.change_table_data],
                        color_scheme="blue",
                        width="20%"
                    ),
                    rx.button(
                        "Add Standarization",
                        size="2",
                        color_scheme="green",
                        width="10%",
                        on_click=TableState.open_modal_add
                    ),
                    add_modal()
                ),
                table_with_edit(),
                flex="1",
                min_width="0",
                overflow="auto",
                spacing="6",
                align_items="stretch",
                width="100%",
            ),
            padding="2em",
            flex="1",
        ),
        spacing="0",
        bg="#F3F4F6",
        on_mount=TableState.load_data

    )
