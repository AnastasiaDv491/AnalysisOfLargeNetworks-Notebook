import urllib.request, json 
with urllib.request.urlopen("https://codex.opendata.api.vlaanderen.be:443/api/Thema") as url:
    print("df")
    data = json.load(url)
    print(data)