from django.db import models


class Account(models.Model):
    id = models.CharField('アカウントID', max_length=10, primary_key=True)
    pass_hash = models.CharField('パスワード', max_length=30)
    email_address = models.EmailField('メールアドレス', max_length=30)

    def __str__(self):
        return self.id
