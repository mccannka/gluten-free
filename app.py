#!/usr/bin/python
# -*- coding: utf-8 -*-
# -------- Config --------------#

import os
from flask import Flask, flash, render_template, redirect, request, \
    session, url_for

from flask_pymongo import PyMongo
from bson.objectid import objectid
from functools import wraps
from werkzeug.security import generate_password_hash, \
    check_password_hash
if os.path.exists('env.py'):
    import env  # noqa: F401


# -------- Homepage / Index --------------#

@app.route('/')
def index():
    return render_template('index.html')


# -------- About page --------------#

@app.route('/about')
def index():
    return render_template('about.html')
