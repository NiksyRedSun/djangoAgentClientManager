from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('member', views.post_member, name='post_member'),
    path('member/<int:id>', views.get_delete_put_member, name='get_delete_put_member'),
    path('clients', views.get_all_clients, name='get_all_clients'),
    path('client', views.post_client, name='post_client'),
    path('client/<int:id>', views.get_delete_put_client, name='get_delete_put'),


]