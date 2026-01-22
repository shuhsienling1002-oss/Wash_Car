import streamlit as st

# ---------------------------------------------------------
# 1. 桃園在地店家資料庫 (模擬數據)
# 這裡收錄了桃園區、中壢、八德等地的美容店
# ---------------------------------------------------------
shops_data = [
    {
        "name": "桃園藝文 IPO 頂級汽車美容",
        "district": "桃園區",
        "location": "桃園區大興西路二段",
        "type": "高階鍍膜/深層護理",
        "price": "💰 2000 - 8000",
        "rating": 4.9,
        "is_amis_owned": False,
        "desc": "藝文特區名店，適合開雙B回鄉的族人，建議提前兩週預約。",
    },
    {
        "name": "中壢後站阿美洗車坊",
        "district": "中壢區",
        "location": "中壢區健行路",
        "type": "精緻洗車+打蠟",
        "price": "💰 400 - 1200",
        "rating": 4.8,
        "is_amis_owned": True,
        "desc": "老闆是我們三一協會的弟兄！族人去洗車多送水鍍膜，手路很乾淨。",
    },
    {
        "name": "八德介壽路自助洗車場",
        "district": "八德區",
        "location": "八德區介壽路一段",
        "type": "24H 自助洗車",
        "price": "💰 10 - 100",
        "rating": 4.3,
        "is_amis_owned": True,
        "desc": "場地超大，適合過年前大家約好一起去洗車聊天，老闆會放阿美族歌。",
    },
    {
        "name": "龜山林口 G'ZOX 鍍膜中心",
        "district": "龜山區",
        "location": "龜山區文化三路",
        "type": "日本頂級鍍膜",
        "price": "💰 3000+",
        "rating": 4.7,
        "is_amis_owned": False,
        "desc": "效果很持久，跑蘇花公路不怕髒，回來沖一沖就乾淨。",
    },
    {
        "name": "平鎮環南路快速美容",
        "district": "平鎮區",
        "location": "平鎮區環南路",
        "type": "快速洗車+內裝",
        "price": "💰 300 - 600",
        "rating": 4.1,
        "is_amis_owned": False,
        "desc": "速度快，適合趕著要回花蓮、沒時間等的族人。",
    },
]

# ---------------------------------------------------------
# 2. App 主程式 (Streamlit)
# ---------------------------------------------------------

# 設定頁面
st.set_page_config(
    page_title="三一協會：返鄉愛車護理",
    page_icon="✨",
    layout="centered"
)

# --- 頂部歡迎區 ---
st.title("三一協會：返鄉愛車護理 ✨")
st.markdown("""
<div style="background-color: #B71C1C; padding: 15px; border-radius: 10px; color: white; margin-bottom: 20px;">
    <h3 style='margin:0; color:white;'>Nga'ay ho! 準備回花東了嗎？</h3>
    <p style='margin-top:5px;'>過年返鄉前，在桃園先把車子洗得亮亮的，開回部落最有面子！</p>
</div>
""", unsafe_allow_html=True)

# --- 側邊欄或頂部篩選 ---
st.write("### 👇 您住在桃園哪裡？")

# 建立篩選按鈕
area_filter = st.radio(
    "選擇區域",
    ["全部顯示", "桃園區", "中壢區", "八德/平鎮", "龜山/其他"],
    horizontal=True,
    label_visibility="collapsed"
)

st.divider()

# --- 資料篩選邏輯 ---
filtered_shops = []
for shop in shops_data:
    if area_filter == "全部顯示":
        filtered_shops.append(shop)
    elif area_filter == "桃園區" and shop["district"] == "桃園區":
        filtered_shops.append(shop)
    elif area_filter == "中壢區" and shop["district"] == "中壢區":
        filtered_shops.append(shop)
    elif area_filter == "八德/平鎮" and shop["district"] in ["八德區", "平鎮區"]:
        filtered_shops.append(shop)
    elif area_filter == "龜山/其他" and shop["district"] not in ["桃園區", "中壢區", "八德區", "平鎮區"]:
        filtered_shops.append(shop)

# --- 顯示結果 ---
st.info(f"🔍 在 {area_filter} 幫您找到 {len(filtered_shops)} 間推薦店家")

for shop in filtered_shops:
    with st.container(border=True):
        col1, col2 = st.columns([7, 3])
        
        with col1:
            st.subheader(shop["name"])
            
            # 族人經營標籤
            if shop["is_amis_owned"]:
                st.markdown(":red[**🔴 三一協會族人經營 (支持自己人!)**]")
            
            st.text(f"📍 {shop['location']} ({shop['district']})")
            st.markdown(f"🛠️ **{shop['type']}**")
            st.markdown(f"💵 **{shop['price']}**")
            st.caption(f"💡 {shop['desc']}")
            
        with col2:
            st.markdown(f"## ⭐ {shop['rating']}")
            # 導航按鈕
            map_url = f"https://www.google.com/maps/search/?api=1&query={shop['name']}+桃園"
            st.link_button("🚗 導航去", map_url, use_container_width=True)

# --- 底部提示 ---
st.divider()
st.markdown(
    """
    <div style='text-align: center; color: grey; font-size: 13px;'>
        ⚠️ <strong>過年提醒：</strong> 春節前一週通常會漲價或排隊，建議提早預約！<br>
        桃園三一協會 Taoyuan Sanyi Association © 2026
    </div>
    """,
    unsafe_allow_html=True
)
