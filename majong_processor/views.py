from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from majong_processor.models import *
import json

from django.shortcuts import redirect

@csrf_exempt
# handle request related to get index page content
def handle_index(request):
    if request.method == "GET":
        index_template = loader.get_template('zhimajiang.html')
        return HttpResponse(index_template.render())
        # return redirect("http://stackoverflow.com/")
    else:
        return HttpResponseNotAllowed(['GET'])
@csrf_exempt
# handle request related to add name page
def handle_name(request):
    if request.method == "GET":
        if Player.objects.all().exists():
            first = Player.objects.filter(id=1)
            second = Player.objects.filter(id=2)
            third = Player.objects.filter(id=3)
            fourth = Player.objects.filter(id=4)
            return HttpResponse("Player names are " + first + ", " + second + ", " + third + ", " + fourth)
        else:
            return HttpResponse("OK")
    elif request.method == "POST":
        '''
        json_data = json.loads(request.body)
        first = Player(name_text=json_data['first'], id=1)
        second = Player(name_text=json_data['second'], id=2)
        third = Player(name_text=json_data['third'], id=3)
        fourth = Player(name_text=json_data['fourth'], id=4)
        first.save()
        second.save()
        third.save()
        fourth.save()
        print('Showing database name table items:')
        print(Player.objects.all())
        return HttpResponse("Server has received players' names.")
        '''
        print(request.body)
        player = json.loads(str(request.body, 'utf-8'))
        # player = json.loads(request.body.decode('utf-8'))
        # print(player['player'])
        response = HttpResponse("Server got it!")
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        print(response)
        return response
    elif request.method == "PUT":
        json_data = json.loads(request.body)
        first = json_data['first']
        second = json_data['second']
        third = json_data['third']
        fourth = json_data['fourth']
        Player.objects.filter(id=1).update(name_text=first)
        Player.objects.filter(id=2).update(name_text=second)
        Player.objects.filter(id=3).update(name_text=third)
        Player.objects.filter(id=4).update(name_text=fourth)
        print('Showing database name table items:')
        print(Player.objects.all())
        return HttpResponse("Server has changed players' names.")
    elif request.method == "DELETE":
        print('Number of deleted names: ' + str(Player.objects.all().delete()))
        print('Showing database name table items, empty if items are deleted correctly:')
        print(Player.objects.all())
        return HttpResponse("Server has deleted all names.")

@csrf_exempt
# handle request related to add score page
def handle_score(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        round = Round()
        first_player = Player.objects.filter(id=1)
        second_player = Player.objects.filter(id=2)
        third_player = Player.objects.filter(id=3)
        fourth_player = Player.objects.filter(id=4)
        first = Score(score=json_data['first'], round=round, owner=first_player)
        second = Score(score=json_data['second'], round=round, owner=second_player)
        third = Score(score=json_data['third'], round=round, owner=third_player)
        fourth = Score(score=json_data['fourth'], round=round, owner=fourth_player)
        first.save()
        second.save()
        third.save()
        fourth.save()
        print('Showing database name table items:')
        print(Player.objects.all())
        return HttpResponse("Server has received players' .")
    elif request.method == "PUT":
        # TODO: handle modify name request
        return HttpResponse("Handling SCORE PUT")
    elif request.method == "DELETE":

        return HttpResponse("Handling SCORE DELETE")

@csrf_exempt
# handle request related to reset or exit game
def handle_reset_or_exit_game(request):
    # TODO: delete all related database tables
    return HttpResponse("Handling reset or exit game")
