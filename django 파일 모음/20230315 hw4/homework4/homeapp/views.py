from django.shortcuts import render
import datetime
# Create your views here.
def menu(request):
    menus = ['짜장면', '짬뽕', '볶음밥']
    today = datetime.datetime.now()
    context = {'menus' : menus, 'today': today}


    return render(request, 'homeapp/menu.html', context)