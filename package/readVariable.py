def readValue():
    import json
    with open("./gameData.txt") as playerJSONFile:  
        dictionary = json.load(playerJSONFile)

    if ("childLiability" not in dictionary):
        dictionary["childLiability"] = "0"
    if ("REBINFO" not in dictionary):
        dictionary["REBINFO"] = "None"
    if ("stocks_funds_cds" not in dictionary):
        dictionary["stocks_funds_cds"] = "None"
    
    dictionary["childExpenses"] = int(dictionary["numberOfChildren"]) * int(dictionary["perChildExpense"])
    dictionary["childExpenses"] = int(dictionary["childExpenses"]) + int(dictionary["childLiability"])
    dictionary["passiveIncome"] = int(dictionary["interest_dividends"]) + int(dictionary["realEstate_business"])
    dictionary["totalIncome"] = int(dictionary["totalIncome"]) + int(dictionary["passiveIncome"])
    dictionary["totalExpenses"] = int(dictionary["taxes"]) + int(dictionary["homeMortgagePayment"]) + int(dictionary["schoolLoanPayment"]) + int(dictionary["carLoanPayment"]) + int(dictionary["creditCardPayment"]) + int(dictionary["retailPayment"]) + int(dictionary["otherExpenses"]) + int(dictionary["childExpenses"])
    dictionary["monthlyCashFlow"] = int(dictionary["totalIncome"]) - int(dictionary["totalExpenses"])
    variableChoice = input("Please key in the variable:\n")
    try:
        print("The value for entered variable is:\n" + str(dictionary[variableChoice]))
    except:
        print("Variable does not exist. Try again . . . ")
        readValue()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def quickInfo():
    import json
    with open("./gameData.txt") as playerJSONFile:  
        dictionary = json.load(playerJSONFile)

    if ("childLiability" not in dictionary):
        dictionary["childLiability"] = "0"
    if ("REBINFO" not in dictionary):
        dictionary["REBINFO"] = "None"
    if ("stocks_funds_cds" not in dictionary):
        dictionary["stocks_funds_cds"] = "None"

    dictionary["childExpenses"] = int(dictionary["numberOfChildren"]) * int(dictionary["perChildExpense"])
    dictionary["childExpenses"] = int(dictionary["childExpenses"]) + int(dictionary["childLiability"])
    dictionary["passiveIncome"] = int(dictionary["interest_dividends"]) + int(dictionary["realEstate_business"])
    dictionary["totalIncome"] = int(dictionary["totalIncome"]) + int(dictionary["passiveIncome"])
    dictionary["totalExpenses"] = int(dictionary["taxes"]) + int(dictionary["homeMortgagePayment"]) + int(dictionary["schoolLoanPayment"]) + int(dictionary["carLoanPayment"]) + int(dictionary["creditCardPayment"]) + int(dictionary["retailPayment"]) + int(dictionary["otherExpenses"]) + int(dictionary["childExpenses"])
    dictionary["monthlyCashFlow"] = int(dictionary["totalIncome"]) - int(dictionary["totalExpenses"])
    print("Payday: " + str(dictionary["monthlyCashFlow"]))
    print("Passive Income: " + str(dictionary["passiveIncome"]))
    print("Total Expenses: " + str(dictionary["totalExpenses"]))
    print("Real Estate / Business: " + str(dictionary["REBINFO"]))
    print("Stocks: " + str(dictionary["stocks_funds_cds"]))
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def start():
    choice = input("What do you want to do? (Read a variable = 0 | Access quick info = 1):\n")
    if (choice == "0"):
        readValue()
    elif (choice == "1"):
        quickInfo()
    else:
        print("Choice not recognized. Try again . . . ")
        start()

if (__name__ == "__main__"):
    start()