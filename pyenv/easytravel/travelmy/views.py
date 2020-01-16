from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Destination
#from django.http import HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse('Hello world')

    dests = Destination.objects.all()

    return render(request, 'travelmy/index.html', {'dests': dests})


def about(request):
    return render(request, 'travelmy/about.html', { 'title': 'About' })


class DestListView(ListView):
    model = Destination
    template_name = 'travelmy/index.html'
    context_object_name = 'dests'
    paginate_by = 3


@login_required
def details(request, pk):
    dests = Destination.objects.get(id=pk)

    return render(request, 'travelmy/details.html', { 'dests': dests, 'title': 'Details' })