from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from .models import CreditCard, MemberShip
from django.views import generic
from django.forms import ModelForm

class CreditCardForm(forms.ModelForm):
    class Meta:
        model = CreditCard
        fields = ['card_number', 'card_name', 'expiration_date', 'security_code']
        labels = {
            'card_number': 'カード番号',
            'card_name': 'カード名義',
            'expiration_date': '有効期限',
            'security_code': 'セキュリティコード',
        }
        widgets = {
            'card_number': forms.TextInput(attrs={'class': 'form-control'}),
            'card_name': forms.TextInput(attrs={'class': 'form-control'}),
            'expiration_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'security_code': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CreditCardUpdateForm(forms.ModelForm):
    class Meta:
        model = CreditCard
        fields = ['card_number', 'card_name', 'expiration_date', 'security_code']
        labels = {
            'card_number': 'カード番号',
            'card_name': 'カード名義',
            'expiration_date': '有効期限',
            'security_code': 'セキュリティコード',
        }
        widgets = {
            'card_number': forms.TextInput(attrs={'class': 'form-control'}),
            'card_name': forms.TextInput(attrs={'class': 'form-control'}),
            'expiration_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'security_code': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CreditCardDeleteForm(forms.ModelForm):
    class Meta:
        model = CreditCard
        fields = ['card_number', 'card_name', 'expiration_date', 'security_code']
        labels = {
            'card_number': 'カード番号',
            'card_name': 'カード名義',
            'expiration_date': '有効期限',
            'security_code': 'セキュリティコード',
        }
        widgets = {
            'card_number': forms.TextInput(attrs={'class': 'form-control'}),
            'card_name': forms.TextInput(attrs={'class': 'form-control'}),
            'expiration_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'security_code': forms.TextInput(attrs={'class': 'form-control'}),
        }

class MemberShipForm(forms.ModelForm):
    class Meta:
        model = MemberShip
        fields = ['user', 'start_date', 'end_date']
        labels = {
            'user': 'ユーザー',
            'start_date': '開始日',
            'end_date': '終了日',
        }

class MemberShipUpdateForm(forms.ModelForm):
    class Meta:
        model = MemberShip
        fields = ['user', 'start_date', 'end_date']
        labels = {
            'user': 'ユーザー',
            'start_date': '開始日',
            'end_date': '終了日',
        }
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class MemberShipCancelForm(forms.ModelForm):
    class Meta:
        model = MemberShip
        fields = ['user', 'start_date', 'end_date']
        labels = {
            'user': 'ユーザー',
            'start_date': '開始日',
            'end_date': '終了日',
        }
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }