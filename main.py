import requests
import re

res = re.search("https://(.*).dfs.core.windows.net/", "Endpoint")  # codeql trigger

with requests.get(res) as response:
    print(response.text)
