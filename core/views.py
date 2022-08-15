from collections import defaultdict
from random import choice

from django.shortcuts import render
from .models import *


def index(request):
    team = list(Team.objects.all())
    roster = Roster.objects.all()

    data = defaultdict(list)

    for r in roster:
        data[r] = [team.pop(team.index(choice(team))) for _ in range(2)]

    for r in roster:
        total = sum(t.points for t in data[r])

    for k, v in data.items():
        print(f"{k} - {v} ")

    context = {
        'data': data.items()

    }
    return render(request,  'base.html', context)