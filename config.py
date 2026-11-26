# API Keys
OTP_INDIA_API_KEY = "c7eb1d1c86327105b1e3fb7855d27f64c74609da9762f14f"
FOUR_SIM_API_KEY = "b35000de7ade8dcda3a636d143e86d41"
OTPDOCTOR_API_KEY = "peoedizjb7jqmday8iuml9r456ljyd62"
TEMPOTP_API_KEY = "bef6c0470508e2ab3377ebca62129d0e"
TEMPORASMS_API_KEY = "ad74bdcf858b8324973ea4a0f03504067877"

# SpyEye
BASE_URL = "https://spyeyeloots4.online/up_yonoV3/"
SPYEYE_API_KEY = "TBRWBDEEPFRND7WYB"

# License (Safety ke liye rakha hai agar code import kare)

# Timers
MAIN_GAME_WAIT = 130
SUBGAME_FOREGROUND_WAIT = 40
NEXT_GAME_DELAY = 3

BACKGROUND_TIMEOUT_4SIM = 900
BACKGROUND_TIMEOUT_OTPDOCTOR = 1200
BACKGROUND_TIMEOUT_TEMPOTP = 900
BACKGROUND_TIMEOUT_TEMPORASMS = 900
BACKGROUND_TIMEOUT_OTPINDIA = 900

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

# Games map
GAME_MAP = {
    "567slots": {"api": "567slots", "ui": "567slots"},
    "MBMBet": {"api": "mbmbet", "ui": "MBMBet"},
    "Bingo": {"api": "bingo101", "ui": "Bingo"},
    "IndSlots": {"api": "indslots", "ui": "IndSlots"},
    "HiRummy": {"api": "hirummy", "ui": "HiRummy"},
    "Maha": {"api": "mahagames", "ui": "Maha"},
    "YonoVip": {"api": "yonovip", "ui": "YonoVip"},
    "789Jackpots": {"api": "789jackpots", "ui": "789Jackpots"},
    "INDRummy": {"api": "indrummy", "ui": "INDRummy"},
    "YonoGames": {"api": "yonogames", "ui": "YonoGames"},
    "SpinCrush": {"api": "spincrush", "ui": "SpinCrush"},
    "YonoSlots": {"api": "yonoslots", "ui": "YonoSlots"},
    "GoGoRummy": {"api": "gogorummy", "ui": "GoGoRummy"},
    "INDclub": {"api": "indclub", "ui": "INDclub"},
    "YonoArcade": {"api": "yonoarcade", "ui": "YonoArcade"},
    "Rummy91": {"api": "rummy91", "ui": "Rummy91"},
    "RummyLudo": {"api": "rummyludo", "ui": "RummyLudo"},
    "YonoRummy": {"api": "yonorummy", "ui": "YonoRummy"},
    "ShareSlots": {"api": "shareslots", "ui": "ShareSlots"},
    "YesSpin": {"api": "yesspin", "ui": "YesSpin"},
    "GoldRummy": {"api": "goldrummy", "ui": "GoldRummy"},
    "TopRummy": {"api": "toprummy", "ui": "TopRummy"},
    "JoyRummy": {"api": "joyrummy", "ui": "Joyrummy"},
    "RummyZip": {"api": "rummyzip", "ui": "RummyZip"},
    "RummyRumble": {"api": "rummyrumble", "ui": "RummyRumble"},
    "SpinRummy": {"api": "spinrummy", "ui": "spinrummy"},
    "Spin101": {"api": "spin101", "ui": "Spin101"},
    "SagaSlots": {"api": "sagaslots", "ui": "SagaSlots"},
    "LoveRummy": {"api": "loverummy", "ui": "LoveRummy"},
    "SpinWinner": {"api": "spinwinner", "ui": "SpinWinner"},
    "JaiHo777": {"api": "jaiho777", "ui": "JaiHo777"},
    "JeetSpin": {"api": "jeetspin", "ui": "JeetSpin"},
    "SpinGold": {"api": "spingold", "ui": "SpinGold"},
    "JaiHoSpin": {"api": "jaihospin", "ui": "JaiHoSpin"},
    "Hindi777": {"api": "hindi777", "ui": "Hindi777"},
    "JaiHoRummy": {"api": "jaihorummy", "ui": "JaiHoRummy"}
}

API_TO_UI = {v["api"].lower(): v["ui"] for v in GAME_MAP.values()}
