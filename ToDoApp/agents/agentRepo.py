import json
from .models import Agent, EventForAgents, EventForClients
from django.forms.models import model_to_dict
from django.core import serializers


def time_to_unix_ag(agent):
    agent.start_membership = int(agent.start_membership.timestamp())
    return agent


def time_to_unix_ev(event):
    event.time = int(event.time.timestamp())
    return event


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


            agent = time_to_unix_ag(agent)
            agent_dict = model_to_dict(agent)
            agent_dict['start_membership'] = agent.start_membership

            return json.dumps(agent_dict)

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



            events = list(map(time_to_unix_ev, events))

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
            event = EventForClients.objects.filter(agent=agent, status=3)[0]
            event = time_to_unix_ev(event)

            event_dict = model_to_dict(event)
            event_dict['time'] = event.time

            return json.dumps(event_dict)

        except Exception as e:
            print(e)
            return f'Something went wrong'


    def get_all_active_agents(self):
        try:
            agents = Agent.objects.filter(status=True, membership=True).order_by("-exp")



            agents = list(map(time_to_unix_ag, agents))

            dict_list = [model_to_dict(event) for event in agents]

            for i in range(len(agents)):
                dict_list[i]["start_membership"] = agents[i].start_membership

            return json.dumps(dict_list)


        except Exception as e:
            print(e)
            return f'Something went wrong'


    def get_all_ex_agents(self):
        try:
            result = Agent.objects.filter(membership=False, status=True).order_by("-exp")
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


    def get_agent_contracts(self, id):
        try:
            agent = Agent.objects.get(id=id)
            events = EventForClients.objects.filter(agent=agent)
            return json.dumps([model_to_dict(event) for event in events])

        except Exception as e:
            print(e)
            return f'Something went wrong'










