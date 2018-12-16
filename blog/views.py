from datetime import datetime

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

from blog.forms import EmailForm
from blog.models import StaticFiles
from blog.models import Thought

import json


def hello(request):
    static_file = StaticFiles.objects.first()
    email_form = EmailForm()
    bday = datetime(1990, 2, 11, 0, 0)
    now = datetime.now()
    age = int((now - bday).days / 365.25)

    return render(request, 'hello.html', {
        'static_file': static_file,
        'email_form': email_form,
        'age': age,
    })


def contact(request):
    if request.is_ajax():
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = ('Contact message from '
                       + form.cleaned_data['name']
                       + ' (' + form.cleaned_data['sender'] + ')')
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            recipient = [settings.MY_EMAIL, ]

            send_mail(subject, message, sender, recipient)
            return HttpResponse(json.dumps({'success': True}))
        else:
            return HttpResponse(json.dumps(form.errors))
    else:
        return HttpResponse(status=400)  # bad request


def code(request):
    code_thoughts = Thought.objects.filter(
        tags__name__in=['code']
    ).order_by('-date')
    static_file = StaticFiles.objects.first()
    return render(request, 'code.html', {
        'code_thoughts': code_thoughts,
        'static_file': static_file,
    })


def thoughts(request):
    thoughts = Thought.objects.exclude(
        tags__name__in=['code']
    ).order_by('-date')
    static_file = StaticFiles.objects.first()
    return render(request, 'thoughts.html', {
        'thoughts': thoughts,
        'static_file': static_file,
    })


def thought(request, slug):
    thought = Thought.objects.get(slug=slug)
    return render(request, 'thought.html', {'thought': thought})


# def code_thought(request, slug):
    # code_thought = Thought.objects.get(slug=slug)
    # return render(request, 'code_thought.html', {'code_thought': code_thought})


def sounds(request):
    static_file = StaticFiles.objects.first()
    return render(request, 'sounds.html', {
        'static_file': static_file,
    })


def pics(request):
    static_file = StaticFiles.objects.first()
    return render(request, 'pics.html', {
        'static_file': static_file,
    })
