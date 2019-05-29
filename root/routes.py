from flask import render_template, flash, redirect, url_for
from root import root
from .forms import LoginForm


@root.route("/")
def home():
    return render_template('home.html', logo_text='Home')


@root.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('root.home'))
    return render_template('login.html', logo_text='Welcome', title='Sign In', form=form)
