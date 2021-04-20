"""Constants of the TpeWater Fee component."""

DEFAULT_NAME = "TpeWater Fee"
DOMAIN = "tpewater_fee"
DOMAINS = ["sensor"]
DATA_KEY = "sensor.tpewater_fee"

ATTR_BILLING_MONTH = "billing_month"
ATTR_BILLING_DATE = "billing_date"
ATTR_PAYMENT = "payment"
ATTR_WATER_CONSUMPTION = "water_consumption"
ATTR_NEXT_BILLING_DATE = "next_billing_date"
ATTR_BILL_AMOUNT = "billing_amount"
ATTR_HTTPS_RESULT = "https_result"
ATTR_LIST = [
    ATTR_BILLING_MONTH,
    ATTR_BILLING_DATE,
    ATTR_PAYMENT,
    ATTR_WATER_CONSUMPTION,
    ATTR_NEXT_BILLING_DATE,
    ATTR_BILL_AMOUNT,
    ATTR_HTTPS_RESULT
]

CONF_WATERID = "waterid"
CONF_COOKIE = "cookie"
# 5308 characters
CONF_VIEWSTATE = "viewstate"
# 668 characters
CONF_EVENTVALIDATION = "eventvalidation"
ATTRIBUTION = "Powered by TpeWater Fee Data"

HA_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 OPR/38.0.2220.41"
BASE_URL = 'https://webs.water.gov.taipei/apps/feequery'

REQUEST_TIMEOUT = 10  # seconds
