from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User, Shop, Category, Reservation, Review, FavoriteShop
from django.utils import timezone


User = get_user_model()

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'username': 'ユーザー名',
            'first_name': '名字',
            'last_name': '名前',
            'email': 'メールアドレス',
            'password1': 'パスワード',
            'password2': 'パスワード確認',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

        def save(self, commit=True):
            user = super().save(commit=False)
            user.username = self.cleaned_data['username']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': 'ユーザー名',
            'password': 'パスワード',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'
        labels = {
            'name': '店舗名',
            'category': 'カテゴリ',
            'description': '詳細',
            'image': '画像',
            'business_day': '営業日',
            'business_hours': '営業時間',
            'postal_code': '郵便番号',
            'address': '住所',
            'phone': '電話番号',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'business_day': forms.TextInput(attrs={'class': 'form-control'}),
            'business_hours': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ReviewForm(forms.Form):
    review = forms.CharField(label='レビュー', widget=forms.Textarea(attrs={'class': 'form-control'}))
    rating = forms.IntegerField(label='評価', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    shop_id = forms.IntegerField(widget=forms.HiddenInput())

class ReservationForm(forms.Form):
    date = forms.DateField(label='日付', widget=forms.DateInput(attrs={'class': 'form-control'}))
    start_time = forms.TimeField(label='開始時間', widget=forms.TimeInput(attrs={'class': 'form-control'}))
    end_time = forms.TimeField(label='終了時間', widget=forms.TimeInput(attrs={'class': 'form-control'}))
    shop_id = forms.IntegerField(widget=forms.HiddenInput())

class SearchForm(forms.Form):
    keyword = forms.CharField(label='キーワード', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.IntegerField(label='カテゴリ', required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    rating = forms.IntegerField(label='評価', required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    start_time = forms.TimeField(label='開始時間', required=False, widget=forms.TimeInput(attrs={'class': 'form-control'}))
    end_time = forms.TimeField(label='終了時間', required=False, widget=forms.TimeInput(attrs={'class': 'form-control'}))
    date = forms.DateField(label='日付', required=False, widget=forms.DateInput(attrs={'class': 'form-control'}))
    business_day = forms.CharField(label='営業日', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    business_hours = forms.CharField(label='営業時間', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    postal_code = forms.CharField(label='郵便番号', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='住所', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='電話番号', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

class CategoryForm(forms.Form):
    name = forms.CharField(label='カテゴリ', widget=forms.TextInput(attrs={'class': 'form-control'}))
    category_id = forms.IntegerField(widget=forms.HiddenInput())

class ShopImageForm(forms.Form):
    image = forms.ImageField(label='画像', widget=forms.FileInput(attrs={'class': 'form-control'}))
    shop_id = forms.IntegerField(widget=forms.HiddenInput())

class FavoriteShopForm(forms.ModelForm):
    created_at = forms.DateTimeField(
        widget=forms.HiddenInput(),
        initial=timezone.now
    )

    class Meta:
        model = FavoriteShop
        fields = '__all__'
        labels = {
            'user': 'ユーザー',
            'shop': '店舗',
        }
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'shop': forms.Select(attrs={'class': 'form-control'}),
        }



