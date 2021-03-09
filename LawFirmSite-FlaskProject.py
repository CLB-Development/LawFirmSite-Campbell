from flask import Flask, render_template, jsonify, redirect, url_for, request

app = Flask(__name__)


@app.route('/')

def Logo():
    return render_template("Logo.html")

