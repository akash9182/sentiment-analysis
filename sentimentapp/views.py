from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import userinput
from sentimentapp.sentiment import primary


def index(request):
    user_input = userinput()
    return render(request, "index.html", {'sentence': user_input})

def analyse(request):
    user_input = userinput(request.GET or None)
    if request.GET and user_input.is_valid():
        sentence = user_input.cleaned_data['input_sentence']
        print(sentence)
        data = primary(sentence)
        return render(request, "result.html", {'data': data})
    return render(request, "index.html", {'sentence': user_input})