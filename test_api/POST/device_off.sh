curl  -H "Content-Type: application/json" -X POST -d "{\"deviceid\":\"$1\", \"event\": \"turnoff\"}" http://127.0.0.1:5000/HandleDeviceEvent