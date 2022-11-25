from flask import Flask, render_template, request, url_for, flash, redirect
import os
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'future work'

techniques_path = "./techniques"

def techniques_from_files():
    # Read the technique json files and populate the website with them
    techniques = []
    json_techniques = [pos_json for pos_json in os.listdir(techniques_path) if pos_json.endswith('.json')]
    for json_technique in json_techniques:
        with open(techniques_path + "/" + json_technique) as file:
            techniques.append(json.load(file))
    return techniques




messages = techniques_from_files()
                
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
            with open(techniques_path + "/" + technique + "_" + cloud + ".json", "w") as file:
                technique_dict = {'technique': technique, 'cloud': cloud, 'emulation': request.form['emulation'], 'detection': request.form['detection']}
                json.dump(technique_dict, file, indent=4, sort_keys=True) 
            #messages.append({'technique': technique, 'cloud': cloud, 'emulation': request.form['emulation'], 'detection': request.form['detection']})
            return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/')
def index():
    return render_template('index.html', messages=techniques_from_files())