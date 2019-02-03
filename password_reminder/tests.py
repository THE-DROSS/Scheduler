from django.test import TestCase
from password_reminder.models import PasswordReminder
import secrets
import logging


class PasswordReminderModelTests(TestCase):
    def test_create_OK(self):
        account_id = "test_ac_id"
        onetime_password = secrets.token_hex()
        try:
            PasswordReminder.create(account_id, onetime_password)
        except:
            self.fail()

    def test_create_param_null(self):
        account_id = None
        onetime_password = None
        try:
            PasswordReminder.create(account_id, onetime_password)
            self.fail()
        except Exception as e:
            logger = logging.getLogger('development')
            logger.info('登録失敗')
            logger.error('=== エラー内容 ===')
            logger.error('type:' + str(type(e)))
            logger.error('args:' + str(e.args))
            logger.error('message:' + e.message)

    def test_create_account_id_maxlength_exceed(self):
        account_id = "test_ac_id_"
        onetime_password = secrets.token_hex()
        try:
            PasswordReminder.create(account_id, onetime_password)
            self.fail()
        except Exception as e:
            logger = logging.getLogger('development')
            logger.info('登録失敗')
            logger.error('=== エラー内容 ===')
            logger.error('type:' + str(type(e)))
            logger.error('args:' + str(e.args))
            logger.error('message:' + e.message)

    def test_create_onetime_password_maxlength_exceed(self):
        account_id = "test_ac_id_"
        onetime_password = secrets.token_hex() + "1"
        try:
            PasswordReminder.create(account_id, onetime_password)
        except Exception as e:
            self.fail()
