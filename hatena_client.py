import os
import time
import requests
import xmltodict as XTD
from dotenv import load_dotenv

load_dotenv()

HATENA_ID = os.environ.get("HATENA_ID")
PASSWORD = os.environ.get("PASSWORD")
BLOG_ID = os.environ.get("BLOG_ID")

url = f"https://blog.hatena.ne.jp/{HATENA_ID}/{BLOG_ID}/atom/entry"

response = requests.get(url, auth=(HATENA_ID, PASSWORD))
xml = XTD.parse(response.text)

while True:
    time.sleep(3)
    for entry in xml["feed"]["entry"]:
        title = entry["title"].replace(" ", "")
        fname = "blog/" + title +".md"
        with open(fname, "w") as f:
            text = ""
            if ("#text" in entry["content"]):
                text = entry["content"]["#text"]
            f.write(text)
    if xml["feed"]["link"][1]["@rel"] != "next":
        break
    url = xml["feed"]["link"][1]["@href"]
    response = requests.get(url, auth=(HATENA_ID, PASSWORD))
    xml = XTD.parse(response.text)

