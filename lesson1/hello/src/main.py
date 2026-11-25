import flet as ft


def main(page: ft.Page):
    # hello World
    hello_world = ft.Text("Hello World", size=50)

    # カウンター表示用のオブジェクト
    counter = ft.Text("0", size=50, data=0)

    # +ボタンがクリックされた時に呼ばれる関数
    def increment_click(e: ft.Event[ft.IconButton]):
        counter.data += 1
        counter.value = str(counter.data)
        page.update()

    def decrement_click(e):
        counter.data -= 1
        counter.value = str(counter.data)
        page.update()

    buttons = ft.Row(
        controls=[
            ft.IconButton(
                icon=ft.Icons.REMOVE,
                key="decrement",
                on_click=decrement_click,
            ),
            ft.IconButton(
                icon=ft.Icons.ADD,
                key="increment",
                on_click=increment_click,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # コンテンツを描画エリアに追加
    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Row(
                            controls=[hello_world, counter],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        buttons,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                alignment=ft.Alignment.CENTER,
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main)
