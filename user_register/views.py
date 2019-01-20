# from django.shortcuts import render

from django.shortcuts import render
from user_register.models import Account

# def input(request, params):
#     param = params
#     return render(request, 'user_register/input', {'param': param})

def input(request):
    return render(request, 'user_register/input')

def conf(request):
    confId = request.POST['id']
    confPass = request.POST['pass']
    confEmail = request.POST['email']
    request.session['id'] = confId
    request.session['pass'] = confPass
    request.session['email'] = confEmail
    return render(request, 'user_register/conf', {'id':confId, 'pass':confPass, 'email':confEmail})

def comp(request):
    compId = request.session['id']
    compPass = request.session['pass']
    compEmail = request.session['email']
    account = Account(id=compId, pass_hash=compPass, email_address=compEmail)
    account.save()
    return render(request, 'user_register/comp')
