# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from os import path
import json
# importing SignupForm from forms.py
from .forms import SignupForm

# view for signup form
def sign_up(request):
    # if the form is already filled
    if request.method == "POST":
        form = SignupForm(request.POST)
        # and if the data is valid means satisfy all the validators conditions
        if form.is_valid():
            # then we retrive the data input by the user and save into the DB
            post = form.save(commit=False)
            post.save()
            return redirect('homepage_detail')
    elif request.method == "GET":
        # else show the signup_details.html template
        form = SignupForm()
        basepath = path.dirname(__file__)
        filepath = path.abspath(path.join(basepath, "..", "data.json"))
    with open(filepath, 'r') as f:
        community = json.loads(f.read())
    return render(request,'signup/signup_details.html', {'form': form, "community": community})
