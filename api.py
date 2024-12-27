import http.client

conn = http.client.HTTPSConnection("od-api-sandbox.oxforddictionaries.com")

headers = {
    'app_id': "48ee3c99",
    'app_key': "15cadcc69368661a9d522441a927292c",
    'Accept': "application/json"
}

conn.request("GET", "/api/v2/translations/en/es/ace", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))