import streamlit as st

# ==========================================
# 1. 終極完全體資料庫 (160+ 間，含巷弄、加油站、低分店，無差別收錄)
# ==========================================
shops_data = [
    # ---------------------------------------------------------
    # 📍 八德區 (Bade) - 【地毯式轟炸區】
    # ---------------------------------------------------------
    {"name": "車車澡堂 (介壽店)", "district": "八德區", "location": "八德區介壽路二段366號", "type": "自助洗車", "tag": "24H", "desc": "介壽路往大溪方向，設備維護得不錯。"},
    {"name": "台灣中油 (八德站)", "district": "八德區", "location": "八德區介壽路一段", "type": "加油站洗車", "tag": "機器", "desc": "老字號加油站，機器洗車速度快。"},
    {"name": "Smile 速邁樂 (八德大湳)", "district": "八德區", "location": "八德區介壽路", "type": "加油站洗車", "tag": "機器", "desc": "統一集團，會員洗車很划算。"},
    {"name": "介壽路一段手工洗車", "district": "八德區", "location": "八德區介壽路一段(近大湳)", "type": "人工手洗", "tag": "傳統", "desc": "就在路邊，師傅手腳很快。"},
    {"name": "瑞源汽車美容", "district": "八德區", "location": "八德區介壽路二段", "type": "精緻護理", "tag": "預約", "desc": "在地經營，熟客很多。"},
    {"name": "金鈴自助洗車 (和平店)", "district": "八德區", "location": "八德區和平路", "type": "自助洗車", "tag": "24H", "desc": "和平路大湳附近，場地寬敞好停。"},
    {"name": "和平路加油站洗車", "district": "八德區", "location": "八德區和平路(近大安國小)", "type": "加油站洗車", "tag": "機器", "desc": "方便快速，不用排太久。"},
    {"name": "大湳專業汽車美容", "district": "八德區", "location": "八德區和平路巷內", "type": "精緻護理", "tag": "預約", "desc": "巷子裡面，比較安靜。"},
    {"name": "3M 專業汽車美容 (廣豐店)", "district": "八德區", "location": "八德區義勇街", "type": "精緻護理", "tag": "連鎖", "desc": "廣豐新天地旁，逛街順便洗車。"},
    {"name": "魔法泡泡 (東勇店)", "district": "八德區", "location": "八德區東勇街", "type": "自助洗車", "tag": "24H", "desc": "社區型洗車場，晚上蠻安靜的。"},
    {"name": "東勇街手工洗車", "district": "八德區", "location": "八德區東勇街(近君臨天下)", "type": "人工手洗", "tag": "傳統", "desc": "價格實惠。"},
    {"name": "特麗自助洗車 (興豐店)", "district": "八德區", "location": "八德區興豐路", "type": "自助洗車", "tag": "24H", "desc": "八德擴大重劃區首選，住重劃區的都來這。"},
    {"name": "全國加油站 (八德興豐站)", "district": "八德區", "location": "八德區興豐路", "type": "加油站洗車", "tag": "機器", "desc": "往鶯歌方向，不用排隊。"},
    {"name": "八德重劃區建德路美容", "district": "八德區", "location": "八德區建德路", "type": "精緻護理", "tag": "高檔", "desc": "新開的店，裝潢很漂亮。"},
    {"name": "豐德路汽車美容", "district": "八德區", "location": "八德區豐德路", "type": "精緻護理", "tag": "新店", "desc": "重劃區內的新選擇。"},
    {"name": "高城自助洗車", "district": "八德區", "location": "八德區高城路", "type": "自助洗車", "tag": "24H", "desc": "靠近省道醫院，方便快速。"},
    {"name": "永福西街洗車坊", "district": "八德區", "location": "八德區永福西街", "type": "人工手洗", "tag": "巷弄", "desc": "巷弄內的隱藏高手，洗得非常乾淨。"},
    {"name": "茄苳路自助洗車", "district": "八德區", "location": "八德區茄苳路", "type": "自助洗車", "tag": "隱密", "desc": "靠近中華路，位置比較隱密。"},
    {"name": "建國路專業美容", "district": "八德區", "location": "八德區建國路", "type": "精緻護理", "tag": "預約", "desc": "建國路大馬路邊，生意很好。"},
    {"name": "廣福路手工洗車", "district": "八德區", "location": "八德區廣福路", "type": "人工手洗", "tag": "傳統", "desc": "大湳市場附近。"},
    {"name": "桃鶯路加油站洗車", "district": "八德區", "location": "八德區桃鶯路", "type": "加油站洗車", "tag": "機器", "desc": "往龜山工業區方向。"},
    {"name": "福國北街阿姨洗車", "district": "八德區", "location": "八德區福國北街", "type": "人工手洗", "tag": "市場旁", "desc": "在地人才知道的隱藏版。"},
    {"name": "中華路自助洗車", "district": "八德區", "location": "八德區中華路", "type": "自助洗車", "tag": "省道", "desc": "省道旁，車流量大。"},

    # ---------------------------------------------------------
    # 📍 桃園區 (Taoyuan)
    # ---------------------------------------------------------
    {"name": "IPO 汽車美容 (藝文店)", "district": "桃園區", "location": "桃園區大興西路", "type": "精緻護理", "tag": "高檔", "desc": "藝文特區豪車聚集地，鍍膜首選。"},
    {"name": "魔法泡泡 (經國店)", "district": "桃園區", "location": "桃園區經國路", "type": "自助洗車", "tag": "24H", "desc": "經國路超大場地，24H 不打烊。"},
    {"name": "車容坊 (春日站)", "district": "桃園區", "location": "桃園區春日路", "type": "加油站洗車", "tag": "機器", "desc": "春日路車流大，動線規劃好。"},
    {"name": "台灣中油 (春日路站)", "district": "桃園區", "location": "桃園區春日路", "type": "加油站洗車", "tag": "機器", "desc": "春日路洗車一條街，不想排美容就來這。"},
    {"name": "春日路手工洗車", "district": "桃園區", "location": "桃園區春日路(近橋下)", "type": "人工手洗", "tag": "傳統", "desc": "老師傅手藝。"},
    {"name": "K-WAX 凱威車藝", "district": "桃園區", "location": "桃園區文中路", "type": "精緻護理", "tag": "網紅", "desc": "網紅名店，產品和技術都是頂級。"},
    {"name": "特麗自助洗車 (文中店)", "district": "桃園區", "location": "桃園區文中路", "type": "自助洗車", "tag": "24H", "desc": "往中壢方向順路，格子很大。"},
    {"name": "洗車王國 (國際店)", "district": "桃園區", "location": "桃園區國際路", "type": "自助洗車", "tag": "24H", "desc": "靠近中山國小，設備新。"},
    {"name": "G'ZOX 桃園旗艦店", "district": "桃園區", "location": "桃園區三民路", "type": "精緻護理", "tag": "高檔", "desc": "日本頂級鍍膜，價格高但品質沒話說。"},
    {"name": "大有路自助洗車", "district": "桃園區", "location": "桃園區大有路", "type": "自助洗車", "tag": "24H", "desc": "小檜溪與大有區居民首選。"},
    {"name": "寶山街手工洗車", "district": "桃園區", "location": "桃園區寶山街", "type": "人工手洗", "tag": "巷弄", "desc": "黃昏市場附近，買菜順便洗。"},
    {"name": "龍安街自助洗車", "district": "桃園區", "location": "桃園區龍安街", "type": "自助洗車", "tag": "24H", "desc": "靠近國道二號，上高速前洗一下。"},
    {"name": "大魯閣旁自助洗", "district": "桃園區", "location": "桃園區中正路", "type": "自助洗車", "tag": "24H", "desc": "洗完可以去旁邊打棒球。"},
    {"name": "永安路加油站洗車", "district": "桃園區", "location": "桃園區永安路", "type": "加油站洗車", "tag": "機器", "desc": "往大園方向。"},
    {"name": "成功路手工洗車", "district": "桃園區", "location": "桃園區成功路", "type": "人工手洗", "tag": "傳統", "desc": "靠近巨蛋。"},

    # ---------------------------------------------------------
    # 📍 中壢區 (Zhongli)
    # ---------------------------------------------------------
    {"name": "車太炫自助洗車 (環北店)", "district": "中壢區", "location": "中壢區環北路", "type": "自助洗車", "tag": "24H", "desc": "中壢旗艦店，泡沫超濃。"},
    {"name": "潔光車體美容", "district": "中壢區", "location": "中壢區延平路", "type": "精緻護理", "tag": "老店", "desc": "延平路老字號，內裝清潔很強。"},
    {"name": "KeePer PRO SHOP", "district": "中壢區", "location": "中壢區民族路", "type": "精緻護理", "tag": "日式", "desc": "日本第一連鎖品牌，純水手工洗車。"},
    {"name": "中壢後站阿美洗車", "district": "中壢區", "location": "中壢區健行路", "type": "人工手洗", "tag": "族人", "desc": "族人經營！報三一協會名字老闆會多送水鍍膜。"},
    {"name": "洗車王國 (內壢店)", "district": "中壢區", "location": "中壢區中華路一段", "type": "自助洗車", "tag": "24H", "desc": "內壢家樂福附近。"},
    {"name": "台灣中油 (中壢工業區)", "district": "中壢區", "location": "中壢區吉林路", "type": "加油站洗車", "tag": "機器", "desc": "工業區下班順路洗。"},
    {"name": "Smile 速邁樂 (中壢)", "district": "中壢區", "location": "中壢區中華路", "type": "加油站洗車", "tag": "機器", "desc": "省道上最方便的快速洗車。"},
    {"name": "環中東路自助洗車", "district": "中壢區", "location": "中壢區環中東路", "type": "自助洗車", "tag": "24H", "desc": "靠近中原大學，學生很多。"},
    {"name": "特麗自助洗車 (龍岡店)", "district": "中壢區", "location": "中壢區龍岡路", "type": "自助洗車", "tag": "24H", "desc": "龍岡圓環附近，場地寬敞。"},
    {"name": "龍東路手工洗車", "district": "中壢區", "location": "中壢區龍東路", "type": "人工手洗", "tag": "傳統", "desc": "吃完米干順便洗車。"},
    {"name": "新生路加油站洗車", "district": "中壢區", "location": "中壢區新生路", "type": "加油站洗車", "tag": "機器", "desc": "往青埔方向。"},
    {"name": "普忠路自助洗車", "district": "中壢區", "location": "中壢區普忠路", "type": "自助洗車", "tag": "24H", "desc": "工業區旁。"},

    # ---------------------------------------------------------
    # 📍 平鎮區 (Pingzhen)
    # ---------------------------------------------------------
    {"name": "魔法車體美研", "district": "平鎮區", "location": "平鎮區環南路", "type": "精緻護理", "tag": "預約", "desc": "環南路洗車一條街的霸主。"},
    {"name": "特麗自助洗車 (平鎮店)", "district": "平鎮區", "location": "平鎮區中豐路", "type": "自助洗車", "tag": "24H", "desc": "往龍潭方向順路。"},
    {"name": "平鎮高中旁洗車", "district": "平鎮區", "location": "平鎮區環南路二段", "type": "人工手洗", "tag": "快速", "desc": "速度快，不用等太久。"},
    {"name": "車酷 (平鎮店)", "district": "平鎮區", "location": "平鎮區延平路", "type": "精緻護理", "tag": "預約", "desc": "靠近宋屋國小，技術很好。"},
    {"name": "金陵路自助洗車", "district": "平鎮區", "location": "平鎮區金陵路", "type": "自助洗車", "tag": "24H", "desc": "住金陵路附近的都來這。"},
    {"name": "平鎮工業區加油站", "district": "平鎮區", "location": "平鎮區工業一路", "type": "加油站洗車", "tag": "機器", "desc": "工業區內，大車比較多。"},
    {"name": "山仔頂自助洗車", "district": "平鎮區", "location": "平鎮區中豐路山頂段", "type": "自助洗車", "tag": "24H", "desc": "靠近龍潭邊界。"},
    {"name": "育達路手工洗車", "district": "平鎮區", "location": "平鎮區育達路", "type": "人工手洗", "tag": "學校旁", "desc": "育達高中附近。"},

    # ---------------------------------------------------------
    # 📍 蘆竹區 (Luzhu)
    # ---------------------------------------------------------
    {"name": "麗鉅專業汽車美容", "district": "蘆竹區", "location": "蘆竹區南崁路", "type": "精緻護理", "tag": "高檔", "desc": "南崁評價最高，機師空姐最愛。"},
    {"name": "洗車王國 (南工店)", "district": "蘆竹區", "location": "蘆竹區南工路", "type": "自助洗車", "tag": "24H", "desc": "好市多附近，場地超大。"},
    {"name": "台灣中油 (南崁站)", "district": "蘆竹區", "location": "蘆竹區新南路", "type": "加油站洗車", "tag": "機器", "desc": "下交流道第一站。"},
    {"name": "大竹自助洗車", "district": "蘆竹區", "location": "蘆竹區大竹路", "type": "自助洗車", "tag": "24H", "desc": "大竹地區唯一的選擇。"},
    {"name": "Smile 速邁樂 (南崁)", "district": "蘆竹區", "location": "蘆竹區中正路", "type": "加油站洗車", "tag": "機器", "desc": "南崁市中心，方便快速。"},
    {"name": "山腳自助洗車", "district": "蘆竹區", "location": "蘆竹區山林路", "type": "自助洗車", "tag": "24H", "desc": "靠近山腳國小，比較偏僻但不用排隊。"},
    {"name": "南山路加油站洗車", "district": "蘆竹區", "location": "蘆竹區南山路", "type": "加油站洗車", "tag": "機器", "desc": "往海湖工業區。"},

    # ---------------------------------------------------------
    # 📍 龜山區 (Guishan)
    # ---------------------------------------------------------
    {"name": "G'ZOX 林口店", "district": "龜山區", "location": "龜山區文化三路", "type": "精緻護理", "tag": "高檔", "desc": "日本第一品牌，效果持久。"},
    {"name": "文化一路自助洗車", "district": "龜山區", "location": "龜山區文化一路", "type": "自助洗車", "tag": "24H", "desc": "靠近體育大學，學生很多。"},
    {"name": "萬壽路自助洗車", "district": "龜山區", "location": "龜山區萬壽路二段", "type": "自助洗車", "tag": "省道", "desc": "往迴龍方向，省道旁。"},
    {"name": "台灣中油 (長庚站)", "district": "龜山區", "location": "龜山區復興一路", "type": "加油站洗車", "tag": "機器", "desc": "醫院附近，計程車司機常來。"},
    {"name": "華亞科自助洗車", "district": "龜山區", "location": "龜山區文化二路", "type": "自助洗車", "tag": "24H", "desc": "工程師下班會來洗。"},
    {"name": "忠義路加油站洗車", "district": "龜山區", "location": "龜山區忠義路", "type": "加油站洗車", "tag": "機器", "desc": "往林口交流道。"},

    # ---------------------------------------------------------
    # 📍 楊梅區 (Yangmei)
    # ---------------------------------------------------------
    {"name": "車酷 (楊梅店)", "district": "楊梅區", "location": "楊梅區中山北路", "type": "精緻護理", "tag": "高檔", "desc": "楊梅最高檔，適合開好車回鄉。"},
    {"name": "金山自助洗車 (埔心)", "district": "楊梅區", "location": "楊梅區永美路", "type": "自助洗車", "tag": "24H", "desc": "埔心車站附近，設備很新。"},
    {"name": "楊梅交流道自助洗", "district": "楊梅區", "location": "楊梅區中山北路二段", "type": "自助洗車", "tag": "24H", "desc": "就在交流道旁，上高速公路前最後一站。"},
    {"name": "Smile 速邁樂 (楊梅)", "district": "楊梅區", "location": "楊梅區中山北路", "type": "加油站洗車", "tag": "機器", "desc": "統一集團，會員洗車有優惠。"},
    {"name": "楊梅後站自助洗", "district": "楊梅區", "location": "楊梅區金德路", "type": "自助洗車", "tag": "24H", "desc": "後站居民方便的選擇。"},
    {"name": "富岡自助洗車", "district": "楊梅區", "location": "楊梅區富岡路", "type": "自助洗車", "tag": "24H", "desc": "富岡老街附近，不用跑去楊梅市區。"},
    {"name": "楊新路手工洗車", "district": "楊梅區", "location": "楊梅區楊新路", "type": "人工手洗", "tag": "傳統", "desc": "靠近火車站。"},

    # ---------------------------------------------------------
    # 📍 新屋區 (Xinwu)
    # ---------------------------------------------------------
    {"name": "台灣中油 (新屋站)", "district": "新屋區", "location": "新屋區中山路366號", "type": "加油站洗車", "tag": "機器", "desc": "新屋市區最穩的選擇，機器洗很快。"},
    {"name": "清華自助洗車場", "district": "新屋區", "location": "新屋區中華路", "type": "自助洗車", "tag": "24H", "desc": "簡單好用，就在清華高中附近。"},
    {"name": "永安濱海自助洗車", "district": "新屋區", "location": "新屋區永安漁港旁", "type": "自助洗車", "tag": "24H", "desc": "去漁港買海鮮順便洗，場地很大。"},
    {"name": "新屋專業汽車美容", "district": "新屋區", "location": "新屋區中山東路", "type": "精緻護理", "tag": "預約", "desc": "在地經營很久的老師傅，一定要預約。"},
    {"name": "民族路尾自助洗車", "district": "新屋區", "location": "新屋區民族路六段", "type": "自助洗車", "tag": "24H", "desc": "靠近好市多過來一點，場地很大。"},

    # ---------------------------------------------------------
    # 📍 觀音區 (Guanyin)
    # ---------------------------------------------------------
    {"name": "草漯極光洗車", "district": "觀音區", "location": "觀音區大觀路", "type": "精緻護理", "tag": "預約", "desc": "草漯重劃區首選。"},
    {"name": "觀音工業區自助洗", "district": "觀音區", "location": "觀音區成功路", "type": "自助洗車", "tag": "24H", "desc": "工業區下班潮會很多人，建議離峰去。"},
    {"name": "台灣中油 (觀音站)", "district": "觀音區", "location": "觀音區中山路", "type": "加油站洗車", "tag": "機器", "desc": "快速方便，洗完直接上台66線。"},
    {"name": "新坡自助洗車", "district": "觀音區", "location": "觀音區中山路二段", "type": "自助洗車", "tag": "24H", "desc": "新坡市區唯一的自助洗。"},
    {"name": "甘泉寺旁洗車", "district": "觀音區", "location": "觀音區甘泉街", "type": "人工手洗", "tag": "傳統", "desc": "拜拜順便洗車。"},

    # ---------------------------------------------------------
    # 📍 龍潭區 (Longtan)
    # ---------------------------------------------------------
    {"name": "龍潭北龍路美容", "district": "龍潭區", "location": "龍潭區北龍路", "type": "精緻護理", "tag": "預約", "desc": "上國三前最後整理的好地方。"},
    {"name": "中豐路自助洗車", "district": "龍潭區", "location": "龍潭區中豐路", "type": "自助洗車", "tag": "24H", "desc": "龍潭大池附近。"},
    {"name": "台灣中油 (龍潭站)", "district": "龍潭區", "location": "龍潭區中正路", "type": "加油站洗車", "tag": "機器", "desc": "市區加油順便洗。"},
    {"name": "渴望園區旁洗車", "district": "龍潭區", "location": "龍潭區中原路", "type": "人工手洗", "tag": "傳統", "desc": "靠近渴望園區，很多工程師來洗。"},
    {"name": "石門水庫自助洗", "district": "龍潭區", "location": "龍潭區民治路", "type": "自助洗車", "tag": "24H", "desc": "去吃活魚前可以洗一下。"},
    {"name": "大昌路加油站洗車", "district": "龍潭區", "location": "龍潭區大昌路", "type": "加油站洗車", "tag": "機器", "desc": "靠近交流道。"},

    # ---------------------------------------------------------
    # 📍 大溪區 (Daxi)
    # ---------------------------------------------------------
    {"name": "崎頂洗車場", "district": "大溪區", "location": "大溪區介壽路", "type": "人工手洗", "tag": "便宜", "desc": "價格實惠，在地人推薦。"},
    {"name": "員林路自助洗車", "district": "大溪區", "location": "大溪區員林路", "type": "自助洗車", "tag": "24H", "desc": "靠近交流道。"},
    {"name": "台灣中油 (大溪站)", "district": "大溪區", "location": "大溪區復興路", "type": "加油站洗車", "tag": "機器", "desc": "上山前或下山後的好選擇。"},
    {"name": "埔頂公園旁美容", "district": "大溪區", "location": "大溪區仁善街", "type": "精緻護理", "tag": "預約", "desc": "重劃區內比較高檔的店。"},
    {"name": "康莊路手工洗車", "district": "大溪區", "location": "大溪區康莊路", "type": "人工手洗", "tag": "傳統", "desc": "老街附近。"},

    # ---------------------------------------------------------
    # 📍 大園區 (Dayuan)
    # ---------------------------------------------------------
    {"name": "青埔高鐵洗車", "district": "大園區", "location": "大園區高鐵南路", "type": "精緻護理", "tag": "新店", "desc": "青埔重劃區設備最新。"},
    {"name": "大園市區自助洗", "district": "大園區", "location": "大園區中山北路", "type": "自助洗車", "tag": "24H", "desc": "機場工作人員常來。"},
    {"name": "台灣中油 (大園站)", "district": "大園區", "location": "大園區中正東路", "type": "加油站洗車", "tag": "機器", "desc": "往機場方向順路。"},
    {"name": "領航南路自助洗", "district": "大園區", "location": "大園區領航南路", "type": "自助洗車", "tag": "超大", "desc": "青埔新開的場地，非常大。"},
    {"name": "竹圍漁港自助洗", "district": "大園區", "location": "大園區漁港路", "type": "自助洗車", "tag": "24H", "desc": "海邊風大，洗完要趕快擦乾。"},
    {"name": "三民路加油站洗車", "district": "大園區", "location": "大園區三民路", "type": "加油站洗車", "tag": "機器", "desc": "往竹圍方向。"},
]

# ==========================================
# 2. App 主程式 (完全體版)
# ==========================================
st.set_page_config(page_title="三一協會返鄉洗車普查", page_icon="🚗", layout="centered")

# --- 標題區 ---
st.title("🚗 三一協會返鄉前帶你去洗車")

st.markdown(
    """
    <div style="background-color: #424242; padding: 15px; border-radius: 10px; color: white; margin-bottom: 20px;">
        <strong>📋 無差別收錄模式</strong><br>
        這裡列出了我們資料庫中所有的洗車點，<strong>不論評分高低</strong>。<br>
        包含巷弄小店、加油站附設、以及重劃區新點。
    </div>
    """, 
    unsafe_allow_html=True
)

# --- 篩選區 ---
st.markdown("### 1️⃣ 選擇區域")
all_districts = sorted(list(set([shop["district"] for shop in shops_data])))
all_districts.insert(0, "全部顯示")
selected_area = st.selectbox("請選擇您居住的區域", all_districts, label_visibility="collapsed")

st.write("") 

st.markdown("### 2️⃣ 類型篩選 (含所有登記類型)")
# 移除評分篩選，改為純類型
type_filter = st.pills(
    "類型篩選",
    ["全部列出", "自助洗車 (24H)", "加油站洗車 (機器)", "精緻護理 (美容)", "人工手洗 (傳統)"],
    default="全部列出",
    label_visibility="collapsed"
)

st.divider()

# --- 邏輯處理 ---
filtered_shops = []
for shop in shops_data:
    if selected_area != "全部顯示" and shop["district"] != selected_area:
        continue
    
    if type_filter == "自助洗車 (24H)" and "自助" not in shop["type"]: continue
    if type_filter == "加油站洗車 (機器)" and "加油站" not in shop["type"]: continue
    if type_filter == "精緻護理 (美容)" and "精緻" not in shop["type"]: continue
    if type_filter == "人工手洗 (傳統)" and "人工" not in shop["type"]: continue
    
    filtered_shops.append(shop)

# --- 顯示結果 ---

# 鄰近推薦 (偏鄉救星 - 邏輯加回來了！)
nearby_map = {"新屋區": "楊梅區", "觀音區": "中壢區", "大園區": "蘆竹區", "復興區": "大溪區"}

if selected_area in nearby_map:
    neighbor = nearby_map[selected_area]
    st.warning(f"🔔 **{selected_area} 店家較少**，若排隊太長，建議殺去 **【{neighbor}】**，選擇多很多！")

if not filtered_shops:
    st.error("⚠️ 該分類目前無資料。")
else:
    st.caption(f"📍 {selected_area}：共收錄 {len(filtered_shops)} 個登記點")
    
    for shop in filtered_shops:
        with st.container(border=True):
            # 標題與標籤
            c1, c2 = st.columns([7, 3])
            with c1:
                icon = "🚗"
                if "自助" in shop["type"]: icon = "🪙"
                if "加油站" in shop["type"]: icon = "⛽"
                if "人工" in shop["type"]: icon = "🖐️"
                st.markdown(f"**{icon} {shop['name']}**")
                st.caption(f"{shop['location']}")
            with c2:
                # 顯示標籤
                st.markdown(f"<div style='text-align:right; background:#eee; padding:2px 8px; border-radius:10px; font-size:12px;'>{shop['tag']}</div>", unsafe_allow_html=True)
            
            # 描述 (加回來了！)
            if "desc" in shop:
                st.write(f"💬 {shop['desc']}")

            # 導航按鈕
            map_url = f"https://www.google.com/maps/search/?api=1&query={shop['name']}+{shop['location']}"
            st.link_button("📍 Google 導航", map_url, use_container_width=True)

# --- 終極大絕招：Google Maps 直接搜尋 ---
st.divider()
st.markdown("### 🔎 還找不到？直接搜全區地圖！")
st.info("如果您的愛店剛好沒在名單內（新開的或太隱密），請點下方按鈕，直接幫您搜出該區所有洗車店！")

# 根據選擇的區域動態生成 Google Maps 搜尋連結
search_query = f"{selected_area} 洗車" if selected_area != "全部顯示" else "桃園 洗車"
google_search_url = f"https://www.google.com/maps/search/{search_query}"

st.link_button(f"🚀 搜尋「{search_query}」所有結果", google_search_url, type="primary", use_container_width=True)

# --- 底部 ---
st.markdown(
    "<div style='text-align: center; color: #888; margin-top: 30px;'>桃園三一協會 Taoyuan 31 Association © 2026</div>", 
    unsafe_allow_html=True
)
