from django.test import TestCase
from password_reminder.models import PasswordReminder
from django.db import utils
import secrets
import logging


class PasswordReminderModelSaveTests(TestCase):
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


class PasswordReminderModelIsAvailableUrlTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        from datetime import datetime, timedelta

        now = datetime.now()
        delta = timedelta(minutes=1)
        future = now + delta
        past = now - delta

        # 有効期限:未来, 削除フラグ:未削除
        PasswordReminder.objects.create(
            account_id="1234567890",
            limit_date=future,
            onetime_url_param="future_no_deleted",
            onetime_pass_hash="1",
            delete_flg="0",
            register_date=now,
            update_date=now
        )

        # 有効期限:過去, 削除フラグ:未削除
        PasswordReminder.objects.create(
            account_id="1234567890",
            limit_date=past,
            onetime_url_param="past_no_deleted",
            onetime_pass_hash="1",
            delete_flg="0",
            register_date=now,
            update_date=now
        )

        # 有効期限:未来, 削除フラグ:削除
        PasswordReminder.objects.create(
            account_id="1234567890",
            limit_date=future,
            onetime_url_param="future_deleted",
            onetime_pass_hash="1",
            delete_flg="1",
            register_date=now,
            update_date=now
        )

        # 有効期限:過去, 削除フラグ:削除
        PasswordReminder.objects.create(
            account_id="1234567890",
            limit_date=past,
            onetime_url_param="past_deleted",
            onetime_pass_hash="1",
            delete_flg="1",
            register_date=now,
            update_date=now
        )

    def test_is_available_url_not_exist_onetime_url_param(self):
        self.assertFalse(PasswordReminder.is_available_url("no_data"))

    def test_is_available_url_future_no_deleted(self):
        self.assertTrue(PasswordReminder.is_available_url("future_no_deleted"))

    def test_is_available_url_past_no_deleted(self):
        self.assertFalse(PasswordReminder.is_available_url("past_no_deleted"))

    def test_is_available_url_future_deleted(self):
        self.assertFalse(PasswordReminder.is_available_url("future_deleted"))

    def test_is_available_url_past_deleted(self):
        self.assertFalse(PasswordReminder.is_available_url("past_deleted"))
