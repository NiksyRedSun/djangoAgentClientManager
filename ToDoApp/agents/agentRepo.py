
from .models import Agent



class agent_repo:


    def create(self, first_name, last_name, age):
        try:
            agent = Agent(first_name=first_name, last_name=last_name, age=age)
            agent.save()
            return f'Our crew got new member, his id is {agent.id}'
        except:
            return "Something went wrong, new member wasn't created"


    def get(self, id):
        try:
            agent = Agent.objects.get(id=id)
            return agent.__str__()
        except:
            return f'Agent with id {id} not found'


    def get_all(self):
        try:
            result = Agent.objects.all()
            return [f"{agent}\n" for agent in result]
        except:
            return "Something went wrong, we can't send you names"


    def delete(self, id):
        try:
            agent = Agent.objects.get(id=id)
            agent.delete()
            return f"Member id {id} was deleted"
        except:
            return f'Member with id {id} not found'



    def update(self, id, first_name, last_name, nickname, age):
        try:
            agent = Agent.objects.get(id=id)
            agent.first_name, agent.last_name, agent.nickname, agent.age = first_name, last_name, nickname, age
            agent.save()
            return f"Agent id {id} was updated"
        except:
            return f'Something went wrong'

