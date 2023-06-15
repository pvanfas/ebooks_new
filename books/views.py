from django.shortcuts import render


def index(request):
    context = {
        "books":"HELLO"
    }
    return render(request, "books/index.html", context)
