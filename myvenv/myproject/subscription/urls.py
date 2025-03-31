from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = "subscription"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("creditcard/", login_required(views.CreditCardView.as_view()), name="creditcard"),
    path("creditcard/create/", views.CreditCardCreateView.as_view(), name="creditcard_create"),
    path("creditcard/update/<int:pk>/", views.CreditCardUpdateView.as_view(), name="creditcard_update"),
    path("creditcard/delete/<int:pk>/", views.CreditCardDeleteView.as_view(), name="creditcard_delete"),
    path("creditcard/<int:pk>/", login_required(views.CreditCardDetailView.as_view()), name="creditcard_detail"),
    path("creditcard/list/", login_required(views.CreditCardListView.as_view()), name="creditcard_list"),
    path("membership/", login_required(views.MemberShipView.as_view()), name="membership"),
    path("member/create/", views.MemberCreateView.as_view(), name="member_create"),
    path("member/update/<int:pk>/", login_required(views.MemberUpdateView.as_view()), name="membership_update"),
    path("member/cancel/<int:pk>/", views.MemberCancelView.as_view(), name="member_cancel"),
    path("member/<int:pk>/", login_required(views.MemberDetailView.as_view()), name="membership_detail"),
    path("member/list/", login_required(views.MemberListView.as_view()), name="membership_list"),
    path("completion/", views.CompletionView.as_view(), name="completion"),
]