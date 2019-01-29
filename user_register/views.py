from django.views.generic import FormView
from django.shortcuts import render
from user_register.models import Account
from user_register.forms import AccountForm
from NIIModule.Login import UserRegister


# 入力画面初期表示
# 確認画面で戻るボタン押下時
class AccountDataInput(FormView):
    form_class = AccountForm
    template_name = "user_register/input"

    def form_valid(self, form):
        return render(self.request, 'user_register/input', {'form': form})


# 入力画面で確認ボタン押下時
class AccountDataConf(FormView):
    form_class = AccountForm

    def form_valid(self, form):
        return render(self.request, 'user_register/conf', {'form': form})

    def form_invalid(self, form):
        return render(self.request, 'user_register/input', {'form': form})


# 登録後のリダイレクト先
def comp(request):
    comp_id = request.POST['id']
    comp_pass = request.POST['pass_hash']
    comp_email = request.POST['email_address']
    if UserRegister.user_register(comp_id, comp_pass, comp_email):
        return render(request, 'user_register/comp')
    else:
        form = AccountForm(request.POST)
        return render(request, 'user_register/input', {'form': form})
