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

longitude = st.number_input('Insert the longitude as a float')
st.write('The longitude is ', longitude)

#Let's ask for dropoff_longitude:

latitude = st.number_input('Insert the latitude as a float')
st.write('The latitude is ', latitude)

#Let's ask for droppoff longitude:

dropff_longtitude = st.number_input('Insert the dropoff longtitude as a float')
st.write('The dropoff longtitude is ', dropff_longtitude)

#Let's ask for droppoff longitude:

dropff_latitude = st.number_input('Insert the dropoff latitude as a float')
st.write('The dropoff latitude is ', dropff_latitude)

#Let's ask for passenger count:

passengers = st.number_input('Insert the number of passengers as an integer')
st.write('The number of passengers is ', passengers)

# 2. Let's build a dictionary containing the parameters for our API

params={'date': date,
        'time': time,
        'longitude':longitude,
        'latitude': latitude,
        'longitude':longitude,
        'dropff_longtitude': dropff_longtitude,
        'dropff_latitude': dropff_latitude,
        'passengers':passengers}

# 3. Let's call our API using the `requests` package

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    response=requests.get(url, params=params)

#4. Let's retrieve the prediction from the **JSON** returned by the API

if response.status_code == 200:
    fare = response.json().get('fare', 'No fare returned')
    st.write('Predicted fare:', fare)
else:
    st.write('Error:', response.status_code)
