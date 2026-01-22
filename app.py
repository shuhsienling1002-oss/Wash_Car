import streamlit as st

# ---------------------------------------------------------
# 1. 模擬數據庫 (店家資料)
# 您可以在這裡直接新增或修改店家資訊
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
    {
        "name": "光復糖廠旁快速洗車",
        "location": "花蓮縣光復鄉",
        "type": "機器洗車+人工擦拭",
        "price": "💰 150 - 300",
        "rating": 4.0,
        "is_amis_owned": False,
        "desc": "就在台9線旁邊，休息吃冰順便洗車。",
    },
]

# ---------------------------------------------------------
# 2. App 頁面設定與主程式
# ---------------------------------------------------------

# 設定網頁標題、圖示與版面
st.set_page_config(
    page_title="三一協會讓你車美美",
    page_icon="🚗",
    layout="centered"
)

# --- 頂部標題區 ---
st.title("三一協會讓你車美美 🚗")
st.markdown("""
<div style="background-color: #d32f2f; padding: 10px; border-radius: 5px; color: white; margin-bottom: 20px;">
    <strong>Nga'ay ho! 歡迎回家</strong><br>
    這是專屬三一協會族人的返鄉愛車特搜網
</div>
""", unsafe_allow_html=True)

# --- 篩選控制區 ---
st.write("### 👇 請問您要回哪裡？")
col_filter, col_empty = st.columns([2, 1])
with col_filter:
    filter_option = st.radio(
        "區域篩選",
        ["全部顯示", "花蓮區", "台東區"],
        horizontal=True,
        label_visibility="collapsed"
    )

st.divider()

# --- 資料篩選邏輯 ---
filtered_shops = []
for shop in shops_data:
    if filter_option == "全部顯示":
        filtered_shops.append(shop)
    elif filter_option == "花蓮區" and "花蓮" in shop["location"]:
        filtered_shops.append(shop)
    elif filter_option == "台東區" and "台東" in shop["location"]:
        filtered_shops.append(shop)

# --- 顯示店家列表 ---
st.caption(f"目前顯示 {len(filtered_shops)} 間店家")

for shop in filtered_shops:
    # 建立一個卡片容器
    with st.container(border=True):
        # 將卡片分為左(資訊)、右(評分與按鈕)兩欄
        col1, col2 = st.columns([7, 3])
        
        with col1:
            # 店名
            st.subheader(shop["name"])
            
            # 族人經營標籤 (如果是族人開的，顯示紅色標籤)
            if shop["is_amis_owned"]:
                st.markdown(":red[**🔴 三一協會族人經營**]")
            
            # 詳細資訊
            st.text(f"📍 地點：{shop['location']}")
            st.text(f"🛠️ 服務：{shop['type']}")
            st.markdown(f"💵 **價格：{shop['price']}**")
            st.caption(f"💬 特色：{shop['desc']}")
            
        with col2:
            # 顯示評分
            st.markdown(f"### ⭐ {shop['rating']}")
            
            # 導航按鈕 (生成 Google Maps 連結)
            map_url = f"https://www.google.com/maps/search/?api=1&query={shop['name']}+{shop['location']}"
            st.link_button("🚗 導航去", map_url, use_container_width=True)

# --- 底部版權區 ---
st.divider()
st.markdown(
    """
    <div style='text-align: center; color: grey; font-size: 12px;'>
        桃園三一協會 Taoyuan Sanyi Association © 2026<br>
        Designed for Pangcah Return
    </div>
    """,
    unsafe_allow_html=True
)
