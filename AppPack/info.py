
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
    infoNames = [str(dictionary["profession"]).upper() , "Payday: {}".format(str(dictionary["monthlyCashFlow"])) , "Passive Income: {}".format(str(dictionary["passiveIncome"])) , "Total Expenses: {}".format(str(dictionary["totalExpenses"])) , "Real Estate / Business: {}".format(str(dictionary["REBINFO"])) , "Stocks / Funds / CDs: {}".format(str(dictionary["stocks_funds_cds"])) , "Number of children: {}".format(str(dictionary["numberOfChildren"]))]
    # print("Payday: " + str(dictionary["monthlyCashFlow"]))
    # print("Passive Income: " + str(dictionary["passiveIncome"]))
    # print("Total Expenses: " + str(dictionary["totalExpenses"]))
    # print("Real Estate / Business: " + str(dictionary["REBINFO"]))
    # print("Stocks: " + str(dictionary["stocks_funds_cds"]))
    return infoNames