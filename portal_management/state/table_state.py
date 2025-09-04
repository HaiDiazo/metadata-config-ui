import reflex as rx


class TableState(rx.State):
    rows: list[dict] = [
        {"id": 1, "name": "Alice", "email": "alice@mail.com"},
        {"id": 2, "name": "Bob", "email": "bob@mail.com"},
    ]

    editing_row: dict | None = None
    show_modal: bool = False
    edit_name: str = ""
    edit_email: str = ""
    modal_open: bool = False

    def open_edit(self, row: dict):
        self.editing_row = row
        self.edit_name = row["name"]
        self.edit_email = row["email"]
        self.show_modal = True

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
