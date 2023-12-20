import random
import json
from .models import EventForClients, Agent, Client, EventForAgents
from django.forms.models import model_to_dict
from django.core import serializers

names = [
    "Alice", "Andrew",
    "Barbara", "Benjamin",
    "Charlotte", "Christopher",
    "David", "Diana",
    "Edward", "Elizabeth",
    "Frank", "Fiona",
    "George", "Grace",
    "Henry", "Hannah",
    "Isaac", "Isabel",
    "Jack", "Jessica",
    "Kevin", "Katherine",
    "Liam", "Lily",
    "Michael", "Megan",
    "Nathan", "Natalie",
    "Oliver", "Olivia",
    "Peter", "Penelope",
    "Quentin", "Quinn",
    "Robert", "Rebecca",
    "Samuel", "Sophia",
    "Thomas", "Taylor",
    "Ulysses", "Uma",
    "Victor", "Victoria",
    "William", "Willow",
    "Xavier", "Xena",
    "Yasmine", "Yuri",
    "Zachary", "Zoe"
]

surnames = [
    "Anderson", "Adams",
    "Brown", "Baker",
    "Clark", "Carter",
    "Davis", "Dixon",
    "Evans", "Edwards",
    "Fisher", "Ford",
    "Garcia", "Gibson",
    "Harris", "Harrison",
    "Irwin", "Ingram",
    "Johnson", "Jackson",
    "Kennedy", "King",
    "Lee", "Lopez",
    "Miller", "Mitchell",
    "Nelson", "Norton",
    "Owens", "O'Connor",
    "Perez", "Parker",
    "Quinn", "Quigley",
    "Reed", "Robinson",
    "Smith", "Stewart",
    "Taylor", "Thomas",
    "Upton", "Underwood",
    "Vargas", "Vance",
    "Williams", "Wilson",
    "Xavier", "Xander",
    "Young", "Yates",
    "Zimmerman", "Zane"
]

nicknames = [
    "Shadow", "Spectre",
    "Viper", "Raven",
    "Phantom", "Ghost",
    "Wraith", "Cobra",
    "Silhouette", "Hawk",
    "Sphinx", "Jaguar",
    "Blade", "Siren",
    "Raptor", "Saber",
    "Echo", "Falcon",
    "Omega", "Prowler",
    "Slyfox", "Panther",
    "Lynx", "Reaper",
    "Thunder", "Griffin",
    "Nightshade", "Bullet",
    "Stalker", "Vortex",
    "Valkyrie", "Crimson",
    "Enigma", "Storm",
    "Phoenix", "Tempest",
    "Onyx", "Rogue",
    "Zenith", "Talon",
    "Spartan", "Sapphire",
    "Wolf", "Zephyr",
    "Nyx", "Neptune",
    "Abyss", "Apex",
    "Blitz", "Banshee"
]


def time_to_unix(event):
    event.time = int(event.time.timestamp())
    return event


class event_repo:

    def create(self, agent_id, client_id, status):
        try:
            agent = Agent.objects.get(id=agent_id)
            client = Client.objects.get(id=client_id)
            event = EventForClients(agent=agent, client=client, status=status)
            event.save()
            return f'Something just happened event id is {event.id}'
        except:
            return "Something went wrong, nothing has happened"


    def get(self, id):
        try:
            event = EventForClients.objects.get(id=id)

            event = time_to_unix(event)
            result_dict = model_to_dict(event)
            result_dict['time'] = event.time

            return json.dumps(result_dict)
        except:
            return f'Something went wrong'


    def get_trash_event(self, id):
        try:
            event = EventForAgents.objects.get(id=id)

            event = time_to_unix(event)
            result_dict = model_to_dict(event)
            result_dict['time'] = event.time

            return json.dumps(result_dict)
        except:
            return f'Something went wrong'


    def get_all(self):
        try:
            events = [*EventForClients.objects.all(), *EventForAgents.objects.all()]
            events.sort(key=lambda x: x.time, reverse=True)

            events = list(map(time_to_unix, events))

            dict_list = [model_to_dict(event) for event in events]

            for i in range(len(events)):
                dict_list[i]["time"] = events[i].time


            return json.dumps(dict_list)

        except Exception as e:
            print(e)
            return f'Something went wrong'


    def delete(self, id):
        try:
            event = EventForClients.objects.get(id=id)
            event.delete()
            return f"Event id {id} was deleted"
        except:
            return f'Event with id {id} not found'



    def update(self, id, agent_id, client_id, status):
        try:
            event = EventForClients.objects.get(id=id)
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

            if not agent.status:
                return "This agent is dead and can't be used for solving problems"

            if not agent.membership:
                return "This agent is excommunicado and can't be used for solving problems"

            client = Client.objects.get(id=client_id)
            random_num = (agent.equipment_level - client.security_level)*0.1 + agent.exp/1000*0.01 + random.random()
            event = EventForClients()
            event.agent = agent
            event.client = client

            if random_num <= 0.15:
                agent.membership = 0
                agent.status = 0
                event.status = 4
                info = f"{agent.first_name} {agent.nickname} {agent.last_name} is KIA"
            elif random_num <= 0.3:
                agent.membership = 0
                event.status = 3
                info = f"{agent.first_name} {agent.nickname} {agent.last_name} is uncovered as agent"
            elif random_num <= 0.65:
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

            return json.dumps(model_to_dict(event))

        except:
            return f'Something went wrong with request'



    def new_agent(self):
        try:
            agent = Agent(first_name=random.choice(names), last_name=random.choice(surnames),
                          nickname=random.choice(nicknames), age=random.randint(20, 50))
            agent.save()
            return json.dumps(model_to_dict(agent))
        except:
            return "Something went wrong, new agent wasn't created"



    def new_client(self):
        try:
            client = Client(first_name=random.choice(names), last_name=random.choice(surnames), age=random.randint(20, 50))
            client.save()
            return json.dumps(model_to_dict(client))
        except:
            return "Something went wrong, new target wasn't created"



    def taking_out_trash(self, agent_id, target_agent_id):
        try:
            agent = Agent.objects.get(id=agent_id)
            target = Agent.objects.get(id=target_agent_id)
            random_num = (agent.equipment_level - target.equipment_level)*0.1 + agent.exp/1000*0.01 - target.exp/1000*0.01 + random.random()
            event = EventForAgents(agent=agent, target=target)

            if random_num <= 0.15:
                agent.membership = 0
                agent.status = 0
                event.status = 4
                info = f"{agent.first_name} {agent.nickname} {agent.last_name} is KIA"

            elif random_num <= 0.65:
                event.status = 2
                info = f"{agent.first_name} {agent.nickname} {agent.last_name} failed"

            else:
                event.status = 1
                agent.exp += int(target.exp//4)
                agent.money += int(target.money//4)
                target.status = 0
                info = f"{agent.first_name} {agent.nickname} {agent.last_name} made his work"

            agent.save()
            target.save()
            event.save()

            return json.dumps(model_to_dict(event))

        except:
            return f'Something went wrong with request'











