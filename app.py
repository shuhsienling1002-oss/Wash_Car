import streamlit as st

# ---------------------------------------------------------
# 1. 全桃園 13 行政區完整資料庫
# ---------------------------------------------------------
shops_data = [
    # --- 新屋區 (Xinwu) ---
    {
        "name": "台灣中油 (新屋站)",
        "district": "新屋區",
        "location": "新屋區中山路",
        "type": "機器洗車",
        "price": "💰 150 - 200",
        "rating": 4.0,
        "desc": "新屋最穩定的選擇，過年前不想跑遠，來這裡嚕一下最快。",
    },
    {
        "name": "新屋自助洗車 (近交流道)",
        "district": "新屋區",
        "location": "新屋區文化路",
        "type": "自助洗車",
        "price": "💰 投幣式",
        "rating": 3.8,
        "desc": "場地簡單但夠用，適合只想沖沖灰塵的族人。",
    },

    # --- 楊梅區 (Yangmei) - 新屋鄰居 ---
    {
        "name": "車酷頂級美車工藝 (楊梅店)",
        "district": "楊梅區",
        "location": "楊梅區中山北路",
        "type": "精緻美容",
        "price": "💰 1200+",
        "rating": 4.8,
        "desc": "就在省道旁，新屋跑過來很快，技術非常好。",
    },
    {
        "name": "埔心牧場旁自助洗",
        "district": "楊梅區",
        "location": "楊梅區幼獅路",
        "type": "自助洗車",
        "price": "💰 投幣式",
        "rating": 4.3,
        "desc": "空間非常大，很多車友會來這裡聚會。",
    },

    # --- 觀音區 (Guanyin) ---
    {
        "name": "草漯極光洗車",
        "district": "觀音區",
        "location": "觀音區大觀路",
        "type": "人工手洗",
        "price": "💰 300 - 600",
        "rating": 4.2,
        "desc": "草漯重劃區這邊評價不錯的店，工業區下班來洗剛好。",
    },

    # --- 龍潭區 (Longtan) ---
    {
        "name": "龍潭北龍路專業美容",
        "district": "龍潭區",
        "location": "龍潭區北龍路",
        "type": "鍍膜/美容",
        "price": "💰 1500+",
        "rating": 4.7,
        "desc": "上國三交流道前最後整理的好地方，老闆很細心。",
    },

    # --- 大溪區 (Daxi) ---
    {
        "name": "崎頂洗車場",
        "district": "大溪區",
        "location": "大溪區介壽路",
        "type": "人工洗車",
        "price": "💰 250 起",
        "rating": 4.1,
        "desc": "大溪老街附近，價格實惠，洗完順便買豆干回家。",
    },

    # --- 大園區 (Dayuan) ---
    {
        "name": "青埔高鐵洗車中心",
        "district": "大園區",
        "location": "大園區高鐵南路",
        "type": "精緻護理",
        "price": "💰 800+",
        "rating": 4.5,
        "desc": "靠近青埔，設備很新，適合開好車的族人。",
    },

    # --- 桃園區 (Taoyuan) ---
    {
        "name": "IPO 汽車美容 (藝文店)",
        "district": "桃園區",
        "location": "桃園區大興西路",
        "type": "高階鍍膜",
        "price": "💰 2000+",
        "rating": 4.8,
        "desc": "藝文特區名店，品質沒話說。",
    },
    {
        "name": "魔法泡泡自助洗 (經國店)",
        "district": "桃園區",
        "location": "桃園區經國路",
        "type": "自助洗車",
        "price": "💰 投幣式",
        "rating": 4.4,
        "desc": "場地大、水壓強。",
    },

    # --- 中壢區 (Zhongli) ---
    {
        "name": "車太炫自助洗車 (環北店)",
        "district": "中壢區",
        "location": "中壢區環北路",
        "type": "自助洗車",
        "price": "💰 投幣式",
        "rating": 4.5,
        "desc": "中壢設備最好的自助洗之一。",
    },
    {
        "name": "潔光車體美容",
        "district": "中壢區",
        "location": "中壢區延平路",
        "type": "精緻洗車",
        "price": "💰 1200+",
        "rating": 4.7,
        "desc": "適合家庭車，內裝清得很乾淨。",
    },

    # --- 八德區 (Bade) ---
    {
        "name": "車車澡堂",
        "district": "八德區",
        "location": "八德區介壽路",
        "type": "自助洗車",
        "price": "💰 20元起",
        "rating": 4.3,
        "desc": "介壽路往大溪方向順路。",
    },

    # --- 平鎮區 (Pingzhen) ---
    {
        "name": "魔法車體美研",
        "district": "平鎮區",
        "location": "平鎮區環南路",
        "type": "精緻護理",
        "price": "💰 600+",
        "rating": 4.6,
        "desc": "環南路洗車一條街首選。",
    },

    # --- 蘆竹區 (Luzhu) ---
    {
        "name": "麗鉅專業汽車美容",
        "district": "蘆竹區",
        "location": "蘆竹區南崁路",
        "type": "頂級護理",
        "price": "💰 2000+",
        "rating": 4.8,
        "desc": "南崁評價最高。",
    },
    
    # --- 龜山區 (Guishan) ---
    {
        "name": "G'ZOX 林口店",
        "district": "龜山區",
        "location": "龜山區文化三路",
        "type": "日本鍍膜",
        "price": "💰 3000+",
        "rating": 4.9,
        "desc": "日本第一品牌，效果持久。",
    },
]

# ---------------------------------------------------------
# 2. App 主程式
# ---------------------------------------------------------
st.set_page_config(page_title="桃園全區 - 返鄉愛車特搜", page_icon="🚙", layout="centered")

# 標題
st.title("🚙 三一協會：返鄉前去洗車")
st.markdown(
    """
    <div style="background-color: #0277BD; padding: 15px; border-radius: 10px; color: white; margin-bottom: 20px;">
        <strong>Nga'ay ho! 13個行政區都有！</strong><br>
        不管您住新屋、觀音還是復興，我們都幫您找到了。<br>
        如果當地選擇太少，系統還會推薦您去隔壁區喔！
    </div>
    """, 
    unsafe_allow_html=True
)

# --- 區域選擇 (包含全桃園 13 區) ---
st.write("### 👇 請選擇您居住的區域")

# 定義所有區域順序
districts_list = [
    "全部顯示", 
    "桃園區", "中壢區", "平鎮區", "八德區", 
    "楊梅區", "蘆竹區", "龜山區", "龍潭區", 
    "大溪區", "大園區", "觀音區", "新屋區", "復興區"
]

selected_area = st.selectbox("選擇區域", districts_list, index=0)

st.divider()

# --- 鄰近區域推薦邏輯 (關鍵功能!) ---
# 這裡設定：如果選了A區，但A區店很少，就推薦去B區
nearby_recommendation = {
    "新屋區": "楊梅區",
    "觀音區": "中壢區",
    "大園區": "蘆竹區",
    "復興區": "大溪區",
    "大溪區": "八德區",
}

# --- 篩選資料 ---
filtered_shops = [shop for shop in shops_data if selected_area == "全部顯示" or shop["district"] == selected_area]

# --- 顯示結果與貼心提醒 ---

# 1. 如果選了比較偏遠的區域，顯示提示
if selected_area in nearby_recommendation:
    neighbor = nearby_recommendation[selected_area]
    st.info(f"💡 **{selected_area} 的選擇可能較少**，若想做深層美容，推薦您可以往 **『{neighbor}』** 找找看喔！")

# 2. 顯示店家卡片
if not filtered_shops:
    if selected_area == "復興區":
        st.warning("🏔️ 復興區山上以天然山泉水洗車為主，建議下山到 **大溪** 會比較多專業店家喔！")
    else:
        st.warning(f"⚠️ {selected_area} 目前資料庫還在擴充中，請參考鄰近區域。")
else:
    st.caption(f"在 {selected_area} 找到 {len(filtered_shops)} 間店家")
    
    for shop in filtered_shops:
        with st.container(border=True):
            col1, col2 = st.columns([7, 3])
            
            with col1:
                st.subheader(f"{shop['name']}")
                st.caption(f"📍 {shop['district']} | {shop['type']}")
                st.markdown(f"**{shop['price']}**")
                st.write(f"💬 {shop['desc']}")
            
            with col2:
                st.markdown(f"<h2 style='text-align:center; color:#FFC107; margin:0;'>★ {shop['rating']}</h2>", unsafe_allow_html=True)
                st.write("")
                map_url = f"https://www.google.com/maps/search/?api=1&query={shop['name']}+{shop['location']}"
                st.link_button("🚗 導航去", map_url, use_container_width=True, type="primary")

# --- 底部 ---
st.divider()
st.markdown(
    "<div style='text-align: center; color: #888;'>桃園三一協會 Taoyuan Sanyi Association © 2026<br>照顧每一位族人的愛車</div>", 
    unsafe_allow_html=True
)

