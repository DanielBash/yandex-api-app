"""
steal my api keys, they were granted for free by yandex,
and requested to publish them in a repo. So fuck them
"""

import requests

geocoder_apikey = "8013b162-6b42-4997-9691-77b7074026e0"
static_apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
org_apikey = "72e09cfa-9163-4f5c-ba75-916fb947567b"


def get_static(api=static_apikey, ll='37.677751,55.757718', spn="", pt=''):
    return requests.get("https://static-maps.yandex.ru/v1", params={
        'apikey': api,
        'll': ll,
        'pt': pt
    })


def get_geocoder(location='Красная пл-дь, 1', api=geocoder_apikey, formating='json'):
    return requests.get("http://geocode-maps.yandex.ru/1.x/", params={
        'apikey': api,
        'format': formating,
        'geocode': location
    })


def get_location(data):
    toponym = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    long, lat = toponym_coodrinates.split(" ")
    delta = "0.005"
    return long, lat, delta


def get_org(api=org_apikey, ll="37.588392,55.734036", lang="ru_RU", text="аптека", type='biz'):
    return requests.get("https://search-maps.yandex.ru/v1/", params={
        'apikey': api,
        'll': ll,
        "lang": lang,
        "type": type,
        "text": text
    })
