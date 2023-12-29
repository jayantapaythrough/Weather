import streamlit as st
from geopy.geocoders import Nominatim
import requests


# Function to get location coordinates
def get_location_coordinates(location_name):
    geolocator = Nominatim(user_agent="your_app_name")
    try:
        location_data = geolocator.geocode(location_name)
        if location_data:
            latitude = location_data.latitude
            longitude = location_data.longitude
            return latitude, longitude
        else:
            st.error(f"Could not find coordinates for {location_name}.")
            return None, None
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None, None

# Streamlit app
st.title("Weather Information App")

# User input for location
location_name = st.text_input("Enter a location:")

# left, right = st.columns(2)

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0026ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #ff0051;
    color:#001eff;
    }
</style>""", unsafe_allow_html=True)

b = st.button("Go")

# Get location coordinates
if b:
    # Get location coordinates
    latitude, longitude = get_location_coordinates(location_name)

    # Check if coordinates are available
    if latitude is not None and longitude is not None:
        # Make the API request
        url = f'https://api.weatherbit.io/v2.0/current?lat={latitude}&lon={longitude}&key={key}&include=minutely'
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            st.write("Weather Information:")
            st.write(data)
        else:
            st.error(f"Error: {response.status_code}")







