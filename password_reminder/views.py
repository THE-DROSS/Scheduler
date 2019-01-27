from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from password_reminder.forms import PasswordReminderForm
import secrets

from django.template import RequestContext
from password_reminder.models import PassWordReminder


# Create your views here.
def reminder(request):
    form = PasswordReminderForm()
    if request.method == 'POST':
        req_email = request.POST['email']
        # TODO DB存在チェック
        # result = search(req_email)
        # if result is none:
        #     error_message = "メールアドレスが登録されていません。"
        #     return render(request, 'password_reminder/reminder.tpl',
        #                     {'form': form,
        #                      'error_message': error_message})

        # ワンタイムパスワードの生成
        onetime_password = secrets.token_hex()

        # TODO DB登録
        # create()

        # TODO メールの送信
        # send_password_reminder_email(req_email)

        form = PasswordReminderForm()
        form.email = req_email
        form.password = onetime_password
        return render(request, 'password_reminder/display.tpl', {'form': form})
    else:
        return render(request, 'password_reminder/reminder.tpl', {'form': form})


def input_pass(request):
    response = "You're looking at the results of question."
    return HttpResponse(response)


def setting(request):
    return HttpResponse("You're voting on question")


def complete(request):
    return HttpResponse("You're voting on question %s.")
