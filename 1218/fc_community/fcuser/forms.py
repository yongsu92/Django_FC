from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required':'아이디를 입력해주세요.'
        },
        max_length=32,label="사용자 이름")
    password = forms.CharField(
        error_messages={
            'required':'비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput,label="비밀번호")

    def clean(self):
        # Form안에 들어있는 clean 함수를 먼저 호출해 준다.
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        
        if username and password:
            fcuser_username = Fcuser.objects.filter(username=username)
            if not fcuser_username:
                self.add_error('username','존재하지 않는 아이디입니다.')
            else:
                fcuser = Fcuser.objects.get(username=username)
                if not check_password(password,fcuser.password):
                    self.add_error('password','비밀번호를 틀렸습니다.')
                else:
                    self.user_id = fcuser.id

