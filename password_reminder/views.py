from django.shortcuts import render
from django.http import HttpResponse
from password_reminder.forms import PasswordReminderForm
from password_reminder.models import PasswordReminder
from django.core.mail import BadHeaderError, send_mail
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
        account_id = "0123456789"
        # for account in result: account_id = account.id

        onetime_url_param = secrets.token_hex()
        onetime_password = secrets.token_hex()
        try:
            models = PasswordReminder()
            models.save(account_id, onetime_url_param, onetime_password)
        except Exception as e:
            print('type:' + str(type(e)))
            print('args:' + str(e.args))
            error_message = "予期せぬエラーが発生しました。もう一度メールアドレスを送信してください。"
            return render(request, 'password_reminder/reminder.tpl',
                          {'form': form,
                           'error_message': error_message})

        try:
            # メールの送信
            subject = "スケジューラからパスワード再設定用URLをお送りします"
            # REVIEW もう少しきれいな書き方があるはず
            onetime_url = request.build_absolute_uri() + "input/" + onetime_url_param
            message = f"下記URLにアクセスし、画面に表示されたパスワードを入力してください。\n {onetime_url}"
            from_email = "sample@sample.com"
            recipient_list = [
                req_email
            ]
            send_mail(subject, message, from_email, recipient_list)
        except BadHeaderError as e:
            print('type:' + str(type(e)))
            print('args:' + str(e.args))
            error_message = "メールの送信に失敗しました。もう一度メールアドレスを送信してください。"
            return render(request, 'password_reminder/reminder.tpl',
                          {'form': form,
                           'error_message': error_message})

        form = PasswordReminderForm()
        form.email = req_email
        form.password = onetime_password
        return render(request, 'password_reminder/display.tpl', {'form': form})
    else:
        return render(request, 'password_reminder/reminder.tpl', {'form': form})


def input_pass(request, onetime_url_param):
    form = PasswordReminderForm()
    # 有効期間チェック(発行から30分以内)
    if not PasswordReminder.is_available_url(onetime_url_param):
        return render(request, 'password_reminder/expired_url.tpl', {'form': form})

    if request.method == 'POST':
        onetime_password = request.POST['password']
        # TODO ワンタイムパスワード存在チェック

        return render(request, 'password_reminder/setting.tpl', {'form': form})
    else:
        return render(request, 'password_reminder/pass_form.tpl', {'form': form})


def setting(request):
    return HttpResponse("You're voting on question")


def complete(request):
    return HttpResponse("You're voting on question %s.")
