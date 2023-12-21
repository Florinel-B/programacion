import urllib.request
import json

def descargarJSON(url):
    data = urllib.request.urlopen(url).read().decode()
    obj = json.loads(data)
    return obj
def recorrerprecios(dinero):
    d={}
    dia=0 
    for i in range (len(dinero['included'][0]['attributes']['values'])):
        if i>24:
            hora=i//24
        if i % 24 == 0 :
            dia +=1
        d[dia,i]= dinero['included'][0]['attributes']['values'][i]['value']
    return d

        




data_ini="2023-12-01"
data_fin="2023-12-14"
url="https://apidatos.ree.es/es/datos/mercados/precios-mercados-tiempo-real?start_date="+data_ini+"T00:00&end_date="+data_fin+"T23:59&time_trunc=hour"
a=descargarJSON(url)
dinerito=a['included'][0]['attributes']['values'][0]['value']
print(dinerito)
preciopordia=recorrerprecios(a)
print(preciopordia)