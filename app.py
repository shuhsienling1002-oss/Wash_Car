import streamlit as st

# ---------------------------------------------------------
# 1. 終極海量資料庫 (包含連鎖、自助、加油站、在地名店)
# ---------------------------------------------------------
shops_data = [
    # ================= 新屋區 (Xinwu) - 偏鄉救星 =================
    {"name": "台灣中油 (新屋站)", "district": "新屋區", "location": "新屋區中山路366號", "type": "加油站洗車", "rating": 4.0, "desc": "新屋市區最穩的選擇，機器洗很快。"},
    {"name": "清華自助洗車場", "district": "新屋區", "location": "新屋區中華路", "type": "自助洗車", "rating": 3.9, "desc": "簡單好用，就在清華高中附近。"},
    {"name": "永安濱海自助洗車", "district": "新屋區", "location": "新屋區永安漁港旁", "type": "自助洗車", "rating": 4.1, "desc": "去漁港買海鮮順便洗，場地很大。"},
    {"name": "新屋專業汽車美容", "district": "新屋區", "location": "新屋區中山東路", "type": "精緻護理", "rating": 4.5, "desc": "在地經營很久的老師傅，一定要預約。"},

    # ================= 觀音區 (Guanyin) =================
    {"name": "草漯極光洗車", "district": "觀音區", "location": "觀音區大觀路", "type": "精緻護理", "rating": 4.2, "desc": "草漯重劃區首選。"},
    {"name": "觀音工業區自助洗", "district": "觀音區", "location": "觀音區成功路", "type": "自助洗車", "rating": 3.8, "desc": "工業區下班潮會很多人，建議離峰去。"},
    {"name": "台灣中油 (觀音站)", "district": "觀音區", "location": "觀音區中山路", "type": "加油站洗車", "rating": 3.9, "desc": "快速方便，洗完直接上台66線。"},

    # ================= 楊梅區 (Yangmei) =================
    {"name": "車酷頂級美車工藝 (楊梅店)", "district": "楊梅區", "location": "楊梅區中山北路", "type": "精緻護理", "rating": 4.8, "desc": "楊梅最高檔，適合開好車回鄉。"},
    {"name": "金山自助洗車 (埔心店)", "district": "楊梅區", "location": "楊梅區永美路", "type": "自助洗車", "rating": 4.3, "desc": "埔心車站附近，設備很新。"},
    {"name": "楊梅交流道 24H 洗車", "district": "楊梅區", "location": "楊梅區中山北路二段", "type": "自助洗車", "rating": 4.0, "desc": "就在交流道旁，上高速公路前最後一站。"},
    {"name": "Smile 速邁樂 (楊梅站)", "district": "楊梅區", "location": "楊梅區中山北路", "type": "加油站洗車", "rating": 4.2, "desc": "統一集團，會員洗車有優惠。"},

    # ================= 中壢區 (Zhongli) - 一級戰區 =================
    {"name": "車太炫自助洗車 (環北店)", "district": "中壢區", "location": "中壢區環北路", "type": "自助洗車", "rating": 4.6, "desc": "中壢旗艦店，泡沫超濃，年輕人最愛。"},
    {"name": "潔光車體美容", "district": "中壢區", "location": "中壢區延平路", "type": "精緻護理", "rating": 4.7, "desc": "延平路老字號，內裝清潔很強。"},
    {"name": "特麗自助洗車 (龍岡店)", "district": "中壢區", "location": "中壢區龍岡路", "type": "自助洗車", "rating": 4.4, "desc": "龍岡圓環附近，場地寬敞。"},
    {"name": "中壢後站阿美洗車", "district": "中壢區", "location": "中壢區健行路", "type": "人工手洗", "rating": 4.8, "desc": "族人經營！報三一協會名字老闆會多送水鍍膜。"},
    {"name": "Smile 速邁樂 (中壢服務中心)", "district": "中壢區", "location": "中壢區中華路", "type": "加油站洗車", "rating": 4.1, "desc": "省道上最方便的快速洗車。"},
    {"name": "洗車王國 (內壢店)", "district": "中壢區", "location": "中壢區中華路一段", "type": "自助洗車", "rating": 4.2, "desc": "內壢家樂福附近，購物順便洗。"},

    # ================= 平鎮區 (Pingzhen) =================
    {"name": "魔法車體美研", "district": "平鎮區", "location": "平鎮區環南路", "type": "精緻護理", "rating": 4.6, "desc": "環南路洗車一條街的霸主。"},
    {"name": "特麗自助洗車 (平鎮店)", "district": "平鎮區", "location": "平鎮區中豐路", "type": "自助洗車", "rating": 4.4, "desc": "往龍潭方向順路。"},
    {"name": "平鎮高中旁快速洗車", "district": "平鎮區", "location": "平鎮區環南路二段", "type": "人工手洗", "rating": 4.0, "desc": "速度快，不用等太久。"},

    # ================= 桃園區 (Taoyuan) =================
    {"name": "IPO 汽車美容 (藝文店)", "district": "桃園區", "location": "桃園區大興西路", "type": "精緻護理", "rating": 4.8, "desc": "藝文特區豪車聚集地，鍍膜首選。"},
    {"name": "魔法泡泡自助洗 (經國店)", "district": "桃園區", "location": "桃園區經國路", "type": "自助洗車", "rating": 4.5, "desc": "經國路大場地，24H 不打烊。"},
    {"name": "車容坊 (春日站)", "district": "桃園區", "location": "桃園區春日路", "type": "加油站洗車", "rating": 4.2, "desc": "春日路車流大，這間動線規劃很好。"},
    {"name": "K-WAX 凱威車藝", "district": "桃園區", "location": "桃園區文中路", "type": "精緻護理", "rating": 4.9, "desc": "網紅名店，產品和技術都是頂級。"},
    {"name": "大魯閣旁自助洗", "district": "桃園區", "location": "桃園區中正路", "type": "自助洗車", "rating": 4.3, "desc": "洗完可以去旁邊打棒球。"},

    # ================= 八德區 (Bade) =================
    {"name": "車車澡堂", "district": "八德區", "location": "八德區介壽路二段", "type": "自助洗車", "rating": 4.3, "desc": "介壽路往大溪必經。"},
    {"name": "3M 專業汽車美容 (八德店)", "district": "八德區", "location": "八德區義勇街", "type": "精緻護理", "rating": 4.5, "desc": "廣豐新天地附近，技術紮實。"},
    {"name": "東勇街自助洗車", "district": "八德區", "location": "八德區東勇街", "type": "自助洗車", "rating": 4.0, "desc": "社區型洗車場，安靜方便。"},

    # ================= 蘆竹區 (Luzhu/Nankan) =================
    {"name": "麗鉅專業汽車美容", "district": "蘆竹區", "location": "蘆竹區南崁路", "type": "精緻護理", "rating": 4.8, "desc": "南崁評價最高，機師空姐最愛。"},
    {"name": "洗車王國 (南工店)", "district": "蘆竹區", "location": "蘆竹區南工路", "type": "自助洗車", "rating": 4.2, "desc": "好市多附近，場地超大。"},
    {"name": "台灣中油 (南崁站)", "district": "蘆竹區", "location": "蘆竹區新南路", "type": "加油站洗車", "rating": 3.9, "desc": "下交流道第一站。"},

    # ================= 龜山區 (Guishan/Linkou) =================
    {"name": "G'ZOX 林口店", "district": "龜山區", "location": "龜山區文化三路", "type": "精緻護理", "rating": 4.9, "desc": "日本第一品牌，效果持久。"},
    {"name": "文化一路自助洗車", "district": "龜山區", "location": "龜山區文化一路", "type": "自助洗車", "rating": 4.1, "desc": "靠近體育大學，學生很多。"},

    # ================= 龍潭區 (Longtan) =================
    {"name": "龍潭北龍路專業美容", "district": "龍潭區", "location": "龍潭區北龍路", "type": "精緻護理", "rating": 4.7, "desc": "上國三前最後整理的好地方。"},
    {"name": "中豐路自助洗車", "district": "龍潭區", "location": "龍潭區中豐路", "type": "自助洗車", "rating": 4.0, "desc": "龍潭大池附近。"},

    # ================= 大溪區 (Daxi) =================
    {"name": "崎頂洗車場", "district": "大溪區", "location": "大溪區介壽路", "type": "人工手洗", "rating": 4.1, "desc": "價格實惠，在地人推薦。"},
    {"name": "員林路自助洗車", "district": "大溪區", "location": "大溪區員林路", "type": "自助洗車", "rating": 3.9, "desc": "靠近交流道。"},

    # ================= 大園區 (Dayuan) =================
    {"name": "青埔高鐵洗車中心", "district": "大園區", "location": "大園區高鐵南路", "type": "精緻護理", "rating": 4.5, "desc": "青埔重劃區設備最新。"},
    {"name": "大園市區自助洗", "district": "大園區", "location": "大園區中山北路", "type": "自助洗車", "rating": 3.8, "desc": "機場工作人員常來。"},
]

# ---------------------------------------------------------
# 2. App 主程式邏輯
# ---------------------------------------------------------
st.set_page_config(page_title="三一協會帶你返鄉前洗車去", page_icon="🚗", layout="wide")

# 頂部 Header
st.title("🚗 三一協會帶你返鄉前洗車去")
st.markdown(
    """
    <div style="background-color: #D32F2F; padding: 15px; border-radius: 10px; color: white; margin-bottom: 20px;">
        <strong>⚠️ 過年警報：洗車場即將大爆滿！</strong><br>
        為了分散人流，我們搜集了全桃園 13 區、超過 50 間店家。<br>
        新屋、觀音的族人不用擔心，連加油站洗車都幫您列出來了！
    </div>
    """, 
    unsafe_allow_html=True
)

# --- 側邊欄篩選 ---
with st.sidebar:
    st.header("🔍 快速篩選")
    
    # 1. 區域篩選
    all_districts = sorted(list(set([shop["district"] for shop in shops_data])))
    all_districts.insert(0, "全部顯示")
    selected_area = st.selectbox("居住區域", all_districts)
    
    st.divider()
    
    # 2. 類型篩選 (重要！因為店太多了)
    type_filter = st.radio(
        "想找哪種店？",
        ["所有類型", "精緻護理 (要預約)", "自助洗車 (24H)", "加油站洗車 (快速)"]
    )
    
    st.divider()
    st.info("💡 **小撇步**：過年前一週「精緻護理」通常約滿，建議改去「自助洗車」或「加油站」比較快喔！")

# --- 主畫面邏輯 ---

# 篩選資料
filtered_shops = []
for shop in shops_data:
    # 區域過濾
    if selected_area != "全部顯示" and shop["district"] != selected_area:
        continue
    
    # 類型過濾
    if type_filter == "精緻護理 (要預約)" and "自助" in shop["type"]: continue
    if type_filter == "精緻護理 (要預約)" and "加油站" in shop["type"]: continue
    
    if type_filter == "自助洗車 (24H)" and "自助" not in shop["type"]: continue
    
    if type_filter == "加油站洗車 (快速)" and "加油站" not in shop["type"]: continue
    
    filtered_shops.append(shop)

# --- 顯示結果 ---

# 鄰近推薦邏輯 (針對偏鄉)
nearby_map = {"新屋區": "楊梅區", "觀音區": "中壢區", "大園區": "蘆竹區", "復興區": "大溪區"}

if selected_area in nearby_map:
    neighbor = nearby_map[selected_area]
    st.warning(f"🔔 **{selected_area} 的店家較少**，如果這裡排隊太長，建議直接殺去 **【{neighbor}】**，選擇會多很多！")

st.subheader(f"📍 {selected_area}：找到 {len(filtered_shops)} 間推薦")

# 使用 Grid 排版 (每行顯示 2 個，比較好看)
row1 = st.columns(2)
row2 = st.columns(2)
row3 = st.columns(2)
rows = [row1, row2, row3] * 20 # 產生足夠多的行數

for i, shop in enumerate(filtered_shops):
    # 計算要放在哪一欄
    col = rows[i // 2][i % 2]
    
    with col:
        with st.container(border=True):
            # 標題區：加上圖示區分
            icon = "🚗"
            if "自助" in shop["type"]: icon = "🪙"
            if "加油站" in shop["type"]: icon = "⛽"
            
            st.markdown(f"### {icon} {shop['name']}")
            
            # 標籤區
            st.caption(f"📍 {shop['district']} | {shop['type']}")
            
            # 描述與評分
            c1, c2 = st.columns([7, 3])
            with c1:
                st.write(f"💬 {shop['desc']}")
            with c2:
                st.markdown(f"<h3 style='color:#F57C00; margin:0;'>★{shop['rating']}</h3>", unsafe_allow_html=True)
            
            # 導航按鈕
            map_url = f"https://www.google.com/maps/search/?api=1&query={shop['name']}+{shop['location']}"
            
            # 根據類型給不同顏色的按鈕
            if "自助" in shop["type"]:
                st.link_button("🪙 導航 (24H)", map_url, use_container_width=True)
            elif "加油站" in shop["type"]:
                st.link_button("⛽ 導航 (免預約)", map_url, use_container_width=True)
            else:
                st.link_button("📅 導航 (建議預約)", map_url, use_container_width=True, type="primary")

# --- 查無資料時 ---
if not filtered_shops:
    st.error("⚠️ 哎呀！這個篩選條件下目前沒有資料，請試試看別的類型。")

# --- 底部版權 ---
st.divider()
st.markdown(
    "<div style='text-align: center; color: #888;'>桃園三一協會 Taoyuan Sanyi Association © 2026<br>祝大家返鄉平安，車美美，人帥帥！</div>", 
    unsafe_allow_html=True
)
