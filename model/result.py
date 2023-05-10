#!/usr/bin/env python
# coding: utf-8

import requests as rq

# create a variable to store the API url
url = 'http://localhost:5000/predict'

# create a diction for vol_moving_avg, adj_close_rolling_med
data = {
    'vol_moving_avg': 12345, 
    'adj_close_rolling_med': 25
}

# get request
result = rq.post(url, json=data)
print(result)

# run the result
volume = result.json()
print(volume)

