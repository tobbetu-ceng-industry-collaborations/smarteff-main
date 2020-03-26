curl -d "{\"deviceid\":\"$2\", \"personid\":\"$1\", \"until\": \"2020-03-26-17-00-00\"}" -H "Content-Type: application/json" -X POST https://smarteff.herokuapp.com/SuspendAutomation
