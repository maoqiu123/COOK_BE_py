# Create your views here.
from django.views.generic.base import View
from utils.ResponseTool import response, response_form

from .forms import RegisterForm, LoginForm
from .service import check_email, register


class UserView(View):
    def get(self, request):
        pass

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            code = check_email(request.POST.get("email", ""))
            if code == 101:
                return response(101, "邮箱已存在", None)
            register(request)
            return response(1000, "注册成功", None)
        else:
            return response_form(1001, register_form.errors, None)


class LoginView(View):
    def get(self):
        pass

    def post(self, request):
        print(self)
        login_form = LoginForm(request.POST)





