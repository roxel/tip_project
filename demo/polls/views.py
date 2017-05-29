from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return HttpResponse(request)