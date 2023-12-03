import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .membersRepo import membersRepo
from .models import Member
# Create your views here.

membersRepo = membersRepo()

def index(request):
    return render(request, "members/index.html")


@csrf_exempt
def post_user_profile(request):
    inputs = json.loads(request.body)
    # check = __сheck_inputs(inputs, ['name', 'age'])
    # if check != 'passed':
    #     return check
    first_name = inputs["first_name"]
    last_name = inputs["last_name"]
    age = inputs["age"]

    return HttpResponse(membersRepo.create(Member(first_name=first_name, last_name=last_name, age=age)))
