curl  -H "Content-Type: application/json" -X POST -d "{\"personid\":\"$1\", \"event\": \"entry\"}" http://127.0.0.1:5000/HandlePersonEvent