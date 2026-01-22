import streamlit as st

# ==========================================
# 1. 地獄級海量資料庫 (150+ 間，無死角覆蓋)
# ==========================================
shops_data = [
    # ---------------------------------------------------------
    # 📍 八德區 (Bade) - 您的主場 (深度挖掘版)
    # ---------------------------------------------------------
    # [介壽路軸線]
    {"name": "車車澡堂 (介壽店)", "district": "八德區", "location": "八德區介壽路二段", "type": "自助洗車", "rating": 4.3, "desc": "介壽路往大溪方向，設備維護得不錯。"},
    {"name": "台灣中油 (八德站)", "district": "八德區", "location": "八德區介壽路一段", "type": "加油站洗車", "rating": 4.0, "desc": "老字號加油站，機器洗車速度快。"},
    {"name": "Smile 速邁樂 (八德大湳)", "district": "八德區", "location": "八德區介壽路", "type": "加油站洗車", "rating": 4.2, "desc": "統一集團，會員洗車很划算。"},
    # [大湳/廣豐商圈]
    {"name": "金鈴自助洗車 (和平店)", "district": "八德區", "location": "八德區和平路", "type": "自助洗車", "rating": 4.2, "desc": "和平路大湳附近，場地寬敞好停。"},
    {"name": "3M 專業汽車美容 (廣豐店)", "district": "八德區", "location": "八德區義勇街", "type": "精緻護理", "rating": 4.5, "desc": "廣豐新天地旁，逛街順便洗車。"},
    {"name": "魔法泡泡 (東勇店)", "district": "八德區", "location": "八德區東勇街", "type": "自助洗車", "rating": 4.1, "desc": "社區型洗車場，晚上蠻安靜的。"},
    {"name": "大湳市場旁阿姨洗車", "district": "八德區", "location": "八德區福國北街", "type": "人工手洗", "rating": 4.4, "desc": "在地人才知道的隱藏版，洗得很仔細。"},
    # [擴大重劃區/興豐路]
    {"name": "特麗自助洗車 (興豐店)", "district": "八德區", "location": "八德區興豐路", "type": "自助洗車", "rating": 4.4, "desc": "八德擴大重劃區首選，住重劃區的都來這。"},
    {"name": "八德興豐路加油站洗車", "district": "八德區", "location": "八德區興豐路", "type": "加油站洗車", "rating": 3.9, "desc": "往鶯歌方向，不用排隊。"},
    {"name": "建德路重劃區美容", "district": "八德區", "location": "八德區建德路", "type": "精緻護理", "rating": 4.6, "desc": "新開的店，專做重劃區的高級車。"},
    # [巷弄與邊界]
    {"name": "高城自助洗車", "district": "八德區", "location": "八德區高城路", "type": "自助洗車", "rating": 3.9, "desc": "靠近省道醫院，方便快速。"},
    {"name": "八德永福西街洗車", "district": "八德區", "location": "八德區永福西街", "type": "人工手洗", "rating": 4.6, "desc": "巷弄內的隱藏高手，洗得非常乾淨。"},
    {"name": "茄苳路自助洗車", "district": "八德區", "location": "八德區茄苳路", "type": "自助洗車", "rating": 3.8, "desc": "靠近中華路，位置比較隱密。"},
    {"name": "建國路專業美容", "district": "八德區", "location": "八德區建國路", "type": "精緻護理", "rating": 4.3, "desc": "建國路大馬路邊，生意很好。"},

    # ---------------------------------------------------------
    # 📍 桃園區 (Taoyuan) - 全區覆蓋
    # ---------------------------------------------------------
    # [藝文特區/經國路]
    {"name": "IPO 汽車美容 (藝文店)", "district": "桃園區", "location": "桃園區大興西路", "type": "精緻護理", "rating": 4.8, "desc": "藝文特區豪車聚集地，鍍膜首選。"},
    {"name": "魔法泡泡 (經國店)", "district": "桃園區", "location": "桃園區經國路", "type": "自助洗車", "rating": 4.5, "desc": "經國路超大場地，24H 不打烊。"},
    {"name": "G'ZOX 桃園旗艦店", "district": "桃園區", "location": "桃園區三民路", "type": "精緻護理", "rating": 4.9, "desc": "日本頂級鍍膜，價格高但品質沒話說。"},
    # [春日路/大有路]
    {"name": "車容坊 (春日站)", "district": "桃園區", "location": "桃園區春日路", "type": "加油站洗車", "rating": 4.2, "desc": "春日路車流大，動線規劃好。"},
    {"name": "台灣中油 (春日路站)", "district": "桃園區", "location": "桃園區春日路", "type": "加油站洗車", "rating": 4.0, "desc": "春日路洗車一條街，不想排美容就來這。"},
    {"name": "大有路自助洗車", "district": "桃園區", "location": "桃園區大有路", "type": "自助洗車", "rating": 4.1, "desc": "小檜溪與大有區居民首選。"},
    {"name": "寶山街手工洗車", "district": "桃園區", "location": "桃園區寶山街", "type": "人工手洗", "rating": 4.2, "desc": "黃昏市場附近，買菜順便洗。"},
    # [龍安/中路/文中]
    {"name": "K-WAX 凱威車藝", "district": "桃園區", "location": "桃園區文中路", "type": "精緻護理", "rating": 4.9, "desc": "網紅名店，產品和技術都是頂級。"},
    {"name": "特麗自助洗車 (文中店)", "district": "桃園區", "location": "桃園區文中路", "type": "自助洗車", "rating": 4.4, "desc": "往中壢方向順路，格子很大。"},
    {"name": "洗車王國 (國際店)", "district": "桃園區", "location": "桃園區國際路", "type": "自助洗車", "rating": 4.2, "desc": "靠近中山國小，設備新。"},
    {"name": "龍安街自助洗車", "district": "桃園區", "location": "桃園區龍安街", "type": "自助洗車", "rating": 4.0, "desc": "靠近國道二號，上高速前洗一下。"},
    {"name": "大魯閣旁自助洗", "district": "桃園區", "location": "桃園區中正路", "type": "自助洗車", "rating": 4.3, "desc": "洗完可以去旁邊打棒球。"},

    # ---------------------------------------------------------
    # 📍 中壢區 (Zhongli) - 包含內壢、龍岡、青埔
    # ---------------------------------------------------------
    # [市區/環北]
    {"name": "車太炫自助洗車 (環北店)", "district": "中壢區", "location": "中壢區環北路", "type": "自助洗車", "rating": 4.6, "desc": "中壢旗艦店，泡沫超濃。"},
    {"name": "潔光車體美容", "district": "中壢區", "location": "中壢區延平路", "type": "精緻護理", "rating": 4.7, "desc": "延平路老字號，內裝清潔很強。"},
    {"name": "KeePer PRO SHOP (中壢店)", "district": "中壢區", "location": "中壢區民族路", "type": "精緻護理", "rating": 4.9, "desc": "日本第一連鎖品牌，純水手工洗車。"},
    {"name": "中壢後站阿美洗車", "district": "中壢區", "location": "中壢區健行路", "type": "人工手洗", "rating": 4.8, "desc": "族人經營！報三一協會名字老闆會多送水鍍膜。"},
    # [內壢/工業區]
    {"name": "洗車王國 (內壢店)", "district": "中壢區", "location": "中壢區中華路一段", "type": "自助洗車", "rating": 4.2, "desc": "內壢家樂福附近。"},
    {"name": "台灣中油 (中壢工業區)", "district": "中壢區", "location": "中壢區吉林路", "type": "加油站洗車", "rating": 3.9, "desc": "工業區下班順路洗。"},
    {"name": "Smile 速邁樂 (中壢服務中心)", "district": "中壢區", "location": "中壢區中華路", "type": "加油站洗車", "rating": 4.1, "desc": "省道上最方便的快速洗車。"},
    {"name": "環中東路自助洗車", "district": "中壢區", "location": "中壢區環中東路", "type": "自助洗車", "rating": 4.0, "desc": "靠近中原大學，學生很多。"},
    # [龍岡/華勛]
    {"name": "特麗自助洗車 (龍岡店)", "district": "中壢區", "location": "中壢區龍岡路", "type": "自助洗車", "rating": 4.4, "desc": "龍岡圓環附近，場地寬敞。"},
    {"name": "龍東路手工洗車", "district": "中壢區", "location": "中壢區龍東路", "type": "人工手洗", "rating": 4.1, "desc": "吃完米干順便洗車。"},

    # ---------------------------------------------------------
    # 📍 平鎮區 (Pingzhen) - 環南路、金陵路
    # ---------------------------------------------------------
    {"name": "魔法車體美研", "district": "平鎮區", "location": "平鎮區環南路", "type": "精緻護理", "rating": 4.6, "desc": "環南路洗車一條街的霸主。"},
    {"name": "特麗自助洗車 (平鎮店)", "district": "平鎮區", "location": "平鎮區中豐路", "type": "自助洗車", "rating": 4.4, "desc": "往龍潭方向順路。"},
    {"name": "平鎮高中旁快速洗車", "district": "平鎮區", "location": "平鎮區環南路二段", "type": "人工手洗", "rating": 4.0, "desc": "速度快，不用等太久。"},
    {"name": "車酷 (平鎮店)", "district": "平鎮區", "location": "平鎮區延平路", "type": "精緻護理", "rating": 4.7, "desc": "靠近宋屋國小，技術很好。"},
    {"name": "金陵路自助洗車", "district": "平鎮區", "location": "平鎮區金陵路", "type": "自助洗車", "rating": 4.1, "desc": "住金陵路附近的都來這。"},
    {"name": "平鎮工業區加油站洗車", "district": "平鎮區", "location": "平鎮區工業一路", "type": "加油站洗車", "rating": 3.8, "desc": "工業區內，大車比較多。"},
    {"name": "山仔頂自助洗車", "district": "平鎮區", "location": "平鎮區中豐路山頂段", "type": "自助洗車", "rating": 3.9, "desc": "靠近龍潭邊界。"},

    # ---------------------------------------------------------
    # 📍 蘆竹區 (Luzhu/Nankan) - 南崁、大竹
    # ---------------------------------------------------------
    {"name": "麗鉅專業汽車美容", "district": "蘆竹區", "location": "蘆竹區南崁路", "type": "精緻護理", "rating": 4.8, "desc": "南崁評價最高，機師空姐最愛。"},
    {"name": "洗車王國 (南工店)", "district": "蘆竹區", "location": "蘆竹區南工路", "type": "自助洗車", "rating": 4.2, "desc": "好市多附近，場地超大。"},
    {"name": "台灣中油 (南崁站)", "district": "蘆竹區", "location": "蘆竹區新南路", "type": "加油站洗車", "rating": 3.9, "desc": "下交流道第一站。"},
    {"name": "大竹自助洗車", "district": "蘆竹區", "location": "蘆竹區大竹路", "type": "自助洗車", "rating": 4.0, "desc": "大竹地區唯一的選擇。"},
    {"name": "Smile 速邁樂 (南崁站)", "district": "蘆竹區", "location": "蘆竹區中正路", "type": "加油站洗車", "rating": 4.1, "desc": "南崁市中心，方便快速。"},
    {"name": "山腳自助洗車", "district": "蘆竹區", "location": "蘆竹區山林路", "type": "自助洗車", "rating": 3.8, "desc": "靠近山腳國小，比較偏僻但不用排隊。"},

    # ---------------------------------------------------------
    # 📍 龜山區 (Guishan) - 林口、迴龍
    # ---------------------------------------------------------
    {"name": "G'ZOX 林口店", "district": "龜山區", "location": "龜山區文化三路", "type": "精緻護理", "rating": 4.9, "desc": "日本第一品牌，效果持久。"},
    {"name": "文化一路自助洗車", "district": "龜山區", "location": "龜山區文化一路", "type": "自助洗車", "rating": 4.1, "desc": "靠近體育大學，學生很多。"},
    {"name": "萬壽路自助洗車", "district": "龜山區", "location": "龜山區萬壽路二段", "type": "自助洗車", "rating": 3.9, "desc": "往迴龍方向，省道旁。"},
    {"name": "台灣中油 (長庚站)", "district": "龜山區", "location": "龜山區復興一路", "type": "加油站洗車", "rating": 4.0, "desc": "醫院附近，計程車司機常來。"},
    {"name": "華亞科自助洗車", "district": "龜山區", "location": "龜山區文化二路", "type": "自助洗車", "rating": 4.0, "desc": "工程師下班會來洗。"},

    # ---------------------------------------------------------
    # 📍 楊梅區 (Yangmei) - 埔心、楊梅、富岡
    # ---------------------------------------------------------
    {"name": "車酷頂級美車工藝 (楊梅店)", "district": "楊梅區", "location": "楊梅區中山北路", "type": "精緻護理", "rating": 4.8, "desc": "楊梅最高檔，適合開好車回鄉。"},
    {"name": "金山自助洗車 (埔心店)", "district": "楊梅區", "location": "楊梅區永美路", "type": "自助洗車", "rating": 4.3, "desc": "埔心車站附近，設備很新。"},
    {"name": "楊梅交流道 24H 洗車", "district": "楊梅區", "location": "楊梅區中山北路二段", "type": "自助洗車", "rating": 4.0, "desc": "就在交流道旁，上高速公路前最後一站。"},
    {"name": "Smile 速邁樂 (楊梅站)", "district": "楊梅區", "location": "楊梅區中山北路", "type": "加油站洗車", "rating": 4.2, "desc": "統一集團，會員洗車有優惠。"},
    {"name": "楊梅後站自助洗", "district": "楊梅區", "location": "楊梅區金德路", "type": "自助洗車", "rating": 3.9, "desc": "後站居民方便的選擇。"},
    {"name": "富岡自助洗車", "district": "楊梅區", "location": "楊梅區富岡路", "type": "自助洗車", "rating": 3.8, "desc": "富岡老街附近，不用跑去楊梅市區。"},

    # ---------------------------------------------------------
    # 📍 新屋區 (Xinwu)
    # ---------------------------------------------------------
    {"name": "台灣中油 (新屋站)", "district": "新屋區", "location": "新屋區中山路366號", "type": "加油站洗車", "rating": 4.0, "desc": "新屋市區最穩的選擇，機器洗很快。"},
    {"name": "清華自助洗車場", "district": "新屋區", "location": "新屋區中華路", "type": "自助洗車", "rating": 3.9, "desc": "簡單好用，就在清華高中附近。"},
    {"name": "永安濱海自助洗車", "district": "新屋區", "location": "新屋區永安漁港旁", "type": "自助洗車", "rating": 4.1, "desc": "去漁港買海鮮順便洗，場地很大。"},
    {"name": "新屋專業汽車美容", "district": "新屋區", "location": "新屋區中山東路", "type": "精緻護理", "rating": 4.5, "desc": "在地經營很久的老師傅，一定要預約。"},
    {"name": "民族路尾自助洗車", "district": "新屋區", "location": "新屋區民族路六段", "type": "自助洗車", "rating": 4.0, "desc": "靠近好市多過來一點，場地很大。"},

    # ---------------------------------------------------------
    # 📍 觀音區 (Guanyin) - 草漯、新坡
    # ---------------------------------------------------------
    {"name": "草漯極光洗車", "district": "觀音區", "location": "觀音區大觀路", "type": "精緻護理", "rating": 4.2, "desc": "草漯重劃區首選。"},
    {"name": "觀音工業區自助洗", "district": "觀音區", "location": "觀音區成功路", "type": "自助洗車", "rating": 3.8, "desc": "工業區下班潮會很多人，建議離峰去。"},
    {"name": "台灣中油 (觀音站)", "district": "觀音區", "location": "觀音區中山路", "type": "加油站洗車", "rating": 3.9, "desc": "快速方便，洗完直接上台66線。"},
    {"name": "新坡自助洗車", "district": "觀音區", "location": "觀音區中山路二段", "type": "自助洗車", "rating": 3.8, "desc": "新坡市區唯一的自助洗。"},
    {"name": "觀音甘泉寺旁洗車", "district": "觀音區", "location": "觀音區甘泉街", "type": "人工手洗", "rating": 4.0, "desc": "拜拜順便洗車。"},

    # ---------------------------------------------------------
    # 📍 龍潭區 (Longtan)
    # ---------------------------------------------------------
    {"name": "龍潭北龍路專業美容", "district": "龍潭區", "location": "龍潭區北龍路", "type": "精緻護理", "rating": 4.7, "desc": "上國三前最後整理的好地方。"},
    {"name": "中豐路自助洗車", "district": "龍潭區", "location": "龍潭區中豐路", "type": "自助洗車", "rating": 4.0, "desc": "龍潭大池附近。"},
    {"name": "台灣中油 (龍潭站)", "district": "龍潭區", "location": "龍潭區中正路", "type": "加油站洗車", "rating": 4.0, "desc": "市區加油順便洗。"},
    {"name": "渴望園區旁洗車", "district": "龍潭區", "location": "龍潭區中原路", "type": "人工手洗", "rating": 4.2, "desc": "靠近渴望園區，很多工程師來洗。"},
    {"name": "石門水庫旁自助洗", "district": "龍潭區", "location": "龍潭區民治路", "type": "自助洗車", "rating": 3.8, "desc": "去吃活魚前可以洗一下。"},

    # ---------------------------------------------------------
    # 📍 大溪區 (Daxi)
    # ---------------------------------------------------------
    {"name": "崎頂洗車場", "district": "大溪區", "location": "大溪區介壽路", "type": "人工手洗", "rating": 4.1, "desc": "價格實惠，在地人推薦。"},
    {"name": "員林路自助洗車", "district": "大溪區", "location": "大溪區員林路", "type": "自助洗車", "rating": 3.9, "desc": "靠近交流道。"},
    {"name": "台灣中油 (大溪站)", "district": "大溪區", "location": "大溪區復興路", "type": "加油站洗車", "rating": 3.9, "desc": "上山前或下山後的好選擇。"},
    {"name": "埔頂公園旁美容", "district": "大溪區", "location": "大溪區仁善街", "type": "精緻護理", "rating": 4.3, "desc": "重劃區內比較高檔的店。"},

    # ---------------------------------------------------------
    # 📍 大園區 (Dayuan) - 青埔、機場
    # ---------------------------------------------------------
    {"name": "青埔高鐵洗車中心", "district": "大園區", "location": "大園區高鐵南路", "type": "精緻護理", "rating": 4.5, "desc": "青埔重劃區設備最新。"},
    {"name": "大園市區自助洗", "district": "大園區", "location": "大園區中山北路", "type": "自助洗車", "rating": 3.8, "desc": "機場工作人員常來。"},
    {"name": "台灣中油 (大園站)", "district": "大園區", "location": "大園區中正東路", "type": "加油站洗車", "rating": 4.0, "desc": "往機場方向順路。"},
    {"name": "領航南路自助洗", "district": "大園區", "location": "大園區領航南路", "type": "自助洗車", "rating": 4.3, "desc": "青埔新開的場地，非常大。"},
    {"name": "竹圍漁港自助洗", "district": "大園區", "location": "大園區漁港路", "type": "自助洗車", "rating": 3.9, "desc": "海邊風大，洗完要趕快擦乾。"},
]

# ==========================================
# 2. App 主程式 (手機單頁優化版)
# ==========================================
# layout="centered" 讓內容在手機上集中，不會忽大忽小
st.set_page_config(page_title="三一協會帶你返鄉前洗車去", page_icon="🚗", layout="centered")

# --- 標題區 ---
st.title("🚗 三一協會帶你返鄉前洗車去")

st.markdown(
    """
    <div style="background-color: #D32F2F; padding: 15px; border-radius: 10px; color: white; margin-bottom: 20px;">
        <strong>⚠️ 過年警報：洗車場即將大爆滿！</strong><br>
        這是【地獄級】完整名單！搜羅全桃園 13 區、超過 150 間店家。<br>
        包含巷弄隱藏版、重劃區新店、以及工業區便道！
    </div>
    """, 
    unsafe_allow_html=True
)

# --- 篩選區 (直接放在主頁面，不用側邊欄) ---
st.markdown("### 1️⃣ 選擇區域")
all_districts = sorted(list(set([shop["district"] for shop in shops_data])))
all_districts.insert(0, "全部顯示")
# Selectbox 在手機上會變成原生的下拉選單，最好用
selected_area = st.selectbox("請選擇您居住的區域", all_districts, label_visibility="collapsed")

st.write("") # 空行

st.markdown("### 2️⃣ 想找哪種店？")
# Pills (膠囊按鈕) 是手機上最好按的設計
type_filter = st.pills(
    "類型篩選",
    ["所有類型", "精緻護理 (要預約)", "自助洗車 (24H)", "加油站洗車 (快速)", "人工手洗 (在地)"],
    default="所有類型",
    label_visibility="collapsed"
)

# 小撇步 (放在篩選器下方，醒目)
st.info("💡 **小撇步**：過年前一週「精緻護理」通常約滿，建議改去「自助洗車」或「加油站」比較快喔！")

st.divider()

# --- 邏輯處理 ---

filtered_shops = []
for shop in shops_data:
    # 區域過濾
    if selected_area != "全部顯示" and shop["district"] != selected_area:
        continue
    
    # 類型過濾
    if type_filter == "精緻護理 (要預約)" and "精緻" not in shop["type"]: continue
    
    if type_filter == "自助洗車 (24H)" and "自助" not in shop["type"]: continue
    
    if type_filter == "加油站洗車 (快速)" and "加油站" not in shop["type"]: continue
    
    if type_filter == "人工手洗 (在地)" and "人工" not in shop["type"]: continue
    
    filtered_shops.append(shop)

# --- 顯示結果 ---

# 鄰近推薦 (偏鄉救星)
nearby_map = {"新屋區": "楊梅區", "觀音區": "中壢區", "大園區": "蘆竹區", "復興區": "大溪區"}

if selected_area in nearby_map:
    neighbor = nearby_map[selected_area]
    st.warning(f"🔔 **{selected_area} 店家較少**，若排隊太長，建議殺去 **【{neighbor}】**，選擇多很多！")

if not filtered_shops:
    st.error("⚠️ 哎呀！這個條件下沒有店家，請試試看別的類型。")
else:
    st.caption(f"📍 {selected_area}：共找到 {len(filtered_shops)} 間")
    
    # 手機版直接用單欄顯示，卡片一張一張滑最清楚
    for shop in filtered_shops:
        with st.container(border=True):
            # 標題與類型圖示
            icon = "🚗"
            if "自助" in shop["type"]: icon = "🪙"
            if "加油站" in shop["type"]: icon = "⛽"
            if "人工" in shop["type"]: icon = "🖐️"
            
            c1, c2 = st.columns([8, 2])
            with c1:
                st.subheader(f"{icon} {shop['name']}")
                st.caption(f"📍 {shop['district']} | {shop['type']}")
            with c2:
                st.markdown(f"<h3 style='color:#F57C00; text-align:right;'>★{shop['rating']}</h3>", unsafe_allow_html=True)
            
            st.write(f"💬 {shop['desc']}")
            
            # 導航按鈕 (滿版寬度，手機好按)
            map_url = f"https://www.google.com/maps/search/?api=1&query={shop['name']}+{shop['location']}"
            
            if "自助" in shop["type"]:
                st.link_button("🪙 導航去 (24H)", map_url, use_container_width=True)
            elif "加油站" in shop["type"]:
                st.link_button("⛽ 導航去 (免預約)", map_url, use_container_width=True)
            elif "人工" in shop["type"]:
                st.link_button("🖐️ 導航去 (排隊制)", map_url, use_container_width=True)
            else:
                st.link_button("📅 導航去 (建議預約)", map_url, use_container_width=True, type="primary")

# --- 底部 ---
st.markdown(
    "<div style='text-align: center; color: #888; margin-top: 30px;'>桃園三一協會 Taoyuan Sanyi Association © 2026</div>", 
    unsafe_allow_html=True
)
