
from .models import Client



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
            return [f"{client.__str__()}\n" for client in result]
        except:
            return "Something went wrong, we can't send you list of targets"


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

