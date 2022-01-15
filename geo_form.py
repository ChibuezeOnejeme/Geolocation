import certifi
import ssl
import certifi
import geopy.geocoders
from geopy.geocoders import Nominatim
from geopy import distance
import folium
from flask import Flask,render_template


ctx = ssl.create_default_context(cafile=certifi.where())

geopy.geocoders.options.default_ssl_context = ctx



geolocator = Nominatim(user_agent='ezemiller')
city_1 = 'awka'
city_2 = 'abuja'

l1 = geolocator.geocode(city_1)
l2 = geolocator.geocode(city_2)
loc1 = ((l1.latitude,l1.longitude))
loc2 = ((l2.latitude,l2.longitude))

print(distance.distance(loc1,loc2).km)

# create a base map centered around Awka
mapObj1 = folium.Map(location = [l1.latitude,l1.longitude], zoom_start = 5)
# create a base map centered around Abuja
mapObj2 = folium.Map(location = [l2.latitude,l2.longitude], zoom_start = 5)
# create marker object for Awka and Abuja
markerObj1 = folium.Marker(location = [l1.latitude,l2.longitude])
markerObj2 = folium.Marker(location = [l2.latitude,l2.longitude])

# add marker to map
markerObj1.add_to(mapObj1)
markerObj2.add_to(mapObj2)
# display map
mapObj1.save('index.html')
mapObj2.save('kande.html')

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')
if __name__ == '__main__':
   app.run()





