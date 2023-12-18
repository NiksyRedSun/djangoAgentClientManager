import json
from .models import Agent, EventForAgents, EventForClients
from django.forms.models import model_to_dict
from django.core import serializers



class agent_repo:


    def create(self, first_name, last_name, nickname, age):
        try:
            agent = Agent(first_name=first_name, last_name=last_name, nickname=nickname, age=age)
            agent.save()
            return f'Our crew got new member, his id is {agent.id}'
        except Exception as e:
            print(e)
            return f'Something went wrong'


    def get(self, id):
        try:
            agent = Agent.objects.get(id=id)
            return json.dumps(model_to_dict(agent))
        except Exception as e:
            print(e)
            return f'Something went wrong'


    def get_all(self):
        try:
            result = Agent.objects.all()
            return json.dumps([model_to_dict(agent) for agent in result])
        except Exception as e:
            print(e)
            return f'Something went wrong'


    def delete(self, id):
        try:
            agent = Agent.objects.get(id=id)
            agent.delete()
            return f"Member id {id} was deleted"
        except Exception as e:
            print(e)
            return f'Something went wrong'



    def update(self, id, first_name, last_name, nickname, age):
        try:
            agent = Agent.objects.get(id=id)
            agent.first_name, agent.last_name, agent.nickname, agent.age = first_name, last_name, nickname, age
            agent.save()
            return f"Agent id {id} was updated"
        except Exception as e:
            print(e)
            return f'Something went wrong'



    def get_all_events_for_agent(self, id):
        try:
            agent = Agent.objects.get(id=id)
            events = [*EventForClients.objects.filter(agent=agent), *EventForAgents.objects.filter(agent=agent)]
            events.sort(key=lambda x: x.time)

            def time_to_unix(event):
                event.time = int(event.time.timestamp())
                return event

            events = list(map(time_to_unix, events))

            dict_list = [model_to_dict(event) for event in events]

            for i in range(len(events)):
                dict_list[i]["time"] = events[i].time


            return json.dumps(dict_list)

        except Exception as e:
            print(e)
            return f'Something went wrong'


    def get_uncovering_event(self, id):
        try:
            agent = Agent.objects.get(id=id)
            event = EventForClients.objects.filter(agent=agent, status=4)
            return json.dumps(model_to_dict(event[0]))

        except Exception as e:
            print(e)
            return f'Something went wrong'


    def get_all_active_agents(self):
        try:
            result = Agent.objects.filter(status=True, membership=True).order_by("-exp")
            return json.dumps([model_to_dict(agent) for agent in result])

        except Exception as e:
            print(e)
            return f'Something went wrong'


    def get_all_ex_agents(self):
        try:
            result = Agent.objects.filter(membership=False, status=True)
            return json.dumps([model_to_dict(agent) for agent in result])

        except Exception as e:
            print(e)
            return f'Something went wrong'


    def get_all_dead_agents(self):
        try:
            result = Agent.objects.filter(status=False)
            return json.dumps([model_to_dict(agent) for agent in result])

        except Exception as e:
            print(e)
            return f'Something went wrong'










