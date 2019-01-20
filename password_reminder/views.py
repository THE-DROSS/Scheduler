from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def reminder(request):
    return render(request, 'password_reminder/reminder.tpl.html', {
        'foo': 'あ'
    })


def display(request):
    return render(request, "You're looking at question")


def input_pass(request):
    response = "You're looking at the results of question."
    return HttpResponse(response)


def setting(request):
    return HttpResponse("You're voting on question")


def complete(request):
    return HttpResponse("You're voting on question %s." % question_id)
