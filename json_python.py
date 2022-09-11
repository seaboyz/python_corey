import json
from textwrap import indent

""" people_string = '''
{
		"people": [
				{
						"name": "John Smith",
						"phone": "615-555-7164",
						"emails": ["john@email.com", ""],
						"has_license": false
				},  
				{
						"name": "Jane Doe",
						"phone": "560-555-5153",   
						"emails": null,
						"has_license": true
				}
		]
}
'''

data = json.loads(people_string)
print(data['people'])

for person in data['people']:
		del person['phone']

new_string = json.dumps(data,indent=2,sort_keys=True)

print(new_string)
 """
""" 
with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    del state['area_codes']

with open('new_states.json','w') as f:
	json.dump(data,f,indent=2) 
"""

import json
from urllib.request import urlopen

with urlopen("https://alpha-vantage.p.rapidapi.com/query") as response:
	source = response.read()

# print(source)

data = json.loads(source)

# print(json.dumps(data,indent=2))
