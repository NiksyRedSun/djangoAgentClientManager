import random

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



    def assassination_attempt(self, agent_id, client_id):
        try:
            agent = Agent.objects.get(id=agent_id)
            client = Client.objects.get(id=client_id)
            random_num = (agent.equipment_level - client.security_level)*0.1 + agent.exp/1000*0.01 + random.random()
            event = Event()
            event.agent = agent
            event.client = client

            if random_num <= 0.25:
                agent.membership = 0
                agent.status = 0
                event.status = 4
                info = f"{agent.first_name} {agent.nickname} {agent.last_name} is KIA"
            elif random_num <= 0.5:
                agent.membership = 0
                event.status = 3
                info = f"{agent.first_name} {agent.nickname} {agent.last_name} is uncovered as agent"
            elif random_num <= 0.75:
                event.status = 2
                info = f"{agent.first_name} {agent.nickname} {agent.last_name} failed"
            else:
                event.status = 1
                agent.exp += client.exp
                agent.money += client.price
                client.status = 0
                info = f"{agent.first_name} {agent.nickname} {agent.last_name} made his work"

            agent.save()
            client.save()
            event.save()

            return info

        except:
            return f'Something went wrong with request'


