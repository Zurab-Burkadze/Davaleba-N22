from flask import Flask, render_template, redirect, url_for, request, session
from datetime import timedelta


app = Flask(__name__)
app.secret_key = '42645645dgaqfadtqt'



app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)


users = {
    "user1": "password1",
    "user2": "password2"
}


@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('home'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session.permanent = True
            session['username'] = username
            return redirect(url_for('home'))
        else:
            error = 'Invalid username or password'
    return render_template('login.html', error=error)


@app.route('/home')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index.html', username=session['username'])


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)

#mas googles didad ara amar ufro slaidebs da sanis vtxove daxmareba