from flask import Flask,render_template,request,url_for,flash,request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

#EDA Packages
import pandas as pd
import numpy as np

# ML Packages
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

#Chamada de funcao
import preditivoflower as preFlower

app = Flask(__name__)
app.secret_key = 'chave de projeto'

class FlowerForm(Form):
    sepallength = TextField('sepallength:', validators=[validators.required()])
    sepalwidth =  TextField('Sepal Largura:', validators=[validators.required()])
    petalalength = TextField('Petala Comprimento:', validators=[validators.required()])
    petalawidth  = TextField('Petala Altura:', validators=[validators.required()]) 


@app.route("/", methods=['GET', 'POST'])
def flower():	
    form = FlowerForm(request.form)
    #sepallength, sepalwidth, petallength, petalwidth
    msg = "iris_petal_sepal.png"
    
    if request.method == 'POST':
        sepallength = request.form['sepallength']
        sepalwidth = request.form['sepalwidth']
        petalalength = request.form['petalalength']
        petalawidth = request.form['petalawidth']
        msg = preFlower.preditivoFlower(sepallength, sepalwidth, petalalength, petalawidth)          
    
	    
    flash(msg)
    return render_template("flowers.html",form=form)

if __name__ == '__main__':
	app.run(host="127.0.0.1",port=8080,debug=True)