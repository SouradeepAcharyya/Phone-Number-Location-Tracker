import phonenumbers
from phonenumbers import geocoder, carrier
from test import number
import folium
from opencage.geocoder import OpenCageGeocode
from dotenv import load_dotenv
import os

# ✅ Load API key securely
load_dotenv()
Key = os.getenv("OPENCAGE_API_KEY")

# Parse and get location info
check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")
print("Location:", number_location)

service_provider = phonenumbers.parse(number)
print("Carrier:", carrier.name_for_number(service_provider, "en"))

# Geocode location
geocoder_api = OpenCageGeocode(Key)
query = str(number_location)
results = geocoder_api.geocode(query)

# Check and map
if results and len(results):
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print("Latitude:", lat, "Longitude:", lng)

    map_location = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=number_location).add_to(map_location)
    map_location.save("mylocation.html")
    print("Map saved as mylocation.html")
else:
    print("❌ Location could not be geocoded. Try a more specific number.")
