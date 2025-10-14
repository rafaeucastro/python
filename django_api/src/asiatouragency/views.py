from django.shortcuts import render
from .models import Tour
from django.conf import settings

# Create your views here.
# View are like controllers of and api, it handles a request
def index(request):
    #getting all Tour objects from the database
    tours = Tour.objects.all()
    year = settings.YEAR
    context = {'tours': tours, 'year': year}
    #returning a page located in templates folder
    return render(request, 'tours/index.html', context=context)