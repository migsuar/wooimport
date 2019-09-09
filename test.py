# -*- coding: utf-8 -*-
import json
import sys

from woocommerce import API



# Configura API woocommerce

wcapi = API(
    url="http://succar-tello.com.ar",
    consumer_key="ck_1ae7b1993a747a56f1eb8ece81540127fb0c736d",
    consumer_secret="cs_072f40bc7a38ecdbe03f73c6f62967c5a410e7a8",
    version="wc/v3",
 )

def leer_productos():
    res=wcapi.get("products/42399").json()
    print(res)
    return True

def leer_todos_productos():
    res=wcapi.get("products/",params={"per_page": 100}).json()
    for renglon in res:
        print(renglon["id"],renglon["name"],renglon["sku"])
    return True

def leer_variaciones():
    res=wcapi.get("products/46198/variations").json()
    print(res)
    return True

def leer_atributos():
    res=wcapi.get("products/attributes").json()
    print(res)
    return True

def leer_categorias():
    res=wcapi.get("products/categories").json()
    print(res)
    return True


#leer_productos()
leer_variaciones()
#leer_atributos()
#leer_categorias()
#leer_todos_productos()