mountainHeights = {"Mount Everest":"8,848",
           "K2":"8,611	",
           "Kangchenjunga":"8,586",
           "Lhotse":"8,516",
           " Makalu": "8,485"
           }
x = 0
for key in mountainHeights:
    print(key)
    x = x + 1

for key in mountainHeights:
    print(mountainHeights[key])
    x = x + 1

for key in mountainHeights:
    print(key + " is " + mountainHeights[key] + " feet tall")
    x = x + 1