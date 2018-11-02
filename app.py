from AppPack import info
from flask import Flask , render_template
app = Flask(__name__)

profName = info.index[0] #extracts out the profName b4 deletion
del info.index[0]    #deletes the profName

@app.route('/')
@app.route('/info')
def output():
    return render_template('quickInfo.html' , profName=profName , index=info.index)



if (__name__ == '__main__'):
    app.run(debug=True,host='0.0.0.0',port='8000')