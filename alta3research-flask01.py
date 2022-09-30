#!/usr/bin/env python3
"""Flask Application Project
-post boba orders
-get orders and using jinja to render in html"""

## import all of the methods, classes, and variables needed for the app
from flask import Flask, render_template, url_for, redirect, jsonify, request

## create the app using the Flask class
app= Flask(__name__)

## this is an empty list of dictionaries
boba = []

## route for the homepage. it renders the html using info from boba
@app.route("/")
def index():
   return render_template("boba.html", orders = boba)

## route for the post request from the form
@app.route("/bobaorders", methods=["GET","POST"])
def adddrink():
   # if the user sends a POST request then take the information on the form and append it to the boba list
   if request.method == 'POST':
      name = request.form.get("name")
      drink = request.form.get("drink")
      size = request.form.get("size")
      sugar = request.form.get("sugar")
      ice = request.form.get("ice")
      toppings = request.form.get("toppings")
      boba.append({ "name": name, "drink": drink, "size": size, "sugar": sugar, "ice": ice, "toppings": toppings })
      # displays the updated information after the form submission
      return render_template("boba.html", orders = boba)
   # if the user sends a GET then go back to home page 
   if request.method == "GET": 
        return redirect(url_for("index"))

## route to show the json of all the orders
@app.route("/allorders")
def allorders():
   # if there are no orders tell the user to add one, other wise return json version of boba list
   if not boba:
      return jsonify("please enter an order")
   else:
      return jsonify(boba)

## run the main function on port 2224
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
