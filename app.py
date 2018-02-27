from flask import Flask, render_template, redirect, url_for, request, flash
from utils import mongorites

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    query_type = request.form["type-select"]

    if request.form["mass"] != "":
        mass = int(request.form["mass"])

    if request.form["recclass"] != "":
        recclass = request.form["recclass"]

    print("query type: " + query_type)
    
    if query_type == "ltmass":
        print("ltmass")
        results = mongorites.query_ltmass(mass)
    elif query_type == "gtmass":
        results = mongorites.query_gtmass(mass)
    elif query_type == "mass":
        results = mongorites.query_mass(mass)
    elif query_type == "recclass":
        results = mongorites.query_recclass(recclass)
    elif query_type == "recclass-mass":
        results = mongorites.query_recclass_mass(recclass, mass)
    
    return render_template('index.html', q_results=results)

if __name__ == '__main__':
    mongorites.main()
    app.debug = True
    app.run()