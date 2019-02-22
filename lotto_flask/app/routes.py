from app import app
from flask import redirect, render_template, request, url_for


@app.route('/', methods=["GET"])
def home():
	return render_template('lotto_data_engineering.html', title_bar = 'Lotto Data Cleaning')


@app.route('/quick_lotto_eda.html')
def notebook():
	return render_template('quick_lotto_eda.html', title_bar ='Quick EDA')
