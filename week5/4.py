# Python JSON parsing
# Exercises to parse json data in python
# Exercise 1
# Using data file sample-data.json, create output that resembles the following by parsing the included JSON file.

import json

with open('sample-data.json', 'r') as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU'}")
print("-" * 80)

for item in data['imdata']:
    attr = item['l1PhysIf']['attributes']
    print(f"{attr['dn']:<50} {attr.get('descr',''):<20} {attr['speed']:<8} {attr['mtu']}")