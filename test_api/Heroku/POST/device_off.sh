curl  -H "Content-Type: application/json" -X POST -d "{\"deviceid\":\"$1\", \"event\": \"turnoff\"}" https://smarteff.herokuapp.com/HandleDeviceEvent