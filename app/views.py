from flask import render_template, redirect, url_for, request
from app import app
from .forms import URLForm
from redis import StrictRedis

r = StrictRedis()

@app.errorhandler(404)
def not_found_error():
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server():
    return render_template('500.html'), 500

def b64encode(i):
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+!'
    result = ''
    while i >= 63:
        result = digits[i % 64] + result
        i = i // 64
    result = digits[i] + result
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        counter = r.incr("counter")
        idcode = b64encode(counter)
        r.set(idcode, request.form['url'])
        url = url_for('index', _external=True) + idcode

        return render_template('index.html', form= form, url = url)
    return render_template('index.html', form = form)

@app.route('/<_id>')
def raw(_id):
    url = r.get(_id)
    return redirect(url)
