def newEvent():
    import json    
    with open("./gameData.txt") as playerJSONFile:  
        dictionary = json.load(playerJSONFile)

    if ("childLiability" in dictionary):
        pass
    else:
        dictionary["childLiability"] = 0

    variableName = input("Please choose variable (interest_dividends|realEstate_business|newChild|stocks_funds_cds|REBINFO|childLiability):\n")

    if (variableName == "newChild"):
        if (dictionary["numberOfChildren"] == "3" or dictionary["numberOfChildren"] == 3):
            print("Warning: Number of children exceeds limit!")
        else:
            dictionary["numberOfChildren"] = int(dictionary["numberOfChildren"]) + 1
            print("Total number of children now: " + str(dictionary["numberOfChildren"]))
    elif(variableName == "stocks_funds_cds"):
        newStocksList = input("Please key in the info about stocks/funds/cds as a list in the format: [NAME,#ofSHARES,COSTperSHARE]\n")
        if ("stocks_funds_cds" in dictionary):
            dictionary["stocks_funds_cds"] = dictionary["stocks_funds_cds"] + newStocksList
        else:
            dictionary["stocks_funds_cds"] = newStocksList
        print("Every stocks_funds_cds now: " + str(dictionary["stocks_funds_cds"]))
    elif (variableName == "REBINFO"):
        newREBList = input("Please key in the info about real estate / business as a list in the format: [nameOfREB,DownPay,Cost,Mortgage_Liability,CashFlow]\n")
        if ("REBINFO" in dictionary):
            dictionary["REBINFO"] = dictionary["REBINFO"] + newREBList
        else:
            dictionary["REBINFO"] = newREBList
        print("Every REBINFO now: " + str(dictionary["REBINFO"]))
    else:
        newValue = input("Please key in value for " + variableName + ":\n")
        dictionary[variableName] = int(dictionary[variableName]) + int(newValue)
        print("New value of " + str(variableName) + ": " + str(dictionary[variableName]))
        
    with open('./gameData.txt', 'w') as outfile:  
        json.dump(dictionary, outfile)

    print("Done.")

# ---------------------------------------------------------------------------------------------------------------------

def rm():
    import json
    with open("./gameData.txt") as gameDataFile:
        dictionary = json.load(gameDataFile)

    print("Welcome to MANUAL TERMINAL. Be careful. Data loss may occur here.")
    def resume():
        print("Current value:" , dictionary[variable])
        newValue = input("Please key in the new value for the variable:\n")
        dictionary[variable] = (newValue)
        print("New value of " + str(variable) + ": " + str(dictionary[variable]))
        print("Done.")

        with open("./gameData.txt","w") as saveToFile:
            json.dump(dictionary,saveToFile)
    
    def setVarValue():
        global variable
        variable = input("Please key in the variable:\n")
        if (variable in dictionary):
            resume()
        else:
            print("Variable does not exist. Try again . . . ")
            setVarValue()    
    
    setVarValue()
    
# ---------------------------------------------------------------------------------------------------------------------

def start():
    choice = input("What would you like to do? (Enter new event = 0 | Manually remove a value from a variable = 1):\n")
    if (choice == "0"):
        newEvent()
    elif (choice == "1"):
        rm()
    else:
        print("Choice not recognised. Try again . . . ")
        start()

if (__name__ == "__main__"):
    start()
