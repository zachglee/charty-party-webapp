from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting, Game
from .utils import game_name_generator

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

# -------- MY MODIFICATIONS

# lets see if we can maintain state here

def play(request):

    new_game = Game()
    new_game.name = game_name_generator()
    new_game.graph = "exponential"
    new_game.save()

    state = new_game.name

    return render(request, "play.html", {"state": state})

def game(request, name):
    games = Game.objects.filter(name=name)
    if games:
        return render(request, "game.html", {"game": games.first()})
    else:
        return render(request, "nogame.html", {"name": name})