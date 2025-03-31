from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.forms import ModelForm, TextInput, FileInput, Select, Textarea, NumberInput, DateInput, TimeInput
from django.utils import timezone
from django.urls import reverse_lazy
from django.conf import settings
from .models import ShopImage, FavoriteShop, Category, Reservation, Review, Shop
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ユーザー名'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '名字'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '名前'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'メールアドレス'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "ユーザー名"
        self.fields['first_name'].label = "名字"
        self.fields['last_name'].label = "名前"
        self.fields['email'].label = "メールアドレス"
        
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ユーザー名'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '名字'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '名前'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'メールアドレス'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "ユーザー名"
        self.fields['first_name'].label = "名字"
        self.fields['last_name'].label = "名前"
        self.fields['email'].label = "メールアドレス"

class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ユーザー名'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '名字'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '名前'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'メールアドレス'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "ユーザー名"
        self.fields['first_name'].label = "名字"
        self.fields['last_name'].label = "名前"
        self.fields['email'].label = "メールアドレス"

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ユーザー名'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '名字'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '名前'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'メールアドレス'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'パスワード'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'パスワード確認'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "ユーザー名"
        self.fields['first_name'].label = "名字"
        self.fields['last_name'].label = "名前"
        self.fields['email'].label = "メールアドレス"
        self.fields['password1'].label = "パスワード"
        self.fields['password2'].label = "パスワード確認"

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


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'start_time', 'end_time']
        labels = {
            'date': '日付',
            'start_time': '開始時間',
            'end_time': '終了時間',
        }
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

class ReservationUpdateForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'start_time', 'end_time']
        labels = {
            'date': '日付',
            'start_time': '開始時間',
            'end_time': '終了時間',
        }
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

class ReservationDeleteForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'start_time', 'end_time']
        labels = {
            'date': '日付',
            'start_time': '開始時間',
            'end_time': '終了時間',
        }
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']
        labels = {
            'category_name': 'カテゴリ名',
        }
        widgets = {
            'category_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']
        labels = {
            'category_name': 'カテゴリ名',
        }
        widgets = {
            'category_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
class CategoryDeleteForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']
        labels = {
            'category_name': 'カテゴリ名',
        }
        widgets = {
            'category_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review']
        labels = {
            'review': 'レビュー',
        }
        widgets = {
            'review': forms.Textarea(attrs={'class': 'form-control'}),
        }

class ReviewUpdateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review']
        labels = {
            'review': 'レビュー',
        }
        widgets = {
            'review': forms.Textarea(attrs={'class': 'form-control'}),
        }

class ReviewDeleteForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review']
        labels = {
            'review': 'レビュー',
        }
        widgets = {
            'review': forms.Textarea(attrs={'class': 'form-control'}),
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "店舗名"
        self.fields['category'].label = "カテゴリ"
        self.fields['description'].label = "詳細"
        self.fields['image'].label = "画像"
        self.fields['business_day'].label = "営業日"
        self.fields['business_hours'].label = "営業時間"
        self.fields['postal_code'].label = "郵便番号"
        self.fields['address'].label = "住所"
        self.fields['phone'].label = "電話番号"

class ShopUpdateForm(forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "店舗名"
        self.fields['category'].label = "カテゴリ"
        self.fields['description'].label = "詳細"
        self.fields['image'].label = "画像"
        self.fields['business_day'].label = "営業日"
        self.fields['business_hours'].label = "営業時間"
        self.fields['postal_code'].label = "郵便番号"
        self.fields['address'].label = "住所"
        self.fields['phone'].label = "電話番号"

class ShopDeleteForm(forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "店舗名"
        self.fields['category'].label = "カテゴリ"
        self.fields['description'].label = "詳細"
        self.fields['image'].label = "画像"
        self.fields['business_day'].label = "営業日"
        self.fields['business_hours'].label = "営業時間"
        self.fields['postal_code'].label = "郵便番号"
        self.fields['address'].label = "住所"
        self.fields['phone'].label = "電話番号"

class ShopSearchForm(forms.Form):
    keyword = forms.CharField(label='キーワード', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(label='カテゴリ', queryset=Category.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    
class ShopImageForm(forms.ModelForm):
    class Meta:
        model = ShopImage
        fields = [] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['image'].label = "画像"
        self.fields['image'].required = False
        self.fields['image'].widget.attrs.update({'class': 'form-control', 'accept': 'image/*'})

        self.fields['image'].help_text = "画像を選択してください。"
        self.fields['image'].error_messages = {
            'invalid': "無効な画像形式です。JPEG, PNG, GIF形式の画像を選択してください。",
        }

        self.fields['image'].validators = [
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif']),
            validate_image_size,
        ]

def validate_image_size(image):
    max_size = 5 * 1024 * 1024  # 5MB
    if image.size > max_size:
        raise ValidationError(f"画像サイズは{max_size / (1024 * 1024)}MB以下にしてください。")


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].label = "ユーザー"
        self.fields['shop'].label = "店舗"
        self.fields['created_at'].label = "登録日"
        self.fields['created_at'].widget.attrs.update({'class': 'form-control', 'readonly': 'readonly'})
        self.fields['created_at'].initial = timezone.now()
        self.fields['created_at'].widget.attrs.update({'class': 'form-control', 'readonly': 'readonly'})
        self.fields['created_at'].help_text = "登録日は自動的に設定されます。"
        self.fields['created_at'].error_messages = {
            'invalid': "無効な日付形式です。",
        }
        self.fields['created_at'].validators = [
            validate_date_format,
        ]

def validate_date_format(value):
    try:
        timezone.datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f')
    except ValueError:
        raise ValidationError("無効な日付形式です。正しい形式で入力してください。")
    

class FavoriteShopUpdateForm(forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].label = "ユーザー"
        self.fields['shop'].label = "店舗"
        self.fields['created_at'].label = "登録日"
        self.fields['created_at'].widget.attrs.update({'class': 'form-control', 'readonly': 'readonly'})
        self.fields['created_at'].initial = timezone.now()
        self.fields['created_at'].widget.attrs.update({'class': 'form-control', 'readonly': 'readonly'})
        self.fields['created_at'].help_text = "登録日は自動的に設定されます。"
        self.fields['created_at'].error_messages = {
            'invalid': "無効な日付形式です。",
        }
        self.fields['created_at'].validators = [
            validate_date_format,
        ]

class FavoriteShopDeleteForm(forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].label = "ユーザー"
        self.fields['shop'].label = "店舗"
        self.fields['created_at'].label = "登録日"
        self.fields['created_at'].widget.attrs.update({'class': 'form-control', 'readonly': 'readonly'})
        self.fields['created_at'].initial = timezone.now()
        self.fields['created_at'].widget.attrs.update({'class': 'form-control', 'readonly': 'readonly'})
        self.fields['created_at'].help_text = "登録日は自動的に設定されます。"
        self.fields['created_at'].error_messages = {
            'invalid': "無効な日付形式です。",
        }
        self.fields['created_at'].validators = [
            validate_date_format,
        ]

class FavoriteShopCreateForm(forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].label = "ユーザー"
        self.fields['shop'].label = "店舗"
        self.fields['created_at'].label = "登録日"
        self.fields['created_at'].widget.attrs.update({'class': 'form-control', 'readonly': 'readonly'})
        self.fields['created_at'].initial = timezone.now()
        self.fields['created_at'].widget.attrs.update({'class': 'form-control', 'readonly': 'readonly'})
        self.fields['created_at'].help_text = "登録日は自動的に設定されます。"
        self.fields['created_at'].error_messages = {
            'invalid': "無効な日付形式です。",
        }
        self.fields['created_at'].validators = [
            validate_date_format,
        ]
