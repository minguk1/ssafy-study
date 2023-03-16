from django.shortcuts import render

# Create your views here.
def throw(request):

    return render(request, 'myapp/throw.html')

def catch(request):
    print(request.GET["message"])
    context = {
        "message" : request.GET["message"],
        "key" : request.GET["key"]
    }

    return render(request, "myapp/catch.html", context)