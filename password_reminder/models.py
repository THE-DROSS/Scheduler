from django.db import models


class PasswordReminder(models.Model):
    id = models.IntegerField('パスワードリマインダーID', max_length=10, primary_key=True)
    account_id = models.CharField('アカウントID', max_length=10)
    limit_date = models.DateTimeField('期限')
    onetime_pass_hash = models.CharField('ワンタイムハッシュ', max_length=128)
    delete_flg = models.CharField('削除フラグ', max_length=1)
    register_date = models.DateTimeField('登録日時')
    update_date = models.DateTimeField('更新日時')


def create(self, account_id, onetime_password):
    self.save()
