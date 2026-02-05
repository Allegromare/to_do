import flet as ft


def main(page: ft.Page):
    counter = ft.Text("0", size=50, data=0)

    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)

    def decrement_click(e):
        counter.data -= 1
        counter.value = str(counter.data)    


    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Container(
                content=ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.Icons.REMOVE, on_click=decrement_click, icon_size=40),
                        counter,
                        ft१९.IconButton(icon=ft.Icons.ADD, on_click=increment_click, icon_size=40),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=30,
                ),
                alignment=ft.Alignment.CENTER,
            ),
        )
    )


ft.run(main)
