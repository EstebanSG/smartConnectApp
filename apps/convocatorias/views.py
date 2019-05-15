from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hola mundo</h1>")
    return render(request, "index.html", {})