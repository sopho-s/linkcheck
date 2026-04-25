from mitmproxy import http
import requests
import time

with open("../apikey", "r") as f:
    APIKEY = f.read()

class Interceptor:
    def request(self, flow: http.HTTPFlow) -> None:
        url: str = flow.request.url
        payload = {
            "url": url,
            "visibility": "unlisted",
        }

        headers = {
            "Content-Type": "application/json",
            "api-key": APIKEY
        }


        response = requests.post("https://urlscan.io/api/v1/scan", json=payload, headers=headers)
        print(response.json())
        uuid = response.json()["uuid"]
        url = "https://urlscan.io/api/v1/result/" + uuid + "/"

        headers = {
            "api-key": APIKEY
        }

        response = requests.get(url, headers=headers)
        time.sleep(7)

        while True:
            response = requests.get(url, headers=headers)
            if response.status_code != 404:
                if response.json()["verticts"]["overall"]["malicious"] == True:
                    flow.response = http.Response.make(
                        418,
                        b"This request has been blocked as malicious",
                    )
                break
            time.sleep(2)