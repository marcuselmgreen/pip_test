import json

# JSON object
x = '[{"Name": "Marcus", "Age": 22, "cpr": "1234567890"}, {"Name": "Marcus", "Age": 22, "cpr": "1234567890"}]'

y = json.loads(x)

print(y)