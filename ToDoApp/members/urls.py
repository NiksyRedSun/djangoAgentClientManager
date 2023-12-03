from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('member', views.post_user_profile, name='postmember'),
]