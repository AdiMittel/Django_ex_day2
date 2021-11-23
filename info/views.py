from django.shortcuts import render
from .models import Animal, Family

# Create your views here.
def animal(request,animal_id):
    animal = Animal.objects.get(id=animal_id)
    return render(request, 'animal.html', {'Animal': animal})

def family(request,family_id):
    family = Family.objects.get(id=family_id)
    return render(request, 'family.html', {'Family': family})

def animals(request):
    animals = Animal.objects.all()
    return render(request, 'animals.html', {'Animals': animals})


