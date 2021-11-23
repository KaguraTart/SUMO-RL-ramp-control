'''
  {
    "SeeDocsAt": "https://github.com/Microsoft/AirSim/blob/master/docs/settings.md",
    "SettingsVersion": 1.2,
    "SimMode": "Car",
    
    "Vehicles": {
      "Car1": {
        "VehicleType": "PhysXCar",
        "X": 0, "Y": 5, "Z": -0.2

      }
  
      }
  }
'''

json = open("settings.json","w")
json.write("{\n")
json.write("\t\"SettingsVersion\": 1.2,\n\t\"SimMode\": \"Car\",\n")
json.write("\n\t\"Vehicles\":{\n")
for i in range(1,101):
    json.write("\t\"Car"+str(i)+"\":{\n")
    json.write("\t\t\"VehicleType\": \"PhysXCar\",\n")
    json.write("\t\t\"X\":"+str(-i*3)+", \"Y\": "+str(i*3+5-1)+",\"Z\": -0.2\n")
    json.write("\t\t\t},\n")
json.write("\t\t\"Car"+str(500)+"\":{\n")
json.write("\t\t\"VehiclecType\": \"PhysXCar\",\n")
json.write("\t\t\"X\":"+str(-1500)+", \"Y\": "+str(1500+5-1)+",\"Z\": -0.2\n")
json.write("\t\t\t}")
json.write("\n\t\t}\n}")
json.close()