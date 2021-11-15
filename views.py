from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, 'views')

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/generic')
def get_generic():
    return render_template("generic.html")

@views.route('/elements')
def get_elements():
    return render_template("elements.html")