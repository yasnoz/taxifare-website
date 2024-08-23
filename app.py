import streamlit as st
import pandas as pd
import requests
import streamlit.components.v1 as components
import pydeck as pdk


'''
# TaxiFarePredictor
'''

st.markdown('''
This is a tool to predict your taxi fare in New York city.
''')

'''
## Map of New York City
'''

''
## Map of New York City


# Define the initial view state of the map centered on New York City
initial_view = pdk.ViewState(
    latitude=40.7831,  # Latitude of Manhattan
    longitude=-73.9712,  # Longitude of Manhattan
    zoom=12,  # Initial zoom level
    pitch=50,  # Pitch angle
)

# Create a deck.gl layer for the map
layer = pdk.Layer(
    "ScatterplotLayer",
    data=[],  # Empty data for now; you can populate this with points later
    get_position="[longitude, latitude]",
    get_color="[200, 30, 0, 160]",
    get_radius=200,
)

# Render the map in Streamlit using pydeck
deck = pdk.Deck(
    map_style="mapbox://styles/mapbox/streets-v11",  # Map style
    initial_view_state=initial_view,
    layers=[layer],
)

# Display the map
st.pydeck_chart(deck)


'''
## Please enter the details of your ride:
'''

pickup_date = st.text_input(label="Pickup date", value="2013-07-06")
pickup_time = st.text_input(label="Pickup time", value="17:18:00")
pickup_longitude = float(st.number_input(label="Pickup longitude", value=-73.950655))
pickup_latitude = float(st.number_input(label="Pickup latitude", value=40.783282))
dropoff_longitude = float(st.number_input(label="Dropoff longitude", value=-73.984365))
dropoff_latitude = float(st.number_input(label="Dropoff latitude", value=40.769802))
passenger_count = int(st.number_input(label="Passenger count", value=1))


pickup_datetime =f'{pickup_date} {pickup_time}'

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    params = {'pickup_datetime': pickup_datetime,
              'pickup_longitude': pickup_longitude,
              'pickup_latitude': pickup_latitude,
              'dropoff_longitude': dropoff_longitude,
              'dropoff_latitude': dropoff_latitude,
              'passenger_count': passenger_count
              }

    response = requests.get(url, params=params).json()

f'Your fare is approximated to be ${round(response["fare"],2)}.'
