from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

messages = [{'technique': 'T0000',
             'cloud': 'AWS',
             'detection': 'none',
             'emulation': 'none'}
            ]

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        technique = request.form['technique']
        cloud = request.form['cloud']

        if not technique:
            flash('Technique ID is required!')
        elif not cloud:
            flash('Cloud provider is required!')
        else:
            messages.append({'technique': technique, 'cloud': cloud, 'emulation': request.form['emulation'], 'detection': request.form['detection']})
            return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/')
def index():
    return render_template('index.html', messages=messages)