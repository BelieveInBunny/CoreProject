from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm["CustomUser"]):
    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm["CustomUser"]):
    class Meta:
        model = CustomUser
        fields = ("email",)

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Email / Username",
        widget=forms.TextInput(attrs={
            "autofocus": True,
            "placeholder": "sora_amamiya@coreproject.moe / soraamamiya#0001",
            "class": "h-12 w-full rounded-xl border-[0.4vw] border-primary-500 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]",
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder":"enter your existing password",
            "class":"h-12 w-full rounded-xl border-[0.4vw] border-primary-500 bg-transparent pl-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:pl-[1vw] md:text-[1.1vw]"
        })
    )