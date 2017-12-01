from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)
def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)
def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"  # more on session below
        print "*"*50
        return redirect("/")
    else:
        return redirect("/")
def show(request, number):
    print number
    return HttpResponse("placeholder to display blog " + number)
def edit(request, number):
    print number
    return HttpResponse("placeholder to edit blog " + number)
def delete(request, number):
    print number
    return HttpResponse("destory blog " + number)