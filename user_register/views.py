# from django.shortcuts import render

from django.shortcuts import render
from user_register.models import Account

# def input(request, params):
#     param = params
#     return render(request, 'user_register/input', {'param': param})

def input(request):
    return render(request, 'user_register/input')

def conf(request):
    conf_id = request.POST['id']
    conf_pass = request.POST['pass']
    conf_email = request.POST['email']
    request.session['id'] = conf_id
    request.session['pass'] = conf_pass
    request.session['email'] = conf_email
    return render(request, 'user_register/conf', {'id':conf_id, 'pass':conf_pass, 'email':conf_email})

def comp(request):
    comp_id = request.session['id']
    comp_pass = request.session['pass']
    comp_email = request.session['email']
    account = Account(id=comp_id, pass_hash=comp_pass, email_address=comp_email)
    account.save()
    return render(request, 'user_register/comp')
