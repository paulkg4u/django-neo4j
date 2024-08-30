from django.shortcuts import render, redirect

# Create your views here.

from .models import Person, Movie
from django.views.generic import ListView, DetailView


def person_list(request):
    persons = Person.nodes.all()
    context = {
        'persons': persons
    }
    return render(request, 'person_list.html', context)


def person_detail(request, name):
    person = Person.nodes.get(name=name)
    context = {
        'person': person,
        'movies': person.acted_in.all(),
        'friends': person.friends.all()

    }
    return render(request, 'person_detail.html', context)


def create_person(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        person = Person(name=name, age=age)
        person.save()
        return redirect('person_list')
    else:
        return render(request, 'create_person.html')
