from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from talk_app import views
from .models import Player, Team, Coach
from .serializers import TeamSerializer, PlayerSerializer, CoachSerializer



def index(request):
    teams = Team.objects.all()
    context = {'teams': teams}
    return render(request, "talk_app/index.html", context)


class TeamsViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PlayersViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class CoachesViewSet(viewsets.ModelViewSet):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
