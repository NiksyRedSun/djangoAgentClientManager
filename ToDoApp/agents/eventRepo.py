from .models import Event, Agent, Client



class event_repo:

    def create(self, agent_id, client_id, status):
        try:
            agent = Agent.objects.get(id=agent_id)
            client = Client.objects.get(id=client_id)
            event = Event(agent=agent, client=client, status=status)
            event.save()
            return f'Something just happened event id is {event.id}'
        except:
            return "Something went wrong, nothing has happened"


    def get(self, id):
        try:
            event = Event.objects.get(id=id)
            return event.__str__()
        except:
            return f'Event with id {id} not found'


    def get_all(self):
        try:
            result = Event.objects.all()
            return [f"{event}\n" for event in result]
        except:
            return "Something went wrong, we can't send you events"


    def delete(self, id):
        try:
            event = Event.objects.get(id=id)
            event.delete()
            return f"Event id {id} was deleted"
        except:
            return f'Event with id {id} not found'



    def update(self, id, agent_id, client_id, status):
        try:
            event = Event.objects.get(id=id)
            agent = Agent.objects.get(id=agent_id)
            client = Client.objects.get(id=client_id)
            event.agent, event.client, event.status = agent, client, status
            event.save()
            return f"Event id {id} was updated"
        except:
            return f'Something went wrong'

