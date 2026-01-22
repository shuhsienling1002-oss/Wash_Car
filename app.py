import flet as ft

# ---------------------------------------------------------
# 1. 模擬數據庫 (Mock Data)
# ---------------------------------------------------------
shops_data = [
    {
        "name": "吉安阿美精緻洗車",
        "location": "花蓮縣吉安鄉",
        "type": "洗車+打蠟",
        "price": "💰 300 - 800",
        "rating": 4.8,
        "is_amis_owned": True,
        "desc": "老闆是吉安部落的，回鄉族人打9折！手路很細。",
    },
    {
        "name": "台東馬蘭光澤美容",
        "location": "台東市更生路",
        "type": "深層美容/鍍膜",
        "price": "💰 1500 - 4000",
        "rating": 4.5,
        "is_amis_owned": False,
        "desc": "設備很新，有休息室可以喝咖啡。",
    },
    {
        "name": "玉里部落自助洗車",
        "location": "花蓮縣玉里鎮",
        "type": "自助洗車",
        "price": "💰 50 - 100",
        "rating": 4.2,
        "is_amis_owned": True,
        "desc": "場地大，適合過年返鄉大家一起來洗。",
    },
    {
        "name": "成功海岸線車體護理",
        "location": "台東縣成功鎮",
        "type": "洗車+內裝",
        "price": "💰 500 - 1200",
        "rating": 4.9,
        "is_amis_owned": True,
        "desc": "靠近海邊，洗完車可以看海，老闆很熱情。",
    },
]

# ---------------------------------------------------------
# 2. App 主程式邏輯
# ---------------------------------------------------------
def main(page: ft.Page):
    # --- 修改點 1: 視窗標題 ---
    page.title = "三一協會讓你車美美"
    
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.window_width = 400
    page.window_height = 800
    
    # 配色方案 (熱情紅 + 純淨白)
    primary_color = ft.colors.RED_700
    
    # --- UI 元件生成函數 ---
    def create_shop_card(shop):
        badges = []
        if shop["is_amis_owned"]:
            badges.append(
                ft.Container(
                    content=ft.Text("族人經營", size=10, color=ft.colors.WHITE),
                    bgcolor=ft.colors.RED_500,
                    padding=5,
                    border_radius=5,
                )
            )
        
        return ft.Card(
            elevation=5,
            content=ft.Container(
                padding=15,
                content=ft.Column([
                    ft.Row([
                        ft.Text(shop["name"], size=18, weight=ft.FontWeight.BOLD),
                        ft.Icon(ft.icons.STAR, color=ft.colors.AMBER, size=16),
                        ft.Text(str(shop["rating"]), size=14, weight=ft.FontWeight.BOLD),
                    ]),
                    ft.Row(badges),
                    ft.Divider(),
                    ft.Row([
                        ft.Icon(ft.icons.LOCATION_ON, size=14, color=ft.colors.GREY),
                        ft.Text(shop["location"], size=12, color=ft.colors.GREY_700),
                    ]),
                    ft.Row([
                        ft.Icon(ft.icons.WATER_DROP, size=14, color=ft.colors.BLUE),
                        ft.Text(shop["type"], size=12),
                    ]),
                    ft.Row([
                        ft.Icon(ft.icons.CURRENCY_EXCHANGE, size=14, color=ft.colors.GREEN),
                        ft.Text(shop["price"], size=12, weight=ft.FontWeight.BOLD),
                    ]),
                    ft.Container(height=5),
                    ft.Text(shop["desc"], size=12, italic=True, color=ft.colors.GREY_600),
                    ft.Container(height=10),
                    ft.ElevatedButton(
                        "預約 / 導航",
                        icon=ft.icons.MAP,
                        style=ft.ButtonStyle(color=ft.colors.WHITE, bgcolor=primary_color),
                        on_click=lambda _: print(f"Navigating to {shop['name']}")
                    )
                ])
            )
        )

    # --- 頁面佈局 ---

    # --- 修改點 2: APP 內部大標題 ---
    header = ft.Container(
        content=ft.Column([
            ft.Text("三一協會讓你車美美", size=24, weight=ft.FontWeight.BOLD, color=primary_color),
            ft.Text("Nga'ay ho! 返鄉愛車特搜網", size=14, color=ft.colors.GREY),
        ]),
        padding=ft.padding.only(bottom=20)
    )

    # 篩選按鈕區
    def filter_shops(e):
        filter_type = e.control.data
        shop_list_view.controls.clear()
        for shop in shops_data:
            if filter_type == "ALL":
                shop_list_view.controls.append(create_shop_card(shop))
            elif filter_type == "Hualien" and "花蓮" in shop["location"]:
                shop_list_view.controls.append(create_shop_card(shop))
            elif filter_type == "Taitung" and "台東" in shop["location"]:
                shop_list_view.controls.append(create_shop_card(shop))
        page.update()

    filter_row = ft.Row([
        ft.ElevatedButton("全部", data="ALL", on_click=filter_shops),
        ft.ElevatedButton("花蓮區", data="Hualien", on_click=filter_shops),
        ft.ElevatedButton("台東區", data="Taitung", on_click=filter_shops),
    ], alignment=ft.MainAxisAlignment.CENTER)

    shop_list_view = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)

    for shop in shops_data:
        shop_list_view.controls.append(create_shop_card(shop))

    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME, label="首頁"),
            ft.NavigationDestination(icon=ft.icons.FAVORITE, label="收藏"),
            ft.NavigationDestination(icon=ft.icons.PERSON, label="協會專區"),
        ]
    )

    page.add(header, filter_row, ft.Divider(), shop_list_view, nav_bar)

ft.app(target=main)
