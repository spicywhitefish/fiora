from forms import UserRegistrationForm, IamaForm
from django.http import HttpResponseNotAllowed
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from django.shortcuts import redirect
from fiora_project.theme import Theme
def iama(request):
    if request.method == 'POST':
        iaf = IamaForm(request.POST)
        # 
        if(iaf.is_valid()):
            context = RequestContext(request)
            gender = iaf.cleaned_data['gender']
            weapon = iaf.cleaned_data['weapon']
            theme = Theme.get_by_values(gender, weapon)
            context['theme'] = theme
            urf = UserRegistrationForm()
            context['urf'] = urf
            return render_to_response('register.html', context)
        else:
            return redirect('home')
    else:
        return HttpResponseNotAllowed('POST requests only')
    
def register(request):
    if request.method == 'POST':
        urf = UserRegistrationForm(request.POST)
        if(urf.is_valid()):
            urf.save()
            return redirect('home')
        else:
            print(urf.errors)
            context = RequestContext(request)
            context['urf'] = urf
            return render_to_response('register.html', context)
            
    else:
        return HttpResponseNotAllowed('POST requests only')