import requests
import re
import datetime


class NextBus(object):

    def __init__(self):
        self.endpoint = 'http://svc.metrotransit.org/'
        self.directions = {
            'south': 1,
            'east': 2,
            'west': 3,
            'north': 4
        }

    def get_route(self,bus_route):
        url = '{}/NexTrip/Routes?format=json'.format(self.endpoint)
        data = self.get_response(url)
        if not data :
            return None
        route = None
        # Returns a list of Transit routes that are in service on the current day.
        for i in range(0, len(data)):
            if bus_route in data[i]['Description']:
                route = data[i]['Route']
        return route

    def get_direction(self, direction):
        dir = [value for key, value in self.directions.items() if direction.lower() == key]
        if not dir:  # exit if not 1 = South, 2 = East, 3 = West, 4 = North
            return None
        return dir[0]

    def get_bus_stop(self,route,direction,bus_stop):
        url='{}/NexTrip/Stops/{}/{}?format=json'.format(self.endpoint,route,direction)
        data = self.get_response(url)
        if not data:
            return None
        stop=[data[i]['Value'] for i in range(len(data)) if bus_stop == data[i]['Text']]
        if (len(stop) == 0):
            return None
        return stop[0]

    def get_next_trip_timestamp(self,route,direction,bus_stop):
        url='{}/NexTrip/{}/{}/{}?format=json'.format(self.endpoint,route,direction,bus_stop)
        data = self.get_response(url)
        if not data:
            return None
        next_trip_timestamp = data[0]['DepartureTime']
        return next_trip_timestamp

    def get_response(self,url):
        try:
            response= requests.get(url=url)
            if response.status_code != requests.codes.ok:
                print("Unable to call the api {}".format(url))
                return None
            data = response.json()
        except Exception as e:
            print("Exception occured while getting response for url {} : {}".format(url,repr(e)))
            return None
        return data

    def calculate_time(self, time):
        timestamp = int(re.search(r'(\d+)', time).group())
        bus_time = datetime.datetime.fromtimestamp(timestamp / 1000)
        now = datetime.datetime.now()
        minutes = str(bus_time - now).split(":")[1] # get the minutes from the timestamps
        minutes = str(int(minutes) +1 )
        return minutes
