from app import app
from flask import redirect, render_template, request, url_for


@app.route('/', methods=["GET"])
def home():
	return render_template('Lotto_Cleaner2.html', title_bar = 'Lotto Data Cleaning')


@app.route('/Lotto_EDA.html')
def notebook():
	return render_template('Lotto_EDA.html', title_bar ='Lotto EDA')
