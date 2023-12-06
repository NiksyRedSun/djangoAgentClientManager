from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('agent', views.post_agent, name='post_agent'),
    path('agent/<int:id>', views.get_delete_put_agent, name='get_delete_put_agent'),
    path('clients', views.get_all_clients, name='get_all_clients'),
    path('client', views.post_client, name='post_client'),
    path('client/<int:id>', views.get_delete_put_client, name='get_delete_put_client'),


]