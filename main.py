import requests
from constants import *

def main():
    atcocode = ''
    # appId = '2009b387'
    # appKey = '7b98ba9c457f6c782a48965cdf8f8eb6'
    r = requests.get(f'http://transportapi.com/v3/uk/bus/stop/{atcoCode}/live.json?app_id={appId}&app_key={appKey}')
    response = r.json()
    departures = response["departures"]
    for busNumber in departures:
        print(busNumber)
    for departures in departures[busNumber]:
        print(departures)
        depatureTime = departures['expected departure time']
        


# prints json as an array


if __name__ == "__main__": main()