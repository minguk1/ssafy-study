from django.shortcuts import render

# Create your views here.
def index(request):

    info = {
        'name': '바보',
        'age' : 21}




    return render(request, 'myapp/index.html', {'info': info})