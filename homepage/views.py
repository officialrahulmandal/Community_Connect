# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from os import path
import json
# view for the homepage of Community Connect
def homepage_details(request):
    # redirects to homepage_detail.html template
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "..", "data.json"))
    with open(filepath, 'r') as f:
        community = json.loads(f.read())
    return render(request, 'homepage/homepage_detail.html', {"community": community})
