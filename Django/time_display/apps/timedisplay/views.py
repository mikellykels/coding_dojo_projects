from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
    "datetime": datetime.datetime.now()
    }
    return render(request, 'timedisplay/index.html', context)
