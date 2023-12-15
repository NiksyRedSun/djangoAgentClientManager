import json
from .models import Agent, EventForAgents, EventForClients, Client
from django.forms.models import model_to_dict







class client_repo:


    def create(self, first_name, last_name, age):
        try:
            client = Client(first_name=first_name, last_name=last_name, age=age)
            client.save()
            return f'We got new target, his id is {client.id}'
        except:
            return "Something went wrong, new target wasn't created"


    def get(self, id):
        try:
            client = Client.objects.get(id=id)
            return client.__str__()
        except:
            return f'Client with id {id} not found'


    def get_all(self):
        try:
            result = Client.objects.all()
            return json.dumps([model_to_dict(agent) for agent in result])
        except Exception as e:
            print(e)
            return f'Something went wrong'


    def delete(self, id):
        try:
            client = Client.objects.get(id=id)
            client.delete()
            return f"Client id {id} was deleted"
        except:
            return f'Client with id {id} not found'



    def update(self, id, first_name, last_name, age):
        try:
            client = Client.objects.get(id=id)
            client.first_name, client.last_name, client.age = first_name, last_name, age
            client.save()
            return f"Looks like client id {id} trying to change his personality"
        except:
            return f'Something went wrong'

