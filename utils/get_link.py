import requests as r
async def get_link(sura, oyat):
    url = "http://api.alquran.cloud/v1/ayah/{}:{}/ar.alafasy".format(sura, oyat)
    url = r.get(url).json()['data']['audio'].replace('/', '//').replace('////', '//')
    return f"<a href='{url}'>{chr(8203)}</a>"