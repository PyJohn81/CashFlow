from AppPack import info
from flask import Flask , render_template
app = Flask(__name__)

infoNames = info.quickInfo()
global infoNames2 #infoNames2 is a variable that stores every index in the list with added <h1> tags
for i in range(len(infoNames)): #this loop adds the <h1> tag for every index in the list and appends it to the infoNames2 variable
    if (i == 0): #this excepts the profession data from the list because it will undergo a different process.
        pass
    elif (i == 1): #this creates the first <h1> tag in the infoNames2 variable
        infoNames2 = '<h1>{}</h1>'.format(infoNames[i])
    elif (i > 1): #this appends all the other indexes in the list to infoNames2 after including the <h1> tag
        infoNames2 = infoNames2 + '<h1>{}</h1>'.format(infoNames[i])

profName = infoNames[0] #extracts out the profName
del infoNames[0]    #deletes the profName

@app.route('/')
@app.route('/info')
def output():
    return render_template('quickInfo.html' , profName=profName , infoNames=infoNames)



if (__name__ == '__main__'):
    app.run(debug=True,host='0.0.0.0',port='8000')