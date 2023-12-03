
from .models import Member



class membersRepo:


    def __guard_is_not_empty(self, member):
        if member is None:
            raise ValueError('There was no any person')


    def create(self, member):
        self.__guard_is_not_empty(member)
        member.save()
        return f'Current Person id is {member.id}'

