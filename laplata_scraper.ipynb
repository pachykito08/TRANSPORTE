import requests
from bs4 import BeautifulSoup
import json
from geopy.geocoders import Nominatim
import time

# Inicializar geocodificador
geolocator = Nominatim(user_agent="laplata_scraper")

def geocode_place(place_name):
    try:
        location = geolocator.geocode(place_name + ", La Plata, Argentina")
        if location:
            return [location.longitude, location.latitude]
    except:
        return None

# Scraping de recorridos
url = "https://www.laplata.gob.ar/transportePublico/#/"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")

routes = {}
for line in soup.find_all("div", class_="recorrido"):
    linea = line.find("h3").text.strip()
    paradas = [p.text.strip() for p in line.find_all("li")]
    routes[linea] = paradas

# Construcción de GeoJSON
features = []
for linea, paradas in routes.items():
    coords = []
    for p in paradas:
        c = geocode_place(p)
        if c:
            coords.append(c)
            time.sleep(1)  # evitar bloqueo de Nominatim
    if coords:
        features.append({
            "type": "Feature",
            "properties": {"linea": linea},
            "geometry": {"type": "LineString", "coordinates": coords}
        })

geojson_data = {"type": "FeatureCollection", "features": features}

with open("laplata_rutas.geojson", "w", encoding="utf-8") as f:
    json.dump(geojson_data, f, ensure_ascii=False, indent=2)

print("Archivo GeoJSON generado: laplata_rutas.geojson")
