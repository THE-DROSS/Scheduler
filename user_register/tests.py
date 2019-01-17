from django.test import TestCase
from NIIModule.Login.UserRegister import UserRegister


class UserRegisterTests(TestCase):

    # def test_input_validate_OK(self):
    #     userRegister = UserRegister(id="abc001", pass_hash="abc001", email_address="abc001@sample.com")
    #     self.assertIs(userRegister.input_validate(), True)

    def test_regist_OK(self):
