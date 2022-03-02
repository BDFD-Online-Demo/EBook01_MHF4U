'''
Author: BDFD
Date: 2022-02-03 15:32:30
LastEditTime: 2022-03-02 17:57:43
LastEditors: BDFD
Description: 
FilePath: \3.4-E-book_Template-Python_Heroku_Deploy\server.py
'''
# from crypt import methods
# from pickle import TRUE
# from unittest import result
# from uuid import RESERVED_FUTURE
from flask import Flask, render_template, request, redirect, url_for, flash
from Component.forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY']= 'bdfd2005'

@app.route('/')
def index():
  return render_template('intro_page.html')

@app.route('/Chapter1')
def Chapter1():
  return render_template('c01/index.html')

@app.route('/Chapter1/01')
def Chapter1_1():
  return render_template('c01/s01.html')

@app.route('/Chapter1/02')
def Chapter1_2():
  return render_template('c01/s02.html')

@app.route('/Chapter2')
def Chapter2():
  return render_template('c02/index.html')

@app.route('/Chapter2/01')
def Chapter2_1():
  return render_template('c02/s01.html')

@app.route('/Chapter2/02')
def Chapter2_2():
  return render_template('c02/s02.html')

if __name__ == '__main__':
  app.run()
