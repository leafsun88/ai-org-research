#!/usr/bin/env python3
"""Step 1: 从276家公司中筛选港美股 + 市值≥$5B"""

import re

# 完整276家公司数据 (ticker -> (name, exchange, mcap, lists, sector, note))
DATA = {
    # ===== Meta-like =====
    "GOOGL": ("Alphabet (Google/YouTube)", "NASDAQ", "$3.5T", "mn", "大型科技平台", "广告+云+AI芯片(TPU)三位一体"),
    "SNAP": ("Snap", "NYSE", "$18B", "m", "社交媒体", "Snapchat直接社交竞品，年轻用户+AR+广告变现"),
    "PINS": ("Pinterest", "NYSE", "$15B", "m", "社交/发现", "视觉发现平台，购买意图数据强"),
    "RDDT": ("Reddit", "NYSE", "$18B", "m", "社交/社区", "社区聚合+广告高速增长"),
    "NXDR": ("Nextdoor", "NYSE", "$1B", "m", "社交/本地", "邻里本地社交"),
    "0700.HK": ("Tencent (腾讯)", "HKEX", "$500B+", "m", "大型科技平台", "WeChat=中国Meta，营销服务广告超千亿"),
    "WB": ("Weibo (微博)", "NASDAQ", "$2B", "m", "社交媒体", "中国微博，社交内容广告变现"),
    "BILI": ("Bilibili", "NASDAQ", "$8B", "m", "社交/视频", "中国Z世代视频社区"),
    "1024.HK": ("Kuaishou (快手)", "HKEX", "$50B", "m", "短视频", "中国短视频第二，AI推荐驱动广告"),
    "035420.KS": ("NAVER", "KOSPI", "$25B", "m", "搜索/内容", "韩国搜索+内容+社交生态"),
    "035720.KS": ("Kakao", "KOSPI", "$15B", "m", "IM/超级App", "韩国国民级IM"),
    "4689.T": ("LY Corporation", "TSE", "$10B", "m", "社交/门户", "LINE+Yahoo Japan合并"),
    "4751.T": ("CyberAgent", "TSE", "$3B", "m", "互联网/广告", "日本内容广告平台"),
    "2121.T": ("MIXI", "TSE", "$1B", "m", "社交/游戏", "日本社交先驱"),
    "SE": ("Sea Limited", "NYSE", "$50B", "ms", "超级平台", "Shopee电商+Garena游戏+SeaMoney"),
    "GRAB": ("Grab Holdings", "NASDAQ", "$15B", "ms", "超级App", "东南亚超级App"),
    "GOTO.JK": ("GoTo Group", "IDX", "$3B", "ms", "超级App", "印尼超级App"),
    "PRX": ("Prosus / Naspers", "Amsterdam", "$80B", "m", "互联网投资控股", "持有Tencent+全球社交投资"),
    "ETERNAL": ("Eternal (前Zomato)", "NSE", "$12B", "m", "本地生活", "印度本地生活超级平台"),
    "3690.HK": ("Meituan (美团)", "HKEX", "$100B", "m", "本地生活", "中国本地生活超级平台"),
    "APP": ("AppLovin", "NASDAQ", "$130B", "m", "AdTech", "AXON AI广告引擎"),
    "TTD": ("The Trade Desk", "NASDAQ", "$18B", "m", "AdTech/DSP", "最大独立DSP"),
    "CRTO": ("Criteo", "NASDAQ", "$1.7B", "m", "AdTech", "商业媒体平台"),
    "MGNI": ("Magnite", "NASDAQ", "$1.5B", "m", "AdTech/SSP", "最大独立SSP"),
    "PUBM": ("PubMatic", "NASDAQ", "$0.6B", "m", "AdTech/SSP", "独立SSP"),
    "DV": ("DoubleVerify", "NYSE", "$1.5B", "m", "AdTech", "AI广告验证"),
    "IAS": ("Integral Ad Science", "NASDAQ", "$1.5B", "m", "AdTech", "广告验证+品牌安全"),
    "TBLA": ("Taboola", "NASDAQ", "$1B", "ms", "AdTech", "AI内容推荐+原生广告"),
    "OB": ("Outbrain", "NASDAQ", "$0.5B", "m", "AdTech", "内容发现+原生广告"),
    "PERI": ("Perion Network", "NASDAQ", "$0.3B", "m", "AdTech", "全渠道AdTech"),
    "TRMR": ("Tremor International", "NASDAQ", "$0.5B", "m", "AdTech", "端到端CTV广告"),
    "RAMP": ("LiveRamp", "NYSE", "$2B", "m", "数据协作", "隐私安全的用户数据连接"),
    "CDLX": ("Cardlytics", "NASDAQ", "$0.3B", "m", "AdTech", "银行消费数据+广告"),
    "APPS": ("Digital Turbine", "NASDAQ", "$0.3B", "ms", "AdTech/移动", "移动App预装+广告"),
    "U": ("Unity Software", "NYSE", "$7B", "m", "游戏引擎/AdTech", "游戏引擎+IronSource广告"),
    "4324.T": ("Dentsu Group", "TSE", "$8B", "m", "广告集团", "全球第五大广告集团"),
    "IZEA": ("IZEA Worldwide", "NASDAQ", "小市值", "m", "影响者营销", "AI网红营销平台"),
    "CXM": ("Sprinklr", "NYSE", "$2B", "ms", "CXM/SaaS", "统一客户体验管理"),
    "BIDU": ("Baidu (百度)", "NASDAQ", "$30B", "m", "搜索/AI", "中国最大搜索广告"),
    "PDD": ("PDD Holdings (拼多多)", "NASDAQ", "$140B", "m", "电商/社交电商", "拼多多社交电商"),
    "YELP": ("Yelp", "NYSE", "$2B", "m", "本地发现", "本地发现+广告"),
    "NAUKRI": ("Info Edge (Naukri)", "NSE", "$7B", "m", "招聘/分类", "印度最大招聘平台"),
    "MELI": ("MercadoLibre", "NASDAQ", "$100B", "ms", "电商/FinTech", "拉美电商+支付+广告+物流超级平台"),
    "CART": ("Maplebear (Instacart)", "NASDAQ", "$8B", "m", "零售媒体", "零售媒体+购物数据广告"),
    "JD": ("JD.com (京东)", "NASDAQ", "$50B", "m", "电商", "中国直销电商广告"),
    "BABA": ("Alibaba (阿里巴巴)", "NYSE", "$300B", "ms", "电商/云", "阿里妈妈最大电商广告"),
    "SPOT": ("Spotify", "NYSE", "$100B", "m", "流媒体/音频", "音频流媒体+AI广告+播客生态"),
    "NFLX": ("Netflix", "NASDAQ", "$400B", "m", "流媒体", "流媒体AVOD广告+全球最大内容飞轮"),
    "ROKU": ("Roku", "NASDAQ", "$9B", "m", "CTV", "CTV操作系统"),
    "IHRT": ("iHeartMedia", "NASDAQ", "$0.2B", "m", "广播/音频", "全美最大广播"),
    "NXST": ("Nexstar Media", "NASDAQ", "$4B", "m", "本地电视", "最大美国地方TV网络"),
    "WBD": ("Warner Bros. Discovery", "NASDAQ", "$20B", "m", "流媒体/内容", "Max流媒体广告层"),
    "PARA": ("Paramount Global", "NASDAQ", "$8B", "m", "流媒体/内容", "Paramount+广告支持层"),
    "FUBO": ("fuboTV", "NYSE", "小市值", "m", "CTV/体育", "体育向CTV流媒体"),
    "RBLX": ("Roblox", "NYSE", "$20B", "m", "游戏/元宇宙", "UGC虚拟世界平台"),
    "3659.T": ("Nexon", "TSE", "$8B", "m", "游戏", "全球最大上市游戏"),
    "259960.KS": ("Krafton", "KOSPI", "$7.5B", "m", "游戏", "PUBG全球游戏社交平台"),
    "036570.KS": ("NCSOFT", "KOSPI", "$3B", "m", "游戏", "韩国MMORPG"),
    "293490.KQ": ("Kakao Games", "KOSDAQ", "$1B", "m", "游戏", "KakaoTalk社交图谱+游戏"),
    "PLTK": ("Playtika", "NASDAQ", "$1.2B", "m", "手游", "移动休闲游戏+AI"),
    "2432.T": ("DeNA", "TSE", "$1B", "m", "社交游戏", "社交游戏Mobage"),
    "MTCH": ("Match Group", "NASDAQ", "$6B", "m", "约会", "Tinder/Hinge矩阵"),
    "BMBL": ("Bumble", "NASDAQ", "$1B", "m", "约会", "女性向约会社交"),
    "GRND": ("Grindr", "NYSE", "$3B", "m", "社群", "LGBTQ+社群"),
    "SPT": ("Sprout Social", "NASDAQ", "$1.5B", "m", "社媒管理", "社媒管理SaaS"),
    "TTWO": ("Take-Two Interactive", "NASDAQ", "$30B", "m", "游戏", "含Zynga移动游戏广告"),
    "HUBS": ("HubSpot", "NYSE", "$20B", "ms", "CRM/营销SaaS", "入站营销+CRM"),
    "CRM": ("Salesforce", "NYSE", "$250B", "ms", "CRM/SaaS", "企业CRM平台+AppExchange生态"),
    "ADBE": ("Adobe", "NASDAQ", "$160B", "m", "创意/营销云", "Experience Cloud广告分析"),
    "KVYO": ("Klaviyo", "NYSE", "$9B", "ms", "电商营销", "电商邮件+SMS营销"),
    "ZETA": ("Zeta Global", "NYSE", "$3B", "m", "营销云", "AI营销云"),
    "SEMR": ("Semrush", "NYSE", "$2B", "m", "数字营销", "数字营销分析+SEO"),
    "BRZE": ("Braze", "NASDAQ", "$4B", "ms", "客户互动", "跨渠道客户互动+AI"),
    "NTES": ("NetEase (网易)", "NASDAQ", "$30B", "m", "游戏/内容", "中国游戏+内容平台"),
    "IQ": ("iQIYI (爱奇艺)", "NASDAQ", "$1B", "m", "流媒体", "中国长视频平台"),
    "TME": ("Tencent Music (腾讯音乐)", "NYSE", "$10B", "m", "音乐/社交", "腾讯生态音乐+社交娱乐"),
    "YY": ("JOYY Group", "NASDAQ", "$1B", "m", "直播社交", "BIGO Live全球直播"),
    "BZ": ("Kanzhun (BOSS直聘)", "NASDAQ", "$5B", "m", "招聘", "中国招聘平台"),
    "TCOM": ("Trip.com", "NASDAQ", "$30B", "m", "旅游", "中国最大旅游平台"),
    "WBTN": ("Naver Webtoon", "NASDAQ", "$1B", "m", "UGC内容", "全球最大WebComic平台"),
    "DOCS": ("Doximity", "NYSE", "$4.6B", "m", "垂直社交", "医生版Meta"),
    "LAMR": ("Lamar Advertising", "NASDAQ", "$15B", "m", "OOH", "美国最大户外广告+数字DOOH"),
    "CCO": ("Clear Channel Outdoor", "NYSE", "$0.8B", "m", "OOH", "全球OOH+DOOH"),
    "DEC.PA": ("JCDecaux", "Euronext Paris", "€4B", "m", "OOH", "全球最大户外广告"),
    "OUT": ("OUTFRONT Media", "NYSE", "$2.5B", "m", "OOH", "美国OOH+DOOH"),
    "AMZN": ("Amazon", "NASDAQ", "$2T", "mn", "电商/云/广告", "AWS云+$56B广告+Trainium AI芯片"),
    "MSFT": ("Microsoft", "NASDAQ", "$3T", "mn", "大型科技平台", "LinkedIn+Azure AI云+Maia AI芯片"),
    "PLTR": ("Palantir Technologies", "NASDAQ", "$200B+", "mn", "AI平台", "AI平台(AIP+Foundry)"),
    "SNOW": ("Snowflake", "NYSE", "$60B", "msn", "数据云", "云数据平台"),
    "IPG": ("Interpublic Group", "NYSE", "$10B", "m", "广告集团", "广告集团+Acxiom数据"),
    "OMC": ("Omnicom Group", "NYSE", "$15B", "m", "广告集团", "广告集团+Omni数据"),
    "WPP.L": ("WPP", "LSE", "£10B", "m", "广告集团", "全球最大广告集团"),
    "PUB.PA": ("Publicis Groupe", "Euronext Paris", "€20B", "m", "广告集团", "Epsilon数据+CoreAI"),
    "SFOR.L": ("S4 Capital", "LSE", "£0.5B", "m", "广告集团", "全数字化广告集团"),
    "2433.T": ("Hakuhodo DY", "TSE", "$3B", "m", "广告集团", "日本第二大广告集团"),
    "PSM.DE": ("ProSiebenSat.1", "Frankfurt", "€1B", "m", "电视/广告", "德国商业电视"),
    "ITV.L": ("ITV", "LSE", "£3B", "m", "电视/广告", "英国最大商业广播"),
    "SCOR": ("ComScore", "NASDAQ", "小市值", "m", "媒体测量", "数字媒体受众测量"),
    "MFE-B.MI": ("Mediaset (MFE)", "Borsa Italiana", "€5B", "m", "电视/广告", "意大利+西班牙商业电视"),
    "M8G.F": ("MGI", "Frankfurt", "€0.5B", "m", "AdTech/游戏", "欧洲移动AdTech"),
    # ===== Shopify-like =====
    "WIX": ("Wix.com", "NASDAQ", "$5B", "s", "建站/电商SaaS", "建站+电商+支付一站式SaaS"),
    "CMRC": ("Commerce.com", "NASDAQ", "$0.4B", "s", "电商SaaS", "Shopify直接竞品"),
    "LSPD": ("Lightspeed Commerce", "NYSE", "$1B", "s", "POS/电商", "零售+餐饮POS+支付"),
    "VTEX": ("VTEX", "NYSE", "$1B", "s", "企业电商SaaS", "拉美最大企业电商SaaS"),
    "GLBE": ("Global-e Online", "NASDAQ", "$8B", "s", "跨境电商", "跨境电商基础设施"),
    "042000": ("Cafe24", "KOSDAQ", "$0.9B", "s", "DTC电商", "韩国最大DTC独立站平台"),
    "2013.HK": ("Weimob (微盟)", "HKEX", "$1.5B", "s", "电商SaaS", "中国微信生态商家SaaS"),
    "8083.HK": ("Youzan (有赞)", "HKEX", "$1B", "s", "社交电商SaaS", "中国微信商家建店"),
    "UNIECOM": ("Unicommerce", "NSE", "$0.1B", "s", "电商运营SaaS", "印度最大电商运营SaaS"),
    "3092.T": ("ZOZO", "TSE", "$10B", "s", "时尚DTC", "日本最大时尚DTC平台"),
    "NYKAA": ("Nykaa", "NSE", "$3B", "s", "美妆电商", "印度美妆垂直电商"),
    "GFG.DE": ("Global Fashion Group", "Frankfurt", "$0.1B", "s", "时尚电商", "东南亚+拉美时尚电商"),
    "TOTS3": ("TOTVS", "B3", "$5B", "s", "ERP/SaaS", "巴西最大ERP"),
    "EVCM": ("EverCommerce", "NASDAQ", "$2B", "s", "垂直SaaS", "服务型小企业垂直SaaS"),
    "TRST.L": ("Trustpilot", "LSE", "£1B", "s", "评价管理", "商家评价管理"),
    "TOST": ("Toast", "NYSE", "$15B", "s", "餐饮SaaS", "餐饮行业操作系统"),
    "TTAN": ("ServiceTitan", "NASDAQ", "$9B", "s", "垂直SaaS", "家庭服务业操作系统"),
    "PCOR": ("Procore Technologies", "NYSE", "$12B", "s", "建筑SaaS", "建筑施工操作系统"),
    "GWRE": ("Guidewire Software", "NYSE", "$20B", "s", "保险SaaS", "保险行业云核心系统"),
    "VEEV": ("Veeva Systems", "NYSE", "$35B", "s", "生命科学SaaS", "生命科学垂直SaaS"),
    "PHR": ("Phreesia", "NYSE", "$0.7B", "s", "医疗SaaS", "医疗患者接诊管理"),
    "PRVA": ("Privia Health", "NASDAQ", "$1B", "s", "医疗SaaS", "医生群体运营平台"),
    "APPF": ("AppFolio", "NASDAQ", "$8B", "s", "地产SaaS", "地产管理操作系统"),
    "BLKB": ("Blackbaud", "NASDAQ", "$4B", "s", "非营利SaaS", "非营利组织操作系统"),
    "TYL": ("Tyler Technologies", "NYSE", "$20B", "s", "政府SaaS", "地方政府全套操作系统"),
    "IOT": ("Samsara", "NYSE", "$25B", "s", "工业IoT", "工业物联网操作系统"),
    "INST": ("Instructure", "NYSE", "$4B", "s", "教育SaaS", "教育科技操作系统"),
    "YEXT": ("Yext", "NYSE", "$0.9B", "s", "商家信息管理", "商家全网信息管理"),
    "DCBO": ("Docebo", "NASDAQ", "$1B", "s", "企业学习SaaS", "企业学习管理SaaS"),
    "EVH": ("Evolent Health", "NYSE", "$2.5B", "s", "医疗技术", "健康系统技术平台"),
    "ADYEN.AS": ("Adyen", "Amsterdam", "$35B", "s", "支付", "全球商家收单"),
    "SQ": ("Block (Square)", "NYSE", "$35B", "s", "支付/SaaS", "中小商家POS+支付+贷款"),
    "XRO.AX": ("Xero", "ASX", "$20B", "s", "会计SaaS", "中小企业会计SaaS"),
    "BILL": ("BILL Holdings", "NYSE", "$6B", "s", "金融SaaS", "中小企业财务运营"),
    "INTU": ("Intuit", "NASDAQ", "$190B", "s", "金融SaaS", "QuickBooks+TurboTax"),
    "GPN": ("Global Payments", "NYSE", "$8B", "s", "支付", "全球商家收单"),
    "FI": ("Fiserv", "NASDAQ", "$70B", "s", "支付", "Clover POS+银行核心系统"),
    "PYPL": ("PayPal", "NASDAQ", "$70B", "s", "支付", "商家支付网关+BNPL"),
    "NVEI": ("Nuvei", "NASDAQ", "$5B", "s", "支付", "垂直行业商家支付"),
    "AFRM": ("Affirm", "NASDAQ", "$12B", "s", "BNPL", "为电商商家提供BNPL"),
    "FOUR": ("Shift4 Payments", "NYSE", "$8B", "s", "垂直支付", "餐饮+酒店+娱乐垂直支付"),
    "DSGX": ("Descartes Systems", "NASDAQ", "$7.5B", "s", "物流SaaS", "电商物流SaaS"),
    "DELHIVERY": ("Delhivery", "NSE", "$2.5B", "s", "物流", "印度最大物流科技"),
    "GXO": ("GXO Logistics", "NYSE", "$5B", "s", "3PL", "纯3PL科技平台"),
    "XPO": ("XPO", "NYSE", "$10B", "s", "物流", "大件配送+LTL网络"),
    "CRGO": ("Freightos", "NASDAQ", "$0.1B", "s", "货运API", "数字货运市场"),
    "MAERSK-B.CO": ("Maersk A/S", "Copenhagen", "$28B", "s", "航运/物流", "集装箱航运+电商物流"),
    "FRSH": ("Freshworks", "NASDAQ", "$3.5B", "s", "CRM SaaS", "中小企业CRM"),
    "AMPL": ("Amplitude", "NASDAQ", "$1.5B", "s", "产品分析", "产品分析"),
    "ZENV": ("Zenvia", "NASDAQ", "$0.05B", "s", "CPaaS", "巴西CPaaS"),
    "TWLO": ("Twilio", "NYSE", "$10B", "s", "CPaaS", "API优先通信平台"),
    "BAND": ("Bandwidth", "NASDAQ", "$0.7B", "s", "CPaaS", "自建运营商网络通信API"),
    "API": ("Agora", "NASDAQ", "$0.2B", "s", "RTC API", "实时音视频API"),
    "SINCH": ("Sinch AB", "Stockholm", "$1B", "s", "CPaaS", "全球CPaaS"),
    "NET": ("Cloudflare", "NYSE", "$50B", "s", "CDN/边缘云", "网络+安全+边缘计算"),
    "FSLY": ("Fastly", "NYSE", "$2B", "s", "边缘云", "边缘云CDN"),
    "OKTA": ("Okta", "NASDAQ", "$15B", "s", "身份认证", "身份认证平台"),
    "ESTC": ("Elastic NV", "NYSE", "$10B", "s", "搜索/数据", "搜索+日志+观测性平台"),
    "FROG": ("JFrog", "NASDAQ", "$3B", "s", "DevOps", "软件开发交付平台"),
    "WDAY": ("Workday", "NASDAQ", "$60B", "sn", "HR/财务SaaS", "人力+财务操作系统"),
    "SAP": ("SAP SE", "NYSE", "$250B", "s", "ERP", "全球最大ERP"),
    "ORCL": ("Oracle", "NYSE", "$350B+", "sn", "ERP/云", "ERP+NetSuite+OCI AI"),
    "SGE.L": ("Sage Group", "LSE", "£15B", "s", "中小企业SaaS", "欧洲中小企业ERP"),
    "NOW": ("ServiceNow", "NYSE", "$200B", "sn", "企业工作流", "企业工作流+Now Assist AI"),
    "VRNT": ("Verint Systems", "NASDAQ", "$2B", "s", "客服SaaS", "企业客服+合规AI"),
    "CPNG": ("Coupang", "NYSE", "$35B", "s", "电商", "韩国版Amazon"),
    "BUKA.JK": ("Bukalapak", "IDX", "$0.3B", "s", "电商", "印尼商家数字化"),
    "327.HK": ("PAX Global", "HKEX", "$1.5B", "s", "支付硬件", "全球POS终端"),
    "ANGI": ("Angi", "NASDAQ", "$0.5B", "s", "本地服务市场", "家装服务商平台"),
    "CSGP": ("CoStar Group", "NASDAQ", "$30B", "s", "商业地产数据", "商业地产数据+市场平台"),
    "WEX": ("WEX Inc.", "NYSE", "$6B", "s", "B2B支付", "B2B支付+企业支出管理"),
    "VYX": ("NCR Voyix", "NYSE", "$2B", "s", "POS", "餐饮+零售POS云平台"),
    "DOMO": ("Domo", "NASDAQ", "$0.2B", "s", "BI SaaS", "商业智能SaaS"),
    "MDB": ("MongoDB", "NASDAQ", "$20B", "s", "数据库", "开发者数据库平台"),
    "DDOG": ("Datadog", "NASDAQ", "$40B", "sn", "可观测性", "云监控+AI可观测性"),
    "LPSN": ("LivePerson", "NASDAQ", "$0.2B", "s", "对话式AI", "对话式AI商务平台"),
    "RADI": ("Radiant Logistics", "NYSE American", "$0.3B", "s", "物流", "中小企业物流管理"),
    "OLO": ("Olo", "NYSE", "$1B", "s", "餐饮SaaS", "餐饮数字点餐SaaS"),
    "FLYW": ("Flywire", "NASDAQ", "$1B", "s", "垂直支付", "教育/医疗/旅游国际支付"),
    "PAYO": ("Payoneer", "NASDAQ", "$2B", "s", "跨境支付", "跨境支付平台"),
    "DLO": ("dLocal", "NASDAQ", "$3B", "s", "跨境支付", "新兴市场支付基础设施"),
    "MQ": ("Marqeta", "NASDAQ", "$2B", "s", "卡发行API", "卡发行API平台"),
    "MNDY": ("monday.com", "NASDAQ", "$8B", "s", "工作管理SaaS", "工作操作系统"),
    "FVRR": ("Fiverr", "NYSE", "$0.4B", "s", "自由职业市场", "自由职业者marketplace"),
    "ETSY": ("Etsy", "NASDAQ", "$7B", "s", "手工电商", "手工/创意卖家平台"),
    "ABNB": ("Airbnb", "NASDAQ", "$70B", "s", "住宿平台", "住宿版Shopify"),
    "BKNG": ("Booking Holdings", "NASDAQ", "$150B", "s", "旅游平台", "全球最大旅行平台"),
    # ===== NVIDIA-like =====
    "AMD": ("Advanced Micro Devices", "NASDAQ", "$150B", "n", "AI芯片", "GPU+CPU双栈，MI300X"),
    "INTC": ("Intel", "NASDAQ", "$90B", "n", "半导体", "Gaudi AI加速器+GPU+FPGA"),
    "AVGO": ("Broadcom", "NASDAQ", "$1.6T", "n", "半导体/定制ASIC", "Google TPU共同设计"),
    "MRVL": ("Marvell Technology", "NASDAQ", "$60B", "n", "半导体", "定制ASIC+光DSP"),
    "ARM": ("Arm Holdings", "NASDAQ", "$140B", "n", "芯片IP", "AI芯片架构IP"),
    "QCOM": ("Qualcomm", "NASDAQ", "$150B", "n", "半导体", "AI200数据中心+骁龙端侧NPU"),
    "688256.SH": ("Cambricon (寒武纪)", "SSE STAR", "¥90B", "n", "AI芯片", "中国AI加速器"),
    "6082.HK": ("Biren Technology (壁仞科技)", "HKEX", "HK$100B", "n", "GPU", "中国通用GPU"),
    "688795.SH": ("Moore Threads (摩尔线程)", "SSE STAR", "¥数十B", "n", "GPU", "中国GPU"),
    "688802.SH": ("MetaX (沐曦)", "SSE STAR", "¥数十B", "n", "GPU", "中国GPU"),
    "AMBA": ("Ambarella", "NASDAQ", "$3B", "n", "边缘AI芯片", "边缘AI推理"),
    "LSCC": ("Lattice Semiconductor", "NASDAQ", "$6B", "n", "FPGA", "低功耗FPGA边缘AI"),
    "SITM": ("SiTime Corporation", "NASDAQ", "$3B", "n", "时钟IC", "AI数据中心精密时序"),
    "9660.HK": ("Horizon Robotics (地平线)", "HKEX", "HK$20B", "n", "汽车AI芯片", "中国ADAS芯片"),
    "CRBS": ("Cerebras Systems", "NASDAQ", "~$20B", "n", "AI芯片", "全晶圆AI处理器"),
    "2454.TW": ("MediaTek (联发科)", "TWSE", "$70B", "n", "Fabless", "台湾最大Fabless"),
    "MBLY": ("Mobileye", "NASDAQ", "$6B", "n", "自动驾驶", "自动驾驶AI芯片EyeQ"),
    "MPWR": ("Monolithic Power Systems", "NASDAQ", "$20B", "n", "电源IC", "AI服务器电源管理IC"),
    "VICR": ("Vicor Corporation", "NASDAQ", "$4B", "n", "电源", "超高效垂直功率传输"),
    "SIMO": ("Silicon Motion", "NASDAQ", "$1.5B", "n", "NAND控制器", "NAND闪存控制器IC"),
    "3034.TW": ("Novatek Microelectronics", "TWSE", "$10B", "n", "显示IC", "显示驱动IC"),
    "2379.TW": ("Realtek Semiconductor", "TWSE", "$8B", "n", "网络SoC", "网络/音频SoC"),
    "688008.SH": ("Montage Technology (澜起科技)", "SSE STAR", "¥17B", "n", "内存接口", "内存接口芯片"),
    "MCHP": ("Microchip Technology", "NASDAQ", "$40B", "n", "MCU/FPGA", "MCU+FPGA+SiC"),
    "TXN": ("Texas Instruments", "NASDAQ", "$175B", "n", "模拟IC", "模拟/混合信号IC巨头"),
    "NXPI": ("NXP Semiconductors", "NASDAQ", "$50B", "n", "汽车芯片", "汽车MCU/SoC全球#1"),
    "ADI": ("Analog Devices", "NASDAQ", "$90B", "n", "模拟IC", "混合信号IC+高速ADC"),
    "ASML": ("ASML Holding", "NASDAQ", "$250B", "n", "光刻机", "EUV光刻机全球唯一"),
    "AMAT": ("Applied Materials", "NASDAQ", "$120B", "n", "半导体设备", "最广谱半导体设备商"),
    "LRCX": ("Lam Research", "NASDAQ", "$90B", "n", "刻蚀设备", "刻蚀+清洗设备全球领先"),
    "KLAC": ("KLA Corporation", "NASDAQ", "$100B", "n", "过程控制", "过程控制/良率管理全球#1"),
    "8035.T": ("Tokyo Electron", "TSE", "$70B", "n", "半导体设备", "日本最大半导体设备商"),
    "SNPS": ("Synopsys", "NASDAQ", "$75B", "n", "EDA", "EDA软件#1"),
    "CDNS": ("Cadence Design Systems", "NASDAQ", "$80B", "n", "EDA", "EDA软件#2+Cerebrus AI"),
    "6857.T": ("Advantest", "TSE", "$30B", "n", "半导体测试", "AI GPU测试设备全球#1"),
    "TER": ("Teradyne", "NASDAQ", "$20B", "n", "测试/机器人", "半导体测试+Universal Robots"),
    "6146.T": ("Disco Corporation", "TSE", "$15B", "n", "切割设备", "半导体切割/研磨全球#1"),
    "4063.T": ("Shin-Etsu Chemical", "TSE", "$80B", "n", "硅片材料", "半导体硅片全球#1"),
    "ACMR": ("ACM Research", "NASDAQ", "$1.5B", "n", "清洁设备", "中国晶圆清洁设备#1"),
    "TSM": ("TSMC (台积电)", "NYSE", "$1.76T", "n", "晶圆代工", "全球最先进代工"),
    "005930.KS": ("Samsung Electronics", "KOSPI", "$250B", "n", "半导体/HBM", "HBM+代工+AI服务器"),
    "000660.KS": ("SK Hynix", "KOSPI", "$100B", "n", "HBM/存储", "HBM全球62%"),
    "MU": ("Micron Technology", "NASDAQ", "$100B", "n", "存储", "HBM3E+LPDDR5+NAND"),
    "0981.HK": ("SMIC (中芯国际)", "HKEX", "$48B", "n", "晶圆代工", "中国最大晶圆代工"),
    "1347.HK": ("Hua Hong Semiconductor", "HKEX", "$20B", "n", "晶圆代工", "中国第二大代工"),
    "WDC": ("Western Digital", "NASDAQ", "$30B", "n", "存储", "NAND+HDD"),
    "STX": ("Seagate Technology", "NASDAQ", "$20B", "n", "存储", "大容量HDD"),
    "002371.SZ": ("NAURA Technology (北方华创)", "SZSE", "¥100B", "n", "半导体设备", "中国最大半导体设备商"),
    "285A.T": ("Kioxia Holdings", "TSE", "$12B", "n", "NAND存储", "NAND闪存全球#3"),
    "META": ("Meta Platforms", "NASDAQ", "$1.5T", "n", "大型科技平台", "MTIA自研推理芯片"),
    "CRWV": ("CoreWeave", "NASDAQ", "$40B", "n", "GPU云", "AI-Native GPU云"),
    "NBIS": ("Nebius Group", "NASDAQ", "$10B", "n", "GPU云", "欧洲GPU云"),
    "9984.T": ("SoftBank Group", "TSE", "$100B", "n", "AI投资控股", "控股ARM+投OpenAI"),
    "AI": ("C3.ai", "NYSE", "$4B", "n", "企业AI", "企业级AI应用SaaS"),
    "ANET": ("Arista Networks", "NYSE", "$100B", "n", "网络设备", "AI数据中心以太网交换机#1"),
    "CSCO": ("Cisco Systems", "NASDAQ", "$240B", "n", "网络设备", "网络基础设施+AI数据中心"),
    "COHR": ("Coherent Corp", "NYSE", "$10B", "n", "光模块", "光模块全球约25%"),
    "LITE": ("Lumentum Holdings", "NASDAQ", "$4B", "n", "激光/光子", "激光器+光子引擎"),
    "FN": ("Fabrinet", "NYSE", "$10B", "n", "光模块代工", "光模块代工#1"),
    "SMCI": ("Super Micro Computer", "NASDAQ", "$20B", "n", "AI服务器", "AI服务器(GPU/液冷)#1"),
    "VRT": ("Vertiv Holdings", "NYSE", "$35B", "n", "数据中心散热", "AI数据中心电源+液冷"),
    "MOD": ("Modine Manufacturing", "NYSE", "$6B", "n", "散热", "数据中心散热系统"),
    "CIEN": ("Ciena Corporation", "NYSE", "$9B", "n", "光网络", "长距光网络WDM"),
    "AAOI": ("Applied Optoelectronics", "NASDAQ", "$1.5B", "n", "光收发器", "数据中心光收发器"),
    "6954.T": ("Fanuc Corporation", "TSE", "$40B", "n", "工业机器人", "工业机器人全球#1"),
    "ABB": ("ABB Ltd", "NYSE", "$100B", "n", "工业自动化", "工业机器人+电气化"),
    "CGNX": ("Cognex Corporation", "NASDAQ", "$8B", "n", "机器视觉", "机器视觉AI边缘推理"),
    "6861.T": ("Keyence Corporation", "TSE", "$100B", "n", "传感器/FA", "传感器+机器视觉"),
    "SYM": ("Symbotic", "NASDAQ", "$30B", "n", "仓储机器人", "仓储AI机器人(沃尔玛)"),
    "ZBRA": ("Zebra Technologies", "NASDAQ", "$20B", "n", "工业IoT", "移动计算+工业IoT"),
    "6723.T": ("Renesas Electronics", "TSE", "$20B", "n", "汽车芯片", "汽车MCU/SoC全球#1"),
    "ASX": ("ASE Technology Holding", "NYSE", "$37B", "n", "封装测试", "全球最大OSAT"),
    "AMKR": ("Amkor Technology", "NASDAQ", "$5B", "n", "封装", "NVIDIA AI芯片封装"),
    "688012.SH": ("AMEC (中微公司)", "SSE STAR", "¥数十B", "n", "刻蚀设备", "中国刻蚀设备#1"),
    "ONTO": ("Onto Innovation", "NASDAQ", "$6B", "n", "检测设备", "光学计量+晶圆检测"),
    "FORM": ("FormFactor", "NASDAQ", "$1.5B", "n", "测试探针", "晶圆测试探针卡"),
    "402340.KS": ("SK Square", "KOSPI", "$10B", "n", "半导体投资控股", "SK Hynix母公司"),
    "3436.T": ("Sumco Corp", "TSE", "$4B", "n", "硅片", "全球第二大硅晶圆"),
    "7735.T": ("SCREEN Holdings", "TSE", "$6B", "n", "半导体设备", "晶圆清洗+涂胶显影"),
    "4062.T": ("Ibiden Co.", "TSE", "$6B", "n", "封装基板", "FC-BGA封装基板全球#1"),
    "6594.T": ("Nidec Corporation", "TSE", "$20B", "n", "电机/散热", "数据中心冷却风扇"),
    "6981.T": ("Murata Manufacturing", "TSE", "$40B", "n", "被动元件", "MLCC"),
    "IFX": ("Infineon Technologies", "Frankfurt", "$50B", "n", "功率半导体", "SiC/GaN"),
    "STM": ("STMicroelectronics", "NYSE", "$20B", "n", "半导体", "汽车AI芯片+SiC"),
    "TATAELXSI": ("Tata Elxsi", "NSE", "$5B", "n", "半导体服务", "印度半导体设计服务"),
    "6239.TW": ("Powertech Technology", "TWSE", "$5B", "n", "封装测试", "内存模组封装测试"),
    "2308.TW": ("Delta Electronics", "TWSE", "$20B", "n", "电源/散热", "AI服务器电源PSU"),
    "WOLF": ("Wolfspeed", "NYSE", "$1B", "n", "SiC功率", "SiC碳化硅功率"),
    "006400.KS": ("Samsung SDI", "KOSPI", "$10B", "n", "电池/能源", "AI数据中心电池"),
}

# ===== 筛选逻辑 =====

# 港美股交易所白名单
US_HK_EXCHANGES = {"NYSE", "NASDAQ", "HKEX", "NYSE American"}

def parse_mcap(mcap_str: str):
    """解析市值字符串为数值(单位: Billion USD)"""
    s = mcap_str.strip()
    if s in ("小市值", "—"):
        return 0.0

    # 处理人民币/港币
    if s.startswith("¥") or s.startswith("HK$"):
        # 粗略转换: ¥ / 7, HK$ / 7.8
        s_clean = re.sub(r"[¥HK$€£+~]", "", s).strip()
        match = re.search(r"([\d.]+)\s*(T|B)?", s_clean)
        if not match:
            return None
        val = float(match.group(1))
        unit = match.group(2) or "B"
        if unit == "T":
            val *= 1000
        if mcap_str.startswith("¥"):
            return val / 7  # CNY to USD
        else:
            return val / 7.8  # HKD to USD

    if s.startswith("€") or s.startswith("£"):
        s_clean = re.sub(r"[€£+~]", "", s).strip()
        match = re.search(r"([\d.]+)\s*(T|B)?", s_clean)
        if not match:
            return None
        val = float(match.group(1))
        unit = match.group(2) or "B"
        if unit == "T":
            val *= 1000
        return val * 1.1  # rough EUR/GBP to USD

    # USD
    s_clean = re.sub(r"[$+~]", "", s).strip()
    if "数十" in s_clean:
        return 15.0  # 数十B CNY ≈ ~$2-3B... too uncertain
    match = re.search(r"([\d.]+)\s*(T|B)?", s_clean)
    if not match:
        return None
    val = float(match.group(1))
    unit = match.group(2) or "B"
    if unit == "T":
        val *= 1000
    return val


# 筛选
passed = []
removed_exchange = []
removed_mcap = []

LIST_NAMES = {"m": "Meta类", "s": "Shopify类", "n": "NVIDIA类"}

for ticker, (name, exchange, mcap_str, lists, sector, note) in DATA.items():
    # 检查交易所
    if exchange not in US_HK_EXCHANGES:
        removed_exchange.append((ticker, name, exchange, mcap_str))
        continue

    # 检查市值
    mcap_val = parse_mcap(mcap_str)
    if mcap_val is None or mcap_val < 5.0:
        removed_mcap.append((ticker, name, mcap_str, mcap_val))
        continue

    list_labels = [LIST_NAMES[c] for c in lists if c in LIST_NAMES]
    passed.append((ticker, name, exchange, mcap_str, mcap_val, "/".join(list_labels), sector, note))

# 排序: 按市值降序
passed.sort(key=lambda x: -x[4])

# 输出结果
print("=" * 80)
print(f"📊 筛选结果：港美股 + 市值≥$5B")
print(f"=" * 80)
print(f"✅ 通过: {len(passed)} 家")
print(f"❌ 交易所不符: {len(removed_exchange)} 家")
print(f"❌ 市值不足$5B: {len(removed_mcap)} 家")
print()

# 按分类统计
meta_count = sum(1 for p in passed if "Meta类" in p[5])
shop_count = sum(1 for p in passed if "Shopify类" in p[5])
nv_count = sum(1 for p in passed if "NVIDIA类" in p[5])
print(f"分类统计: Meta类={meta_count}, Shopify类={shop_count}, NVIDIA类={nv_count}")
print()

print("--- 通过的公司 ---")
print(f"{'#':>3} | {'Ticker':<12} | {'公司名':<35} | {'交易所':<8} | {'市值':>10} | {'分类':<20} | {'行业'}")
print("-" * 130)
for i, (ticker, name, exchange, mcap_str, mcap_val, lists, sector, note) in enumerate(passed, 1):
    print(f"{i:>3} | {ticker:<12} | {name:<35} | {exchange:<8} | {mcap_str:>10} | {lists:<20} | {sector}")

print()
print("--- 因交易所移除 ---")
for ticker, name, exchange, mcap_str in removed_exchange:
    print(f"  {ticker:<14} {name:<30} {exchange:<15} {mcap_str}")

print()
print("--- 因市值<$5B移除 ---")
for ticker, name, mcap_str, mcap_val in removed_mcap:
    val_str = f"${mcap_val:.1f}B" if mcap_val is not None else "?"
    print(f"  {ticker:<14} {name:<30} {mcap_str:<12} (≈{val_str})")
