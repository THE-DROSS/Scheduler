from django.shortcuts import render
from django.http import HttpResponse
from password_reminder.forms import PasswordReminderForm
from password_reminder.models import PasswordReminder
import secrets

from django.template import RequestContext


# Create your views here.
def reminder(request):
    form = PasswordReminderForm()
    if request.method == 'POST':
        req_email = request.POST['email']
        # TODO DB存在チェック
        # result = filter(email_address="email_address")
        # if result is none:
        #     error_message = "メールアドレスが登録されていません。"
        #     return render(request, 'password_reminder/reminder.tpl',
        #                     {'form': form,
        #                      'error_message': error_message})

        # TODO アカウント情報の取得
        # テストコード 本来はアカウントモデルから取得した値を使用
        account_id = "99999"
        # for account in result: account_id = account.id


        onetime_password = secrets.token_hex()
        try:
            PasswordReminder.create(account_id, onetime_password)
        except:
            error_message = "予期せぬエラーが発生しました。もう一度メールアドレスを送信してください。"
            return render(request, 'password_reminder/reminder.tpl',
                             {'form': form,
                              'error_message': error_message})

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
