from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()


class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={"class":"form-control","id":"from_full_name"}
            )
        )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Your email"
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class":"form-control",
                "placeholder":"Your message"
            }
        )
    )
    # Mỗi class tương ứng đều chỉ có 1 def(function) tương ứng 
    def clean_email(self):  #Kiểm tra lỗi khi input email
        fullname=self.cleaned_data.get("fullname")
        print("cái full name nè ")
        if not "Hungreo" in fullname:
            raise forms.ValidationError("User name cần phải là Hưng rèo")
        email=self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be Gmail")
        return fullname,email
    
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Vui lòng điền tài khoản...."
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Vui lòng điền mật hẩu....",
            }
        )
    )
class RegisterForm(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Vui lòng điền tài khoản...."
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Vui lòng điền mật khẩu...."
            }
        )
    )
    passwordAgain = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Vui lòng điền lại mật khẩu"
            }
        )
    )
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Username is taken')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email is taken')
        return email
    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        passwordAgain = self.cleaned_data.get('passwordAgain')
        if passwordAgain != password:
            raise forms.ValidationError("Xác nhận mật khẩu sai")
        return data