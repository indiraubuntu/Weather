import streamlit as st
import requests
import pydeck as pdk

st.header('Méteo France')

col1, col2 = st.columns(2)

with col1:
    city = st.text_input("Entrez une ville :")

# Default coordinates for the map when no city is inputted
default_coords = {'lat': 48.8566, 'lon': 2.3522}  # Defaults to Paris, but you can adjust as needed

if col2.button('GO') and city:
    # Fetching data from the OpenWeather API
    API_KEY = st.secrets["general"]["API_KEY"]
    
    def fetch_weather_data(city, API_KEY):
        BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"
        response = requests.get(BASE_URL, params={"q": city, "units": "metric", "appid": API_KEY})
        
        if response.status_code == 200:
            return response.json()
        else:
            return None

    data = fetch_weather_data(city, API_KEY)   # Assign the result to the variable data

    if data:
        # Extracting the required details
        coords = data['city']['coord']
        today = data['list'][0]['main']['temp']
        tomorrow = data['list'][8]['main']['temp']
        day_after_tomorrow = data['list'][16]['main']['temp']

        # Displaying the temperatures
        st.write(f"Today's temperature in {city}: {today}°C")
        st.write(f"Tomorrow's temperature in {city}: {tomorrow}°C")
        st.write(f"Day after tomorrow's temperature in {city}: {day_after_tomorrow}°C")
    else:
        st.write(f"No weather data available for {city}.")
        coords = default_coords
else:
    coords = default_coords

# Displaying the map using pydeck
map_layer = pdk.Layer(
    "ScatterplotLayer",
    data={
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [coords['lon'], coords['lat']]
            }
        }]
    },
    get_position="[coordinates[0], coordinates[1]]",
    get_radius=10000,  # Adjusted to make the point look like a pinpoint
    get_fill_color="[0, 0, 255]",  # Blue color
    pickable=True,
    opacity=0.6
)

st.pydeck_chart(pdk.Deck(layers=[map_layer], initial_view_state={"latitude": coords['lat'], "longitude": coords['lon'], "zoom": 10, "pitch": 50}))
