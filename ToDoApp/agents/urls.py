from django.urls import path
from . import views


urlpatterns = [


    path('', views.index, name='get_agents'),
    path('agent', views.post_agent, name='post_agent'),
    path('agent/<int:id>', views.get_delete_put_agent, name='get_delete_put_agent'),


    path('clients', views.get_all_clients, name='get_all_clients'),
    path('client', views.post_client, name='post_client'),
    path('client/<int:id>', views.get_delete_put_client, name='get_delete_put_client'),


    path('events', views.get_all_events, name='get_all_events'),
    path('event', views.post_event, name='post_event'),
    path('event/<int:id>', views.get_delete_put_event, name='get_delete_put_event'),

    path('attempt', views.attempt, name='attempt'),

    path('newagent', views.new_agent, name='new_agent'),
    path('newclient', views.new_client, name='new_client'),


    path('getallevs', views.get_all_events_for_agent, name='getallevs'),
    path('getuncoverev', views.get_uncovering_event, name='getuncoverev'),
    path('getallactive', views.get_all_active_agents, name='getallactive'),
    path('getallex', views.get_all_ex_agents, name='getallex'),
    path('getalldead', views.get_all_dead_agents, name='getalldead'),


]