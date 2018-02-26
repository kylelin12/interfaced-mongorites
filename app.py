from flask import Flask, render_template, redirect, url_for, request, flash
from utils import mongorites

app = Flask(__name__)

@app.route('/')
def root():
    mongorites.main()
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    query_type = request.form["type-select"]

    if request.form["mass"] != "":
        mass = request.form["mass"]

    if request.form["recclass"] != "":
        recclass = request.form["recclass"]

    if query_type == "ltmass":
        results = mongorites.query_ltmass(mass)
    if query_type == "gtmass":
        results = mongorites.query_gtmass(mass)
    if query_type == "mass":
        results = mongorites.query_mass(mass)
    if query_type == "recclass":
        results = mongorites.query_recclass(recclass)
    if query_type == "recclass-mass":
        results = mongorites.query_recclass_mass(recclass, mass)
    
    return render_template('index.html', q_results=results)

if __name__ == '__main__':
    app.debug = True
    app.run()