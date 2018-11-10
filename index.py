def main():

    from package import readVariable , events , loadGame

    def start():
        action = input("What would you like to do? \n(Access quick info = 0/info | Enter new event = event | Manually change or remove variable value = change/remove | View variable value = view/read | Start new game = new | Create profession datafile = prof | Access superuser terminal = terminal):\n")

        if (action == "0" or action == "info"):
            readVariable.quickInfo()
        elif (action == "event"):
            events.newEvent()
        elif (action == "change" or action == "remove"):
            events.rm()  
        elif (action == "view" or action == "read"):
            readVariable.readValue()
        elif (action == "new"):
            loadGame.newGame()
        elif (action == "prof"):
            loadGame.createProfDatafile()
        elif (action == "terminal"):
            print("Warning: Run terminal.py manually")
        else:
            print("Choice not recognised. Try again . . . ")
            start()
    
    start()
    try:
        with open('app.py') as openRead:
            readApp = openRead.read()
        with open('app.py' , 'w') as openWrite:
            openWrite.write(readApp)
        print("Detected: In FlaskUI directory. Changes updated to FlaskUI. . .")
    except:
        print("Detected: Not in FlaskUI directory.")

if (__name__ == '__main__'):
    main()