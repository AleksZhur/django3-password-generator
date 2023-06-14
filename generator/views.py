from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    thepassword = ''
   # lowercase_letters = list('abcdefghijklmnopqrstuvwxyz')
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    simbol = '!#$%&*+-=?@^_'
    length = int(request.GET.get('length', 12))

   # if request.GET.get('uppercase'):
   #     lowercase_letters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

   #if request.GET.get('numbers'):
   #     lowercase_letters.extend(list('0123456789'))

    #if request.GET.get('special'):
      #  lowercase_letters.extend(list('!#$%&*+-=?@^_'))

    #for i in range(length):
     #   thepassword += random.choice(lowercase_letters)

    while len(thepassword) != length:
        if request.GET.get('numbers'):
            thepassword += random.choice(digits)
        if request.GET.get('uppercase'):
            thepassword += random.choice(uppercase_letters)
        if request.GET.get('low_case'):
            thepassword += random.choice(lowercase_letters)
        if request.GET.get('special'):
            thepassword += random.choice(simbol)
        if request.GET.get('bad_chars'):
            thepassword = ''.join([char for char in thepassword if char not in 'il1Lo0O'])

    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')