import os
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

for entry in xml["feed"]["entry"]:
    title = entry["title"].replace(" ", "")
    fname = "blog/" + title +".md"
    with open(fname, "w") as f:
        f.write(entry["content"]["#text"])