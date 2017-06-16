import mido
import time
import requests
from datadog import statsd

from tonal import Tonal, mapping

API_KEY = "ADD_PI_KEY_HERE"
GEO = "40.712784,-74.005941"
call = "https://api.forecast.io/forecast/{0}/{1}"

output = mido.open_output()
tonal = Tonal()
mid_range = tonal.create_sorted_midi("HarmonicMajor", "C")
weather = call.format(API_KEY, GEO)
start = time.time()
max_time = 100
values = dict()
old_values = dict()

chans = dict(
    temp=1,
    app_temp=2,
    dew=3,
    humidity=4,
    visibility=5,
    ozone=6,
    windBearing=7
)


def get_info():
    hourly = []
    r = requests.get(weather)
    for i in range(len(r.json()["hourly"]["data"])):
        hourly.append(r.json()["hourly"]["data"][i])
    return hourly


def parse(record):
    values.update(temp=record["temperature"])
    values.update(
        app_temp=record["apparentTemperature"]
    )
    values.update(dew=record["dewPoint"])
    values.update(humidity=record["humidity"] * 100)
    values.update(visibility=record["visibility"] * 10)
    values.update(ozone=record["ozone"])
    values.update(ozone=record["windBearing"])

keys = ["temperature", "apparentTemperature", "dewPoint", "humidity",
        "visibility", "ozone", "windBearing"]

while True:
    data = get_info()
    for item in data:
        parse(item)
        for key, value in values.iteritems():
            chan = chans.get(key)
            try:
                output.send(mido.Message(
                    'note_on',
                    note=mapping(value, mid_range),
                    velocity=50,
                    channel=chan))
            except Exception as e:
                print("Error: {}".format(e.message))
            time.sleep(1)
            print(key, value, "note on", chan)
            statsd.gauge(key, value)
    for item in data:
        parse(item)
        for key, value in values.iteritems():
            chan = chans.get(key)
            output.send(mido.Message(
                'note_off',
                note=mapping(value, mid_range),
                channel=chan))
            time.sleep(1)
            print(key, value, "note off", chan)
