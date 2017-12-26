import json
data='''
[
    {
       "name" : "Chuck",
       "id"   :  "2",
       "x"    :  "3"
    },
    {
       "name" : "Harsh",
       "id"   :  "3",
       "x"    :  "7"
    }
]'''

info=json.loads(data)
for item in info:
    print("Name: ",item["name"])
    print("X: ",item["x"])
    print("ID: ",item["id"])
