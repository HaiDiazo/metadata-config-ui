import reflex as rx

from portal_management.state.table_state import TableState


def edit_modal():
    return rx.dialog.root(
        rx.dialog.trigger(rx.box()),
        rx.dialog.content(
            rx.dialog.title(f"Edit Standarization '{TableState.edit_standarization}'"),
            rx.vstack(
                rx.hstack(
                    rx.text("Standarization:", size="2", text_align="left", width="120px"),
                    rx.input(
                        value=TableState.edit_standarization,
                        placeholder="Standarization",
                        on_change=TableState.set_edit_standarization,
                        width="100%",
                    ),
                    spacing="2",
                    align_items="center",
                    width="100%",
                ),
                rx.hstack(
                    rx.text("Type:", size="2", text_align="left", width="120px"),
                    rx.input(
                        value=TableState.edit_type,
                        placeholder="Type",
                        on_change=TableState.set_edit_type,
                        width="100%",
                    ),
                    spacing="2",
                    align_items="center",
                    width="100%",
                ),
                rx.hstack(
                    rx.text("Query:", size="2", text_align="left", width="120px"),
                    rx.text_area(
                        value=TableState.edit_query,
                        placeholder="Query",
                        on_change=TableState.set_edit_query,
                        width="100%",
                    ),
                    spacing="2",
                    align_items="center",
                    width="100%",
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


def add_modal():
    return rx.dialog.root(
        rx.dialog.trigger(rx.box()),
        rx.dialog.content(
            rx.dialog.title(f"Add New Standarization"),
            rx.vstack(
                rx.hstack(
                    rx.text("Standarization:", size="2", text_align="left", width="120px"),
                    rx.input(
                        value=TableState.add_standarization,
                        placeholder="Standarization",
                        on_change=TableState.set_add_standarization,
                        width="100%",
                    ),
                    spacing="2",
                    align_items="center",
                    width="100%",
                ),
                rx.hstack(
                    rx.text("Type:", size="2", text_align="left", width="120px"),
                    rx.input(
                        value=TableState.select_type,
                        placeholder="Type",
                        on_change=TableState.set_add_types,
                        width="100%",
                    ),
                    spacing="2",
                    align_items="center",
                    width="100%",
                ),
                rx.hstack(
                    rx.text("Query:", size="2", text_align="left", width="120px"),
                    rx.text_area(
                        value=TableState.add_query,
                        placeholder="Query",
                        on_change=TableState.set_add_query,
                        width="100%",
                    ),
                    spacing="2",
                    align_items="center",
                    width="100%",
                ),
                rx.hstack(
                    rx.button("Cancel", on_click=TableState.close_modal_add),
                    rx.button("Save", on_click=TableState.save_add, color_scheme="green"),
                    spacing="3",
                ),
                spacing="4",
            ),
        ),
        open=TableState.show_modal_add,
        on_open_change=TableState.set_modal_add_open
    )
