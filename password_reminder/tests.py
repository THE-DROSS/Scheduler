from django.test import TestCase
from password_reminder.models import PasswordReminder
from django.db import utils
import secrets
import logging


class PasswordReminderModelTests(TestCase):
    def test_save_OK(self):
        account_id = "test_ac_id"
        onetime_url_param = secrets.token_hex()
        onetime_password = secrets.token_hex()
        try:
            models = PasswordReminder()
            models.save(account_id, onetime_url_param, onetime_password)
        except Exception as e:
            logger = logging.getLogger('development')
            logger.info('登録失敗')
            logger.error('=== エラー内容 ===')
            logger.error('type:' + str(type(e)))
            logger.error('args:' + str(e.args))
            self.fail()

    def test_save_account_id_null(self):
        account_id = None
        onetime_url_param = secrets.token_hex()
        onetime_password = secrets.token_hex()
        try:
            models = PasswordReminder()
            models.save(account_id, onetime_url_param, onetime_password)
            self.fail()
        except utils.IntegrityError as e:
            logger = logging.getLogger('development')
            logger.info('登録失敗')
            logger.error('=== エラー内容 ===')
            logger.error('type:' + str(type(e)))
            logger.error('args:' + str(e.args))

    def test_save_onetime_url_param_null(self):
        account_id = "test_ac_id"
        onetime_url_param = None
        onetime_password = secrets.token_hex()
        try:
            models = PasswordReminder()
            models.save(account_id, onetime_url_param, onetime_password)
            self.fail()
        except utils.IntegrityError as e:
            logger = logging.getLogger('development')
            logger.info('登録失敗')
            logger.error('=== エラー内容 ===')
            logger.error('type:' + str(type(e)))
            logger.error('args:' + str(e.args))

    # ハッシュ化する際にエラーになる
    def test_save_onetime_password_null(self):
        account_id = "test_ac_id"
        onetime_url_param = secrets.token_hex()
        onetime_password = None
        try:
            models = PasswordReminder()
            models.save(account_id, onetime_url_param, onetime_password)
            self.fail()
        except AttributeError as e:
            logger = logging.getLogger('development')
            logger.info('登録失敗')
            logger.error('=== エラー内容 ===')
            logger.error('type:' + str(type(e)))
            logger.error('args:' + str(e.args))

    # 文字数を超える場合、最大文字数まで登録される
    def test_save_account_id_maxlength_exceed(self):
        account_id = "test_ac_id" + "1"
        onetime_url_param = secrets.token_hex()
        onetime_password = secrets.token_hex()
        try:
            models = PasswordReminder()
            models.save(account_id, onetime_url_param, onetime_password)
        except Exception as e:
            logger = logging.getLogger('development')
            logger.info('登録失敗')
            logger.error('=== エラー内容 ===')
            logger.error('type:' + str(type(e)))
            logger.error('args:' + str(e.args))
            self.fail()

    # 文字数を超える場合、最大文字数まで登録される
    def test_save_onetime_url_param_maxlength_exceed(self):
        account_id = "test_ac_id"
        onetime_url_param = secrets.token_hex() + "#"
        onetime_password = secrets.token_hex()
        try:
            models = PasswordReminder()
            models.save(account_id, onetime_url_param, onetime_password)
        except Exception as e:
            logger = logging.getLogger('development')
            logger.info('登録失敗')
            logger.error('=== エラー内容 ===')
            logger.error('type:' + str(type(e)))
            logger.error('args:' + str(e.args))
            self.fail()

    # 登録前にハッシュ化するため、DBの文字数を超えない
    def test_save_onetime_password_maxlength_exceed(self):
        account_id = "test_ac_id"
        onetime_url_param = secrets.token_hex()
        onetime_password = secrets.token_hex() + "1"
        try:
            models = PasswordReminder()
            models.save(account_id, onetime_url_param, onetime_password)
        except Exception as e:
            logger = logging.getLogger('development')
            logger.info('登録失敗')
            logger.error('=== エラー内容 ===')
            logger.error('type:' + str(type(e)))
            logger.error('args:' + str(e.args))
            self.fail()
