import json

f = open("config.json")
j = json.load(f)
print(j.get('company_name'))