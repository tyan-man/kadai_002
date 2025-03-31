from django.shortcuts import render
from django.views.generic import TemplateView
from .models import CreditCard, MemberShip
from django.views import generic
from .forms import CreditCardForm, MemberShipForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

@method_decorator(login_required,name="dispatch")
class HomeView(generic.TemplateView):
    template_name = "subscription/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    
class CreditCardView(LoginRequiredMixin, generic.TemplateView):
    template_name = "subscription/creditcard.html"

class CreditCardCreateView(LoginRequiredMixin, generic.CreateView):
    model = CreditCard
    template_name = "subscription/creditcard_create.html"
    form_class = CreditCardForm
    success_url = reverse_lazy('crud:creditcard')

class CreditCardUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = CreditCard
    template_name = "subscription/creditcard_update.html"
    form_class = CreditCardForm
    success_url = reverse_lazy('crud:creditcard')

class CreditCardDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = CreditCard
    template_name = "subscription/creditcard_delete.html"
    success_url = reverse_lazy('crud:creditcard')

class CreditCardDetailView(LoginRequiredMixin, generic.DetailView):
    model = CreditCard
    template_name = "subscription/creditcard_detail.html"
    context_object_name = "creditcard"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['creditcard'] = self.object
        return context

class CreditCardListView(LoginRequiredMixin, generic.ListView):
    model = CreditCard
    template_name = "subscription/creditcard_list.html"
    context_object_name = "creditcards"

    def get_queryset(self):
        return CreditCard.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['creditcards'] = self.get_queryset()
        return context

class MemberShipView(LoginRequiredMixin, generic.TemplateView):
    template_name = "subscription/membership.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    
class MemberCreateView(TemplateView):
    template_name = "subscription/member_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        creditcard = CreditCard.objects.filter(user=self.request.user).first()
        context['creditcard'] = creditcard
        return context

class MemberUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = MemberShip
    template_name = "subscription/member_update.html"
    form_class = CreditCardForm
    success_url = reverse_lazy('subscription:membership')

class MemberCancelView(LoginRequiredMixin, generic.DeleteView):
    model = MemberShip
    template_name = "subscription/member_cancel.html"
    success_url = reverse_lazy('subscription:membership')

class MemberDetailView(LoginRequiredMixin, generic.DetailView):
    model = MemberShip
    template_name = "subscription/member_detail.html"
    context_object_name = "membership"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['membership'] = self.object
        return context
    
class MemberListView(LoginRequiredMixin, generic.ListView):
    model = MemberShip
    template_name = "subscription/member_list.html"
    context_object_name = "memberships"

class CompletionView(TemplateView):
    template_name = "subscription/completion.html"