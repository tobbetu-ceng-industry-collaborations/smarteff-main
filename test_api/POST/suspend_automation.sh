curl -d "{\"deviceid\":\"$2\", \"personid\":\"$1\", \"until\": \"2020-01-03-10-20-11\"}" -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/SuspendAutomation
