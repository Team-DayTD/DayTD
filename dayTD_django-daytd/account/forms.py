from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import *

# 폼 : 폼태그 -> HTML의 태그 -> 프론트단에서 사용자의 입력을 받는 인터페이스
# 장고의 폼 : HTML의 폼 역할, 데이터 베이스에 저장할 내용을 형식, 제약조건
# 성별 추가하고 이름 제외하기
class RegisterForm(forms.Form):
    password = forms.CharField(label='Password', max_length=40,
                                widget=forms.TextInput(attrs={
                                        'class' : 'Ouruser-password'
                                        }))
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    
    birth_year = forms.DateTimeField(label='birthday', widget=forms.SelectDateWidget) 

    class Meta:
        model = User
        fields = ['user_id', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords not matched!')
        return cd['password2']