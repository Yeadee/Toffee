import requests, re, json, base64, os, datetime
from pytz import timezone
from requests_toolbelt.multipart.encoder import MultipartEncoder
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def data_decrypt(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = base64.b64decode(ciphertext)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext, AES.block_size)
    return plaintext.decode()

def toffupdate():
    inf = os.environ['TOFFEE_HEADER1']
    mp_encoder = MultipartEncoder(fields={'data': inf})
    fheader = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Content-Type': mp_encoder.content_type}
    furl = os.environ['TOFFEE_URL1']
    res = requests.post(furl,data=mp_encoder,headers=fheader,proxies=proxy)
    secret_key=os.environ['TOFFEE_SECRET_KEY']
    try:
        dbdata = json.loads(data_decrypt(secret_key.encode(),res.text))["response"]["dbVersionV2"]
    except:
        data={"message":"proxy not working","time":disptime}
        with open("toffee_channel_data.json","w") as w:
            json.dump(data,w,indent=2)
        return "proxy not working."
    version = "1793"
    for item in dbdata:
        if item["api_name"]=="getUgcAppHomePageContentTofeeV2":
            version = item["db_version"]
            break
    url2=os.environ['TOFFEE_URL2']
    api=f"{url2}{version}"
    headers={"client-api-header":os.environ['TOFFEE_HEADER2']}
    req=requests.get(url=api,headers=headers,proxies=proxy)
    categories=json.loads(data_decrypt(secret_key.encode(),req.text))["response"]["categories"]
    #with open("toffee_raw_data.json","w") as w:
    #    json.dump(categories,w,indent=2)
    all_data=[]
    for category in categories:
        for channel in category['channels']:
            data = {}
            data["category_name"],data['id'],data['name'],data['logo'],data['link'],data['cookie'],data["cookie_expire"] = channel["category_name"],channel['id'],channel['program_name'],channel['channel_logo'],channel['plain_hls_url'],channel['sign_cookie'],channel["sign_cookie_expire"]
            if "streamer" in channel['plain_hls_url']:
                data['link'] = channel['plain_hls_url_for_url_type']
            all_data.append(data)
    fulldata = {}
    fulldata['channels_found'] = len(all_data)
    fulldata["last_update"] = disptime
    fulldata['channels'] = all_data
    with open("toffee_channel_data.json","w") as w:
        json.dump(fulldata,w,indent=2)
    return None

proxy=json.loads(os.environ['BDPROXY'])

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
timenow=datetime.datetime.now(timezone("Asia/Dhaka"))
disptime=timenow.strftime("%d-%m-%Y %I:%M:%S %p")
toffupdate()

