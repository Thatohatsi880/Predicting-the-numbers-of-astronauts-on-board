import json
import urlib.request
import turtle
import time
import webbrowser
import geocoder

url = "https://api.open-notify.org/asreons.json"
response = urlib.request.urlopen(url)
result = json.loads(response.read())
file = open("iss.txt", "w")
file.write("There are currently" + 
           str(result["number"]) + "astronauts on the ISS: /n/n")

people = result["people"]
for p in people:
    file.write(p['name'] + "- on board" + "/n")
#print long and lot
g= geocoder.ip('me')
file.write("/n Your current latitude and longitude is: " + str(g.latlng))
file.close()
webbrowser.open("iss.txt")