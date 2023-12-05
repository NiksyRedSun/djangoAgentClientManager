
from .models import Member



class member_repo:


    def create(self, first_name, last_name, age):
        try:
            member = Member(first_name=first_name, last_name=last_name, age=age)
            member.save()
            return f'Our crew got new member, his id is {member.id}'
        except:
            return "Something went wrong, new member wasn't created"


    def get(self, id):
        try:
            member = Member.objects.get(id=id)
            return member
        except:
            return f'Person with id {id} not found'


    def get_all(self):
        try:
            result = Member.objects.all()
            return [f"{member}\n" for member in result]
        except:
            return "Something went wrong, we can't send you names"


    def delete(self, id):
        try:
            member = Member.objects.get(id=id)
            member.delete()
            return f"Member id {id} was deleted"
        except:
            return f'Member with id {id} not found'



    def update(self, id, first_name, last_name, age):
        try:
            member = Member.objects.get(id=id)
            member.first_name, member.last_name, member.age = first_name, last_name, age
            member.save()
            return f"Member id {id} was updated"
        except:
            return f'Something went wrong'

