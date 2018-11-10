from AppPack import info
from flask import Flask , render_template , url_for , flash , redirect
from forms import RegistrationForm  , LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'e976d98a104d9186edffa0bbb37aa4c7'

profName = info.index[0] #extracts out the profName b4 deletion
del info.index[0]    #deletes the profName

@app.route('/')
@app.route('/info')
def output():
    return render_template('quickInfo.html' , profName=profName , index=info.index)

@app.route('/register' , methods=['GET' , 'POST'])
def register():
    form = RegistrationForm()
    if (form.validate_on_submit()):
        flash(f'Account created for {form.username.data}!' , 'success')
        return redirect(url_for('/'))
    return render_template('register.html' , title='Register' , form=form)

@app.route('/login')
def login():
    form =  LoginForm()
    return render_template('login.html' , title='Login' , form=form)

if (__name__ == '__main__'):
    app.run(debug=True,host='0.0.0.0',port='8000')