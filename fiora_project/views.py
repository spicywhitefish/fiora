# Top-level simple views
from django.shortcuts import render_to_response
from django.http import HttpResponseNotAllowed

def register(request):
    if request.method == 'POST':
        return render_to_response('register.html')
    else:
        return HttpResponseNotAllowed()