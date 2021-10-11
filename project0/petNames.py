petDict = {"carl":"dog",
           "sam":"bat",
           "jon":"mouse",
           "garfield":"cat"
           }


x = 0
for key in petDict:
    print(key + " is a " + petDict[key])
    x = x + 1