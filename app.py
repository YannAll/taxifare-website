import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''
# 1. Let's ask for user input
#Let's ask for date:

date = st.date_input(
    "What is the date?",
    datetime.date(2019, 7, 6))
st.write('Today is:', date)

#Let's ask for time:

time = st.time_input(
    "What is the time ?",
    datetime.time(8, 45))
st.write('The time is:', time)

#Let's ask for longitude:

pickup_longitude = st.number_input('Insert the longitude as a float')
st.write('The longitude is ', pickup_longitude)

#Let's ask for dropoff_longitude:

pickup_latitude = st.number_input('Insert the latitude as a float')
st.write('The latitude is ', pickup_latitude)

#Let's ask for droppoff longitude:

dropoff_longitude = st.number_input('Insert the dropoff longtitude as a float')
st.write('The dropoff longtitude is ', dropoff_longitude)

#Let's ask for droppoff longitude:

dropoff_latitude = st.number_input('Insert the dropoff latitude as a float')
st.write('The dropoff latitude is ', dropoff_latitude)

#Let's ask for passenger count:

passengers = st.number_input('Insert the number of passengers as an integer')
st.write('The number of passengers is ', passengers)

# 2. Let's build a dictionary containing the parameters for our API

params = {
    'pickup_datetime': f"{date} {time}",
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': int(passengers)
}

# 3. Let's call our API using the `requests` package

url = 'https://taxifare.lewagon.ai/predict'

response=requests.get(url, params=params)

print(response.status_code == 200)

if response.status_code == 200:
    fare = response.json().get('fare', 'No fare returned')
    st.write('Predicted fare:', fare)
else:
    st.write('Error:', response.status_code)

print(f"The expected fare for your taxi is: {response.json().get('fare', 'No fare returned')}")






# Test data to plug into the app
#pickup_datetime='2014-07-06 19:18:00'
#pickup_longitude=-73.950655,
#pickup_latitude=40.783282,
#dropoff_longitude=-73.984365
#dropoff_latitude=40.769802
#passenger_count=1)
