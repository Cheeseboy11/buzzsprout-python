#!/usr/bin/env python3.7
import requests
import json
import random

def build_url(profileid, token, json):
    base_url = 'https://www.buzzsprout.com/api'
    url = f"{base_url}/{profileid}/{json}?api_token={token}"
    return url

def random_episode(profileid, token):
    url = build_url(profileid, token, 'episodes.json')
    print(f"The URL built is: {url}")
    
    r = json.loads(requests.get(url).content)

    count = 0
    for episode in r:
        count += 1
    
    randomint = random.randint(1,count)

    episode = r[randomint]
    
    return episode