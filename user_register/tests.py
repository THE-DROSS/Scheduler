from django.test import TestCase
from django.utils.crypto import get_random_string
from NIIModule.Login.UserRegister import user_register
from user_register.models import Account


class UserRegisterTests(TestCase):

    def test_regist_OK(self):
        test_id = get_random_string(10)
        test_pass = get_random_string(30)
        test_email = get_random_string(24) + "@aa.bb"
        self.account = Account(id=test_id, pass_hash=test_pass, email_address=test_email)
        success_check = user_register(self.account)
        self.assertEqual(success_check, True)
        q = Account.objects.get(id=test_id)
        self.assertEqual(q.id, test_id)
        self.assertEqual(q.pass_hash, test_pass)
        self.assertEqual(q.email_address, test_email)

    def test_regist_NG_maxlength(self):
        test_id = get_random_string(11)
        test_pass = get_random_string(31)
        test_email = get_random_string(25) + "@aa.bb"
        self.account = Account(id=test_id, pass_hash=test_pass, email_address=test_email)
        success_check = user_register(self.account)
        self.assertEqual(success_check, False)
