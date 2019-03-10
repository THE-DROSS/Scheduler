from django.db import models
from datetime import datetime, timedelta
import hashlib


class PasswordReminder(models.Model):
    id = models.IntegerField('パスワードリマインダーID', primary_key=True)
    account_id = models.CharField('アカウントID', max_length=10)
    limit_date = models.DateTimeField('期限')
    onetime_url_param = models.CharField('一時URL用パラメータ', max_length=64)
    onetime_pass_hash = models.CharField('ワンタイムハッシュ', max_length=128)
    delete_flg = models.CharField('削除フラグ', max_length=1)
    register_date = models.DateTimeField('登録日時')
    update_date = models.DateTimeField('更新日時')

    def save(self, account_id, onetime_url_param, onetime_password):
        # 期限, 登録日時, 更新日時に使用
        now = datetime.now()

        self.account_id = account_id

        delta = timedelta(minutes=30)
        self.limit_date = now + delta

        self.onetime_url_param = onetime_url_param
        self.onetime_pass_hash = hashlib.sha512(onetime_password.encode('utf-8')).hexdigest()
        self.delete_flg = "0"  # 未削除
        self.register_date = now
        self.update_date = now

        super(PasswordReminder, self).save()

    @classmethod
    def is_available_url(cls, onetime_url_param):
        cnt = cls.objects.filter(onetime_url_param=onetime_url_param,
                                 limit_date__gt=datetime.now(),
                                 delete_flg="0"
                                 ).count()
        return cnt > 0

    @classmethod
    def is_available_password(cls, onetime_url_param, onetime_password):
        onetime_pass_hash = hashlib.sha512(onetime_password.encode('utf-8')).hexdigest()

        cnt = cls.objects.filter(onetime_url_param=onetime_url_param,
                                 onetime_pass_hash=onetime_pass_hash,
                                 limit_date__gt=datetime.now(),
                                 delete_flg="0"
                                 ).count()
        return cnt > 0
