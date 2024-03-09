import flet as ft


class CalculatorApp(ft.UserControl):
    result = ft.Text(value="0",
                     text_align=ft.TextAlign.END,
                     color=ft.colors.WHITE,
                     expand=True)
    operation = ft.Text(value="",
                        text_align=ft.TextAlign.END,
                        color=ft.colors.GREY_50,
                        expand=True)

    def build(self):
        return ft.Container(
            width=300,
            bgcolor=ft.colors.BLACK,
            border_radius=ft.border_radius.all(20),
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Row(controls=[self.operation], alignment=ft.MainAxisAlignment.END),
                    ft.Row(controls=[self.result], alignment=ft.MainAxisAlignment.END),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="AC",
                                bgcolor=ft.colors.BLUE_GREY_100,
                                color=ft.colors.BLACK,
                                expand=2,
                            ),
                            ft.ElevatedButton(
                                text="+/-",
                                bgcolor=ft.colors.ORANGE,
                                color=ft.colors.WHITE,
                                expand=2,
                            ),
                            ]),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="C",
                                bgcolor=ft.colors.BLUE_GREY_100,
                                color=ft.colors.BLACK,
                                expand=1,
                            ),
                            ft.ElevatedButton(
                                text="√",
                                bgcolor=ft.colors.ORANGE,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                            ft.ElevatedButton(
                                text="%",
                                bgcolor=ft.colors.ORANGE,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                            ft.ElevatedButton(
                                text="/",
                                bgcolor=ft.colors.ORANGE,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="7",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                            ft.ElevatedButton(
                                text="8",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                            ft.ElevatedButton(
                                text="9",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                            ft.ElevatedButton(
                                text="*",
                                bgcolor=ft.colors.ORANGE,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="4",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                            ft.ElevatedButton(
                                text="5",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                            ft.ElevatedButton(
                                text="6",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                            ft.ElevatedButton(
                                text="-",
                                bgcolor=ft.colors.ORANGE,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="1",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                            ft.ElevatedButton(
                                text="2",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                            ft.ElevatedButton(
                                text="3",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                            ft.ElevatedButton(
                                text="+",
                                bgcolor=ft.colors.ORANGE,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="0",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=2,
                            ),
                            ft.ElevatedButton(
                                text=".",
                                bgcolor=ft.colors.WHITE24,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                            ft.ElevatedButton(
                                text="=",
                                bgcolor=ft.colors.ORANGE,
                                color=ft.colors.WHITE,
                                expand=1,
                            ),
                        ]
                    ),
                ]
            )
        )


def main(page: ft.Page):
    page.title = "Calc App"
    # create application instance
    calc = CalculatorApp()

    # add application's root control to the page
    page.add(calc)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ft.app(target=main)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
