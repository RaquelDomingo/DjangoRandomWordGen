from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
import random

# Create your views here.
def index(request):
    if not 'attempt' in request.session:
        request.session['attempt'] = 0
        request.session['word'] = 'Click GENERATE for a Random Word!'
    return render(request, 'random_word/index.html')

def create(request):
    random_word = ''
    letters = get_random_string(length=14)
    for i in range(12):
        letter_index = random.randint(0, len(letters) - 1)
        random_word += letters[letter_index]
    request.session['attempt'] += 1
    request.session['word'] = random_word
    return redirect('/')

def reset(request):
    del request.session['attempt']
    del request.session['word']
    return redirect('/')

