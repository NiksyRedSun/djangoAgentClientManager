import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .agentRepo import agent_repo
from .clientRepo import client_repo
from .eventRepo import event_repo
from .models import Agent
# Create your views here.

agent_repo = agent_repo()
client_repo = client_repo()
event_repo = event_repo()


def __сheck_inputs(inputs, requires):
    for param in requires:
        if param not in inputs:
            return json.dumps({'status': 'data_error', 'message': f'{param} expected', 'error_code:': 400})
    return 'passed'


@csrf_exempt
def index(request):
    return HttpResponse(agent_repo.get_all())


@csrf_exempt
def get_delete_put_agent(request, id):

    if request.method == 'GET':
        return HttpResponse(agent_repo.get(id))


    elif request.method == 'DELETE':
        return HttpResponse(agent_repo.delete(id))


    elif request.method == 'PUT':
        inputs = json.loads(request.body)
        result = __сheck_inputs(inputs, ['first_name', 'last_name', "nickname", "age"])
        if result != 'passed':
            return result
        return HttpResponse(agent_repo.update(id, inputs["first_name"], inputs["last_name"], inputs["nickname"], inputs["age"]))


@csrf_exempt
def post_agent(request):
    if request.method == 'POST':
        inputs = json.loads(request.body)
        result = __сheck_inputs(inputs, ['first_name', 'last_name', "nickname", "age"])
        if result != 'passed':
            return HttpResponse(result)
        return HttpResponse(agent_repo.create(inputs["first_name"], inputs["last_name"], inputs["nickname"], inputs["age"]))
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




@csrf_exempt
def get_all_events(request):
    return HttpResponse(event_repo.get_all())



@csrf_exempt
def get_delete_put_event(request, id):

    if request.method == 'GET':
        return HttpResponse(event_repo.get(id))


    elif request.method == 'DELETE':
        return HttpResponse(event_repo.delete(id))


    elif request.method == 'PUT':
        inputs = json.loads(request.body)
        result = __сheck_inputs(inputs, ['agent', 'client', "status"])
        if result != 'passed':
            return result
        return HttpResponse(event_repo.update(id, inputs["agent"], inputs["client"], inputs["status"]))


@csrf_exempt
def post_event(request):
    if request.method == 'POST':
        inputs = json.loads(request.body)
        result = __сheck_inputs(inputs, ['agent', 'client', "status"])
        if result != 'passed':
            return HttpResponse(result)
        return HttpResponse(event_repo.create(inputs["agent"], inputs["client"], inputs["status"]))
    else:
        return HttpResponse("Wrong method")



@csrf_exempt
def attempt(request):
    if request.method == 'PUT':
        inputs = json.loads(request.body)
        result = __сheck_inputs(inputs, ['agent', 'client'])
        if result != 'passed':
            return HttpResponse(result)
        return HttpResponse(event_repo.assassination_attempt(inputs["agent"], inputs["client"]))
    else:
        return HttpResponse("Wrong method")