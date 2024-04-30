from flask import Flask, render_template

app = Flask(__name__)

def database():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'secret':
            return redirect(url_for('home'))
        else:
            error = 'Invalid credentials. Please try again.'
    return render_template('login.html', error=error)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')





if __name__ == '__main__':
    app.run(debug=True)
