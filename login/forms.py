from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    status = (
        ('farmer', "农场主"),
        ('technician', "技术人员"),
        ('marketer', "技术人员"),
    )

    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    identity = forms.ChoiceField(label='身份', choices=status)
    captcha = CaptchaField(label='验证码')


class RegisterForm(forms.Form):

    status = (
        ('farmer', "农场主"),
        ('technician', "技术人员"),
        ('marketer', "市场人员"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    identity = forms.ChoiceField(label='身份', choices=status)
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')

