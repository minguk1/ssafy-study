from django.shortcuts import render

# Create your views here.
def calculation(request):

    return render(request, 'calculators/calculation.html')

def result(request):
    num1 = int(request.GET["num1"])
    num2 = int(request.GET["num2"])
    num_plus = num1 + num2
    num_minus = num1 - num2
    num_multi = num1 * num2
    if num2 != 0:
        num_dis = num1/num2
    elif num2 == 0:
        num_dis = "계산할 수 없습니다"



    context = {
        "num1" : num1,
        "num2" : num2,
        "plus" : num_plus,
        "minus" : num_minus,
        "multi" : num_multi,
        "dis" : num_dis
    }

    return render(request, 'calculators/result.html', context)