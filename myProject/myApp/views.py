
from django.shortcuts import render, redirect
from .models import Person

people = []

def add_person(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        person = Person(username=username, password=password)
        people.append(person)
        return redirect('default')
    return render(request, 'myapp/add.html')

def show_people(request):
    context = {'people': people}
    return render(request, 'myapp/default.html', context)
