# from https://katb.in/iqahelikevo
import requests

data = [
    {
      "name": "Kraken",
      "address": "IVBHJFHZWPXRX2EA7AH7Y4UTTBO2AK73XI65OIXDEAEN7VO2IHWXKOKOVM"
    },
    {
        "name": "Binance",
        "address": "SP745JJR4KPRQEXJZHVIEN736LYTL2T2DFMG3OIIFJBV66K73PHNMDCZVM"
    },
    {
        "name": "Binance",
        "address": "HEOQ3S6V47RFLU2RZ5GTQYJBEFRL54UWZ77PNUBNTDVSXIPYOPE2XZJSLE"
    },
    {
        "name": "Binance US",
        "address": "QXE3ITCREUKZXA57VZ3KOHFSTENVWE7FLLHZ5ITJ2BVTCUJ3YTUZRL2TNM"
    },
    {
        "name": "Binance",
        "address": "MTCEM5YJJSYGW2RCXYXGE4SXLSPUUEJKQAWG2GUX6CNN72KQ3XPJCM6NOI"
    },
    {
        "name": "Kraken",
        "address": "IVBHJFHZWPXRX2EA7AH7Y4UTTBO2AK73XI65OIXDEAEN7VO2IHWXKOKOVM"
    },
    {
        "name": "KuCoin",
        "address": "IMGMVBZEPMM36AIMWI7FZHG2G44KEESC5ALZHWX7B7SBNBDY6Z7COYMO6U"
    },
    {
        "name": "Crypto.com",
        "address": "USJEM4NZJQ5WQJFRSAVUASFSRJTA5L5F5RSZEQC7WM4IQPY7SX6HRC2E5Q"
    },
    {
        "name": "Huobi",
        "address": "QD6NSI23VUWBUUT5PJJV7KZ34QEWRIOJJACSYA2OR743RCQQJVLEVZ4WW4"
    },
    {
        "name": "Yieldly",
        "address": "FMBXOFAQCSAD4UWU4Q7IX5AV4FRV6AKURJQYGXLW3CTPTQ7XBX6MALMSPY"
    },
    {
        "name": "Coinbase Pro",
        "address": "UXVAPU4KERSMNUILDVZUKKF4KMWQ7RFSSYPXYSEGSYNYILC4FEHISKRBNM"
    },
    {
        "name": "Coinbase",
        "address": "LWUWBZPVBS24TDBDZ72LUYJJF75KUJ3IUP6YGG45PVKGNAJYRGQD5CSCPA"
    },
    {
        "name": "MEXC",
        "address": "M3IAMWFYEIJWLWFIIOEDFOLGIVMEOB3F4I3CA4BIAHJENHUUSX63APOXXM"
    },
    {
        "name": "Okex",
        "address": "ZVMOZVZJK64NEYDPUDGGC52NI6HOX2LUQVIWYCQTJ2DFXRGPL72C2BQYNM"
    },
    {
        "name": "Huobi",
        "address": "J4AEINCSSLDA7LNBNWM4ZXFCTLTOZT5LG3F5BLMFPJYGFWVCMU37EZI2AM"
    },
    {
        "name": "Bitfinex",
        "address": "JDQ7EW3VY2ZHK4DKUHMNP35XLFPRJBND6M7SZ7W5RCFDNYAA47OC5IS62I"
    },
    {
        "name": "Bitmax",
        "address": "GGUMZYT7GHGTOUOMBXVY3AY754UKOKABBD4732COI7IVXMOCR4P4X23YYA"
    },
    {
        "name": "Coinlist",
        "address": "AXY45DUDUDXFK2IBS6L4H4HFUD23IEIN7JJAQKQAQFAGP2L77P4F57NJ5M"
    },
    {
        "name": "Coinlist",
        "address": "INEMEBYNS5I2CMX4JH3B7HFSY26AMJEO4T23Q3K6H6F7WR7JZMJ2YTOS7A"
    },
    {
        "name": "Okex",
        "address": "33TEPJ2V7LVEUF5UJ4XZKTNJDZ2THE67TH7BRJKQZH6ZPKLPWKE4DWGMAI"
    }
    {
        "name": "Bitstamp",
        "address": "6ITEMKNE36NXKWWDL3WBYDHK3T77UY3QDCMBYBC5QMGVDFWEP626JX6CXY"
    }
    Coinbase
    UXVAPU4KERSMNUILDVZUKKF4KMWQ7RFSSYPXYSEGSYNYILC4FEHISKRBNM
    
    MEXC
    M3IAMWFYEIJWLWFIIOEDFOLGIVMEOB3F4I3CA4BIAHJENHUUSX63APOXXM
  ]

api_accounts_link = "https://algoexplorerapi.io/idx2/v2/accounts/"
sum = 0
for wallet in data:
    s = requests.get(api_accounts_link + wallet["address"]).json()["account"]["amount"]
    print(wallet["name"],"has","{:,}".format(s / 1000000),"ALGO")
    sum += s
print("TOTAL:","{:,}".format(sum / 1000000),"ALGO")