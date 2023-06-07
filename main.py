import json
from pprint import pprint
import requests
from geopy import distance
import folium
from flask import Flask


#________________________________________________________________________________________________#


def fetch_coordinates(yandex_geocoder_apikey, address):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    response = requests.get(base_url, params={
        "geocode": address,
        "apikey": yandex_geocoder_apikey,
        "format": "json",
    })
    response.raise_for_status()
    found_places = response.json()['response']['GeoObjectCollection']['featureMember']

    if not found_places:
        return None

    most_relevant = found_places[0]
    lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
    return lat, lon


#________________________________________________________________________________________________#    
yandex_geocoder_apikey = ("ef14f529-5559-43da-8ee6-5ae1ed765b47")
#просто ключ от яндекс геоокодера / yandex geocoder key

person_location  = input("Где вы находитесь?")
person_coords = fetch_coordinates(yandex_geocoder_apikey , person_location )
#Местонахождение человека (безкоорд)/Location of a person(without coordinates)


#_______________________________________________________________________________
with open("coffee.json", "r", encoding='UTF-8') as my_file:
  file_contents = my_file.read()
coffee_shops = json.loads(file_contents)#Из текстого формата в формат списка словарей
#Работа с файлом/Working with a file


#_______________________________________________________________________________
coffee_shops_with_distance = []
for coffee in coffee_shops:
  coffee_grab = {'title'  :            coffee['Name'] ,
              'latitude'  :  coffee['Latitude_WGS84'] ,
              'longitude' : coffee['Longitude_WGS84'] ,
              'distance'  :(distance.distance(person_coords,(coffee['Latitude_WGS84'] , coffee['Longitude_WGS84'])).km),
             }
  coffee_shops_with_distance.append(coffee_grab)
#Собственный список с кафешками/Own list with cafes


#________________________________________________________________________________
def get_user_posts(user):
    return user['distance']
distance_sorted_coffee_shops =  sorted(coffee_shops_with_distance, key=get_user_posts)
five_nearest_coffee_shops = distance_sorted_coffee_shops[0:5] 
#Ближайшая кофейня/Nearest coffee shop


#_________________________________________________________________________________
person_reversed_coords = [person_coords[0],person_coords[1]]
map = folium.Map(location = person_reversed_coords,zoom_start=13, tiles="Stamen Terrain")

tooltip = "Click me!"

folium.Marker(
    [five_nearest_coffee_shops[0]['latitude'],five_nearest_coffee_shops[0]['longitude']],
    popup=five_nearest_coffee_shops[0]['title'],
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    [five_nearest_coffee_shops[1]['latitude'],five_nearest_coffee_shops[1]['longitude']],
    popup=five_nearest_coffee_shops[1]['title'],
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    [five_nearest_coffee_shops[2]['latitude'],five_nearest_coffee_shops[2]['longitude']],
    popup=five_nearest_coffee_shops[2]['title'],
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    [five_nearest_coffee_shops[3]['latitude'],five_nearest_coffee_shops[3]['longitude']],
    popup=five_nearest_coffee_shops[3]['title'],
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    [five_nearest_coffee_shops[4]['latitude'],five_nearest_coffee_shops[4]['longitude']],
    popup=five_nearest_coffee_shops[4]['title'],
    icon=folium.Icon(color="green", icon="info-sign"),
).add_to(map)

folium.Marker(
    person_reversed_coords,
    popup="Ваше местонахождение",
    icon=folium.Icon(color="red", icon="info-sign"),
).add_to(map)

map.save("index.html")
#Работа с картой/Work with map


#_______________________________________________________________________
def website():
    with open('index.html', 'r' , encoding ='UTF-8') as file:
      return file.read()


app = Flask(__name__)
app.add_url_rule('/', 'hello', website)

pprint(five_nearest_coffee_shops)
app.run('0.0.0.0')
#Работа по созданию локального сайта/Work with local website