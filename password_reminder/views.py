from django.shortcuts import render
from django.http import HttpResponse
from password_reminder.forms import PasswordReminderForm
from django.template import RequestContext
from password_reminder.models import PassWordReminder


# Create your views here.
def reminder(request):
    form = PasswordReminderForm()
    return render(request, 'password_reminder/reminder.tpl', {'form': form})


def display(request):
    req_email = request.POST['email']

    # バリデーション
    # validate(req_email)

    # ワンタイムパスワードの生成
    # onetime_password = create_onetime_password()

    # メールの送信
    # send_password_reminder_email(req_email)

    form = PasswordReminderForm()
    form.email = req_email
    form.password = 'onetime_password'
    return render(request, 'password_reminder/display.tpl', {'form': form})


def input_pass(request):
    response = "You're looking at the results of question."
    return HttpResponse(response)


def setting(request):
    return HttpResponse("You're voting on question")


def complete(request):
    return HttpResponse("You're voting on question %s.")
