# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 09:44:45 2019

@author: amand
"""
#
#from flask import Flask
#
#app = Flask("MyApp")
#
#@app.route("/")
#
#def hello():
#    return '<strong> Hello, this is the home page. </strong><a href="/contactus">Contact Us<a>'
#
#@app.route("/anotherpage")
#
#def text():
#    return "<h1> FLASK </h1><p>Today we are learning about flask.</p>"
#
#@app.route("/maths")
#
#def sum():
#    x = 1+2
#    return str(x)
#
#@app.route("/contactus")
#
#def contactdetails():
#    return "<p>Not today please.</p>"
#
#app.run(debug=True)

from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")

def hello():
    return "Hello World"

@app.route("/contactus")

def contactdetails():
    return "<p>Not today please.</p>"

@app.route("/<name>")

def hello_someone(name):
    return render_template("hello.html", name=name.title())

@app.route("/food/<food>")

def lunch(food):
    return render_template("lunch.html", food=food)

@app.route("/game")

def game():
    return render_template("game.html")

@app.route("/html")

def text():
    return render_template("index.html")

@app.route("/confirmation", methods=["POST"])

def confirmation():
    form_data = request.form
    result="All OK"
    email = form_data["email"]
    print (form_data["email"])
    return render_template("confirmation.html", title="Form confirmation", **locals())

app.run(debug=True)