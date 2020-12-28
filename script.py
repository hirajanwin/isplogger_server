from dotenv import load_dotenv
import speedtest
import requests
import json
import datetime
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
load_dotenv()

def initSpeedtest():
    print("Speedtest in Progress")
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    data = {
            "status": "success",
            "upload": int(res["upload"]),
            "download": int(res["download"]),
            "ping": res["ping"],
            "isp": res["client"]["isp"],
            "ip": res["client"]["ip"],
            "country": res["client"]["country"],
            "sent": res["bytes_sent"],
            "received": res["bytes_received"]
        }

    return data


def test():
    attempts = 10
    key = os.getenv("NETWORK_ID")
    server = os.getenv("SERVER")
    print(key)
    for i in range(attempts):
    
        try:

            tst = initSpeedtest()
            print(tst)
            

            req = requests.post(server + "/api/speedtest/"+key, data=tst)
            print(req)
            print("test complete")

            return "OK"

        except Exception as e:
            print(e)
            if i < attempts - 1:
                pass

                return "error"
            else:
                raise

        break

test()
