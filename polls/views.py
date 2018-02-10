from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world, wellcome to the polls index!")