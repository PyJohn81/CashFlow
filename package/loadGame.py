def newGame():
    import json

    def writeProfessionDefaults():
        profChoice = input("Please key in the name of your profession(in small letters):\n")
        fileName = "./datafiles/" + profChoice + ".txt"

        try:
            with open(fileName) as jsonFile:  
                data = json.load(jsonFile)
            data["profession"] = str(profChoice)
            with open("./gameData.txt","w") as jsonFile2:
                json.dump(data,jsonFile2)
            print("Done. Game profession set to " + profChoice + ".")
        except:
            print("Error: Profession not found.")
            writeProfessionDefaults()



    confirm = input("Are you sure you want to start a new game? This will erase all previous data. ( YES | NO  )\n")

    if (confirm == "YES"):
        writeProfessionDefaults()
    elif (confirm == "NO"):
        print("Process canceled.")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def createProfDatafile():
    import json
    global data
    data = {}

    variables = ["numberOfChildren","monthlyCashFlow","salary","interest_dividends","realEstate_business","passiveIncome","totalIncome","taxes","homeMortgagePayment","schoolLoanPayment","carLoanPayment","creditCardPayment","retailPayment","otherExpenses","childExpenses","perChildExpense","totalExpenses","savings","homeMortgage","schoolLoans","carLoans","creditCards","retailDebt"]
    prof = input("Please key in your profession(small letters):\n")
    filename = "./datafiles/" + prof + ".txt"
    for i in variables:
        data[i] = input("Please key in " + i + ":\n")

    with open(filename,"w") as dataFile:
        json.dump(data , dataFile) 

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def start():
    choice = input("What would you like to do? (Start new game = 0 | Create profession datafile = 1):\n")
    if (choice == "0"):
        newGame()
    elif (choice == "1"):
        createProfDatafile()
    else:
        print("Choice not recognized. Try again . . . ")
        start()

if (__name__ == "__main__"):
    start()