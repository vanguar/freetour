from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<str:slug>/', views.post_detail, name='post_detail'),
    path('subscription/', views.subscription, name='subscription'),


]

