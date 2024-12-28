# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24602058"))
API_HASH = getenv("API_HASH", "b976a44ccb8962b20113113f84aeebf6")
BOT_TOKEN = getenv("BOT_TOKEN", "7851100883:AAF_li2stMTYKJsmZeGTkNWXVWyZ82oj0y4")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7303810912").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://alexdev3604434:z1XtIpe508UzmWhN@cluster0.pnsbr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002155004811")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002224203739"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
