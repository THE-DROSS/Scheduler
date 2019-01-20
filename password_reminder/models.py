from django.db import models


class PassWordReminder(models.Model):
    id = models.CharField('パスワードリマインダーID', max_length=10, primary_key=True)
    account_id = models.CharField('アカウントID', max_length=10)
    limit_date = models.DateTimeField('期限')
    onetime_pass_hash = models.CharField('ワンタイムハッシュ', max_length=30)
    delete_flg = models.CharField('削除フラグ', max_length=10)
    register_date = models.DateTimeField('登録日時')
    update_date = models.DateTimeField('更新日時')
