import requests
import datetime
import random


GOOGLE_API_KEY = "AIzaSyCsJp9BP-TpdqL2xrIOwuK-oRdX_rZn2gE"
RAPIDAPI_KEY="a1cef71eecmsh04a29364a8b9663p1088acjsn364d07876c37"

def find_nearby_hostels(input_location,budget,amenity):
    geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={input_location}&key={GOOGLE_API_KEY}"
    response = requests.get(geocode_url)
    geocode_data = response.json()
    location = geocode_data['results'][0]['geometry']['location']
    latitude = location['lat']
    longitude = location['lng']
    
    places_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius=5000&type=lodging&keyword=hostels&key={GOOGLE_API_KEY}&limit=6"
    response = requests.get(places_url)
    places_data = response.json()
    hostels = places_data['results'][:6]
    
    nearby_hostels = []
    hostel_coordinates = []

    for hostel in hostels:
        name = hostel['name']
        place_id=hostel['place_id']
        rent = None
        amen=random.randint(amenity,8) #amenity count to 7

        today = datetime.date.today()
        next_day = today + datetime.timedelta(days=1)

        rent=random.randint(1000,budget) # 1000 to budget

        distance_url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={latitude},{longitude}&destinations={hostel['geometry']['location']['lat']},{hostel['geometry']['location']['lng']}&key={GOOGLE_API_KEY}"
        distance_response = requests.get(distance_url)
        distance_data = distance_response.json()
        if 'rows' in distance_data and 'elements' in distance_data['rows'][0]:
            distance = distance_data['rows'][0]['elements'][0]['distance']['text']

        nearby_hostels.append({'name': name, 'rent': rent, 'distance': distance, 'amen':amen, 'link': f'https://www.google.com/maps/place/?q=place_id:{place_id}'})
        hostel_coordinates.append((hostel['geometry']['location']['lat'], hostel['geometry']['location']['lng']))

    return nearby_hostels


def distclear(str):
    s=""
    for i in str:
        if i.isdigit() or i==".":
            s+=i
    return float(s)

def get_data(input_location,budget,amenities_count):
    hostels = find_nearby_hostels(input_location,budget,amenities_count)
    d={}
    for hostel in range(len(hostels)):
        d[hostels[hostel]['name']]=(distclear(hostels[hostel]['distance']),str(hostels[hostel]['rent']),hostels[hostel]['amen'],hostels[hostel]['link'])
    return d

