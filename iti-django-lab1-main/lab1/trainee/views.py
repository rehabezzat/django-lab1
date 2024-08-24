from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def trainee_list(request):
    trainees = [
        {
            "id": 1,
            "name": "mazen",
            "age": 23,
            "email": "mazen@gmail.com",
            "department": "pyhton",
        },
        {
            "id": 2,
            "name": "saad",
            "age": 25,
            "email": "saad@gmail.com",
            "department": "java",
        },
        {
            "id": 3,
            "name": "ahmed",
            "age": 27,
            "email": "ahmed@gmail.com",
            "department": "c++",
        },
    ]
    context = {}
    context["trainees"] = trainees
    return render(request, "trainee/list.html", context)
    # return HttpResponse("<h1>Trainee List</h1>")


def trainee_create(request):
    # return HttpResponse("<h1>Trainee create</h1>")
    return render(request, "trainee/create.html")


def trainee_update(request, id):
    # return HttpResponse("<h1>Trainee update</h1>")
    context = {}
    context = {"id": id}
    return render(request, "trainee/update.html", context)


def trainee_delete(request, id):
    # return HttpResponse("<h1>Trainee delete</h1>")
    context = {}
    context = {"id": id}
    return render(request, "trainee/delete.html", context)


def trainee_details(request, id):
    # return HttpResponse(f"<h1>Trainee Details: {id}</h1>")
    context = {}
    context = {"id": id}
    return render(request, "trainee/details.html", context)
