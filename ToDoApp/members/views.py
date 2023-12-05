import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .memberRepo import member_repo
from .clientRepo import client_repo
from .models import Member
# Create your views here.

member_repo = member_repo()
client_repo = client_repo()


def __сheck_inputs(inputs, requires):
    for param in requires:
        if param not in inputs:
            return json.dumps({'status': 'data_error', 'message': f'{param} expected', 'error_code:': 400})
    return 'passed'


@csrf_exempt
def index(request):
    return HttpResponse(member_repo.get_all())


@csrf_exempt
def get_delete_put_member(request, id):

    if request.method == 'GET':
        return HttpResponse(member_repo.get(id))


    elif request.method == 'DELETE':
        return HttpResponse(member_repo.delete(id))


    elif request.method == 'PUT':
        inputs = json.loads(request.body)
        result = __сheck_inputs(inputs, ['first_name', 'last_name', "age"])
        if result != 'passed':
            return result
        return HttpResponse(member_repo.update(id, inputs["first_name"], inputs["last_name"], inputs["age"]))


@csrf_exempt
def post_member(request):
    if request.method == 'POST':
        inputs = json.loads(request.body)
        result = __сheck_inputs(inputs, ['first_name', 'last_name', "age"])
        if result != 'passed':
            return HttpResponse(result)
        return HttpResponse(member_repo.create(inputs["first_name"], inputs["last_name"], inputs["age"]))
    else:
        return HttpResponse("Wrong method")


@csrf_exempt
def get_all_clients(request):
    return HttpResponse(client_repo.get_all())


@csrf_exempt
def get_delete_put_client(request, id):

    if request.method == 'GET':
        return HttpResponse(client_repo.get(id))


    elif request.method == 'DELETE':
        return HttpResponse(client_repo.delete(id))


    elif request.method == 'PUT':
        inputs = json.loads(request.body)
        result = __сheck_inputs(inputs, ['first_name', 'last_name', "age"])
        if result != 'passed':
            return result
        return HttpResponse(client_repo.update(id, inputs["first_name"], inputs["last_name"], inputs["age"]))


@csrf_exempt
def post_client(request):
    if request.method == 'POST':
        inputs = json.loads(request.body)
        result = __сheck_inputs(inputs, ['first_name', 'last_name', "age"])
        if result != 'passed':
            return HttpResponse(result)
        return HttpResponse(client_repo.create(inputs["first_name"], inputs["last_name"], inputs["age"]))
    else:
        return HttpResponse("Wrong method")
