from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Shop, Category, Reservation, Review, FavoriteShop
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm, ShopForm, CategoryForm, ReservationForm, ReviewForm, FavoriteShopForm

class SignUpView(CreateView):
    template_name = "resistration/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy('login')

class LoginView(generic.FormView):
    template_name = "registration/login.html"
    form_class = LoginForm
    success_url = reverse_lazy('top')

class LogoutView(generic.TemplateView):
    template_name = "registration/logout.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '/')
        return context
    
class TopView(generic.TemplateView):
    template_name = "top.html"

class MypageView(generic.TemplateView):
    template_name = "crud/mypage.html"

class MemberIndexView(generic.TemplateView):
    template_name = "crud/member_index.html"

class AdminIndexView(generic.TemplateView):
    template_name = "admin_index.html"

class ShopListView(generic.ListView):
    model = Shop
    template_name = "shop_list.html"
    ordering = ["name"]

class ShopDetailView(generic.DetailView):
    model = Shop
    template_name = "shop_detail.html"

class ShopCreateView(generic.CreateView):
    model = Shop
    template_name = "shop_create.html"
    fields = '__all__'

class ShopUpdateView(generic.UpdateView):
    model = Shop
    template_name = "shop_update.html"
    fields = '__all__'

class ShopDeleteView(generic.DeleteView):
    model = Shop
    template_name = "shop_delete.html"
    success_url = "/shop/"

class CategoryListView(generic.ListView):
    model = Category
    template_name = "category_list.html"
    ordering = ["name"]

class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = "category_detail.html"

class CategoryCreateView(generic.CreateView):
    model = Category
    template_name = "category_create.html"
    fields = '__all__'

class CategoryUpdateView(generic.UpdateView):
    model = Category
    template_name = "category_update.html"
    fields = '__all__'

class CategoryDeleteView(generic.DeleteView):
    model = Category
    template_name = "category_delete.html"
    success_url = "/category/"

class ReviewListView(generic.ListView):
    model = Review
    template_name = "review_list.html"
    ordering = ["name"]

class ReviewDetailView(generic.DetailView):
    model = Review
    template_name = "review_detail.html"

class ReviewCreateView(generic.CreateView):
    model = Review
    template_name = "review_create.html"
    fields = '__all__'

class ReviewUpdateView(generic.UpdateView):
    model = Review
    template_name = "review_update.html"
    fields = '__all__'

class ReviewDeleteView(generic.DeleteView):
    model = Review
    template_name = "review_delete.html"
    success_url = "/review/"


class ReservationListView(generic.ListView):
    model = Reservation
    template_name = "reservation_list.html"
    ordering = ["name"]

class ReservationDetailView(generic.DetailView):
    model = Reservation
    template_name = "reservation_detail.html"

class ReservationCreateView(generic.CreateView):
    model = Reservation
    template_name = "reservation_create.html"
    fields = '__all__'

class ReservationUpdateView(generic.UpdateView):
    model = Reservation
    template_name = "reservation_update.html"
    fields = '__all__'

class ReservationDeleteView(generic.DeleteView):
    model = Reservation
    template_name = "reservation_delete.html"
    success_url = "/reservation/"

class FavoriteShopListView(generic.ListView):
    model = FavoriteShop
    template_name = "favorite_list.html"
    ordering = ["name"]

class FavoriteShopCreateView(generic.CreateView):
    model = FavoriteShop
    template_name = "favorite_create.html"
    fields = '__all__'

class FavoriteShopDeleteView(generic.DeleteView):
    model = FavoriteShop
    template_name = "favorite_delete.html"
    success_url = "/favorite/"

class AdminIndexView(generic.TemplateView):
    template_name = "admin_index.html"

