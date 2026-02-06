import flet as ft


def main(page: ft.Page):
    page.title = "Tasker"
    page.add(
        ft.SafeArea(
            ft.Column(
                [
                    ft.Text("Tasker App"),
                ]
            )
        )
    )


ft.run(main)
