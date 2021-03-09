from skyfield.api import load
import json
import threading

#loads the ephemeris amd then loads the planets
planets = load('de421.bsp')
earth, mars, saturn, mercury, venus, jupiter, uranus, neptune = planets['earth'], planets['mars'], planets['SATURN BARYCENTER'], planets['MERCURY BARYCENTER'], planets['VENUS BARYCENTER'], planets['JUPITER BARYCENTER'], planets['URANUS BARYCENTER'], planets['NEPTUNE BARYCENTER']


def updateAstroData():
  from skyfield.api import load

 #works out what time scale to use and what the current time is for that timescale
  ts = load.timescale()
  t = ts.now()
  planetList = [mars, saturn, mercury, venus, jupiter, uranus, neptune]
  planetData = []
  threading.Timer(400.0, updateAstroData).start()
  for planet in planetList:

    #This tells the function where the user is (earth) and what your looking at (whatever planet the loop is on)
    #The second line tells it what to measure, in this case ra, dec and distance.
    astrometric = earth.at(t).observe(planet)
    ra, dec, distance = astrometric.radec()
    
    def appendData(notStr):
      nowStr = str(notStr)
      planetData.append(nowStr)
    appendData(ra)
    appendData(dec)

  #sends the planetData to the json file
  print(planetData)
  with open('testdata.json', 'w') as json_file:
    json.dump(planetData, json_file)

updateAstroData()