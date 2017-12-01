from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
# def index(request):
#     response = "index"
#     return HttpResponse(response)
def survey(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)
def new(request):
    response = "NEW SURVEY"
    return HttpResponse(response)