from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from majong_processor.models import *
import json

from django.shortcuts import redirect

@csrf_exempt
# handle request related to get index page content
def handle_index(request):
    if request.method == "GET":
        index_template = loader.get_template('jimajiang.html')
        return HttpResponse(index_template.render())
    else:
        return HttpResponseNotAllowed(['GET'])

@csrf_exempt
# handle request related to add name page
def handle_json_traffic(request):
    if request.method == "GET":
        # first check shuffle, then check if player database is empty, if empty, go to else;
        # if not empty, construct json and send it back via http response

        shuffle = DatabaseShuffle.objects.filter(id=0).first().get_value()
        shuffle = not shuffle
        if shuffle:
            if PlayerShuffle.objects.all().exists():
                print("in 1.1")
                players = list(PlayerShuffle.objects.values_list('name_text'))
                all_score = list(RoundScoreShuffle.objects.values())
                json_response = {'allScore': all_score, 'Players': players}
                print(json_response)
                response = JsonResponse(json_response)
                response["Access-Control-Allow-Origin"] = "*"
                response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
                response["Access-Control-Max-Age"] = "1000"
                response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
                return response
            else:
                print("in 1.2")
                response = HttpResponse("There is no player in this game.")
                response["Access-Control-Allow-Origin"] = "*"
                response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
                response["Access-Control-Max-Age"] = "1000"
                response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
                return response
        else:
            if Player.objects.all().exists():
                print("in 2.1")
                players = list(Player.objects.values_list('name_text'))
                all_score = list(RoundScore.objects.values())
                json_response = {'allScore': all_score, 'Players': players}
                print(json_response)
                response = JsonResponse(json_response)
                response["Access-Control-Allow-Origin"] = "*"
                response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
                response["Access-Control-Max-Age"] = "1000"
                response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
                return response
            else:
                print("in 2.2")
                response = HttpResponse("There is no player in this game.")
                response["Access-Control-Allow-Origin"] = "*"
                response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
                response["Access-Control-Max-Age"] = "1000"
                response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
                return response
    elif request.method == "POST":
        # after recieving a request, first check shuffle to determine which database should be overwritten,
        # then clear that database and write data, after that, execute shuffle

        # prepare values to be written to database
        body = json.loads(request.body)
        all_score_list = list(body['allScore'])
        player_list = list(body['Players'])

        shuffle = DatabaseShuffle.objects.filter(id=0).first().get_value()
        if shuffle:
            PlayerShuffle.objects.all().delete()
            RoundScoreShuffle.objects.all().delete()
            for index, name in enumerate(player_list):
                player = PlayerShuffle(name_text=name, id=index)
                player.save()
            for score in all_score_list:
                round_score = RoundScoreShuffle(id=score['id'], is1=score['is1'], is2=score['is2'],
                                                is3=score['is3'], is4=score['is4'])
                round_score.save()
            print('Post request updated shuffle database successfully.')
            new_shuffle = not shuffle
            DatabaseShuffle.objects.filter(id=0).update(shuffle=new_shuffle)
            print('        Players names are:')
            print(PlayerShuffle.objects.all())
            print('        Round scores are:')
            print(RoundScoreShuffle.objects.all())
        else:
            Player.objects.all().delete()
            RoundScore.objects.all().delete()
            for index, name in enumerate(player_list):
                player = Player(name_text=name, id=index)
                player.save()
            for score in all_score_list:
                round_score = RoundScore(id=score['id'], is1=score['is1'], is2=score['is2'],
                                                is3=score['is3'], is4=score['is4'])
                round_score.save()
            print('Post request updated database successfully.')
            new_shuffle = not shuffle
            DatabaseShuffle.objects.filter(id=0).update(shuffle=new_shuffle)
            print('        Players names are:')
            print(Player.objects.all())
            print('        Round scores are:')
            print(RoundScore.objects.all())

        response = HttpResponse("Server got it!")
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
        return response

    elif request.method == "DELETE":
        Player.objects.all().delete()
        PlayerShuffle.objects.all().delete()
        RoundScore.objects.all().delete()
        RoundScoreShuffle.objects.all().delete()
        return HttpResponse("Server has deleted all names and scores.")

# @csrf_exempt
# handle request related to add score page
'''
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
'''
# @csrf_exempt
# handle request related to reset or exit game
'''
def handle_reset_or_exit_game(request):
    # TODO: delete all related database tables
    return HttpResponse("Handling reset or exit game")
'''
