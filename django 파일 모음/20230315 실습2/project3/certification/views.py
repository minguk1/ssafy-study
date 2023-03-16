from django.shortcuts import render

# Create your views here.
def certification1(request):
    
    age = range(25, 31)
    grade = ['a','b','c','d']
    context = { 'age' : age, 'grade' : grade, 'name' : '김태형'}

    
    return render(request, 'certification/certification1.html', context)

def certification2(request):
    age = range(25, 31)
    grade = ['a','b','c','d']
    context = { 'age' : age, 'grade' : grade, 'name' : "신성주"}
    
    return render(request, 'certification/certification2.html', context)

def certification3(request):
    age = range(25, 31)
    grade = ['a','b','c','d']
    context = { 'age' : age, 'grade' : grade, 'name' : "임준환"}
    
    return render(request, 'certification/certification3.html', context)