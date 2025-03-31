from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.views.generic import TemplateView, DetailView, ListView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Shop, Category, Reservation, Review, FavoriteShop
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm, ShopForm, CategoryForm, ReservationForm, ReviewForm, FavoriteShopForm
from django.contrib.auth.views import PasswordResetDoneView as BasePasswordResetDoneView
from django.contrib.auth.models import User
from subscription.models import MemberShip
from django.views.generic import TemplateView

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("crud:member_index")


class LoginView(generic.FormView):
    template_name = "registration/login.html"
    form_class = LoginForm
    success_url = reverse_lazy('crud:member_index')

class LogoutView(generic.TemplateView):
    template_name = "registration/logout.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '/')
        return context
    
class PasswordChangeView(generic.FormView):
    template_name = "registration/password_change_form.html"
    form_class = LoginForm
    success_url = reverse_lazy('password_change_done')

class PasswordChangeDoneView(generic.TemplateView):
    template_name = "registration/password_change_done.html"

class PasswordResetView(generic.FormView):
    template_name = "registration/password_reset_form.html"
    form_class = LoginForm
    success_url = reverse_lazy('password_reset_done')

class PasswordResetDoneView(BasePasswordResetDoneView):
    template_name = "registration/password_reset_done.html"
    
class TopView(LoginRequiredMixin, TemplateView):
    template_name = "crud/top.html"

class MypageView(LoginRequiredMixin, generic.TemplateView):
    template_name = "crud/mypage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['membership'] = MemberShip.objects.filter(user=self.request.user).first()
        return context

class MemberIndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = "crud/member_index.html"

class AdminIndexView(LoginRequiredMixin, generic.TemplateView):
    template_name = "admin/admin_index.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('/accounts/login/?next=%s' % request.path)
        return super().dispatch(request, *args, **kwargs)
    
class ShopListView(LoginRequiredMixin, generic.ListView):
    model = Shop
    template_name = "shop/shop_list.html"
    ordering = ["name"]

class ShopDetailView(LoginRequiredMixin, generic.DetailView):
    model = Shop
    template_name = "shop/shop_detail.html"

class ShopCreateView(LoginRequiredMixin, generic.CreateView):
    model = Shop
    template_name = "shop/shop_create.html"
    fields = '__all__'

class ShopUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Shop
    template_name = "shop/shop_update.html"
    fields = '__all__'

class ShopDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Shop
    template_name = "shop/shop_delete.html"
    success_url = "/shop/"

class CategoryListView(LoginRequiredMixin, generic.ListView):
    model = Category
    template_name = "category/category_list.html"
    ordering = ["name"]

class CategoryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Category
    template_name = "category/category_detail.html"

class CategoryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Category
    template_name = "category/category_create.html"
    fields = '__all__'

class CategoryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Category
    template_name = "category/category_update.html"
    fields = '__all__'

class CategoryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Category
    template_name = "category/category_delete.html"
    success_url = "/category/"

class ReviewListView(LoginRequiredMixin, generic.ListView):
    model = Review
    template_name = "review/review_list.html"
    ordering = ["name"]

class ReviewDetailView(LoginRequiredMixin, generic.DetailView):
    model = Review
    template_name = "review/review_detail.html"

class ReviewCreateView(LoginRequiredMixin, generic.CreateView):
    model = Review
    template_name = "review/review_create.html"
    fields = '__all__'

class ReviewUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Review
    template_name = "review/review_update.html"
    fields = '__all__'

class ReviewDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Review
    template_name = "review/review_delete.html"
    success_url = "/review/"


class ReservationListView(generic.ListView):
    model = Reservation
    template_name = "reservation/reservation_list.html"
    ordering = ["name"]

class ReservationDetailView(generic.DetailView):
    model = Reservation
    template_name = "reservation/reservation_detail.html"

class ReservationCreateView(generic.CreateView):
    model = Reservation
    template_name = "reservation/reservation_create.html"
    fields = '__all__'

class ReservationUpdateView(generic.UpdateView):
    model = Reservation
    template_name = "reservation/reservation_update.html"
    fields = '__all__'

class ReservationDeleteView(generic.DeleteView):
    model = Reservation
    template_name = "reservation/reservation_delete.html"
    success_url = "/reservation/"

class FavoriteShopListView(generic.ListView):
    model = FavoriteShop
    template_name = "favorite_shop/favorite_shop_list.html"
    context_object_name = "favorites"

    def get_queryset(self):
        return super().get_queryset().order_by("shop")

class FavoriteShopCreateView(generic.CreateView):
    model = FavoriteShop
    template_name = "favorite_shop/favorite_shop_create.html"
    fields = '__all__'

class FavoriteShopDeleteView(generic.DeleteView):
    model = FavoriteShop
    template_name = "favorite_shop/favorite_shop_delete.html"
    success_url = "/favorite/"

class FavoriteShopDetailView(DetailView):
    model = FavoriteShop
    template_name = "favorite_shop/favorite_shop_detail.html"
    context_object_name = "favorite_shop"

class UserDetailView(DetailView):
    model = User
    template_name = "user/user_detail.html"
    context_object_name = "user_detail"

    success_url = reverse_lazy('crud:user_detail')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_detail'] = self.object
        return context
    
class UserUpdateView(UpdateView):
    model = User
    template_name = "user/user_update.html"
    fields = ['username', 'email', 'first_name', 'last_name']
    success_url = reverse_lazy('crud:user_detail')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.object
        return context
    
class UserDeleteView(DeleteView):
    model = User
    template_name = "user/user_delete.html"
    success_url = reverse_lazy('crud:user_detail')
    context_object_name = "user_detail"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_detail'] = self.object
        return context

class UserCreateView(CreateView):
    model = User
    template_name = "user/user_create.html"
    form_class = SignUpForm
    success_url = reverse_lazy('crud:user_detail')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.object
        return context

class UserCancelView(DeleteView):
    model = User
    template_name = "user/user_confirm_delete.html"
    success_url = reverse_lazy("crud:member_index")
    context_object_name = "user_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_detail'] = self.object
        return context

class UserListView(generic.ListView):
    model = User
    template_name = "user/user_list.html"
    ordering = ["username"]
    context_object_name = "user_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_list'] = self.get_queryset()
        return context

class CompletionView(TemplateView):
    template_name = "subscription/completion.html"
