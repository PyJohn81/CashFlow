import json
with open("./gameData.txt") as gameDataFile:
    dictionary = json.load(gameDataFile)

# ---------------------------------------------------------------------------------------------------------------------

# string = eval(input("Please key in the syntax:\n"))










# ---------------------------------------------------------------------------------------------------------------------

with open("./gameData.txt","w") as saveToFile:
    json.dump(dictionary,saveToFile)


