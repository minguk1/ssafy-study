from django.shortcuts import render

# Create your views here.
def food(request):
    food = ["피자", "치킨", "국밥", "초밥", "민초흑당로제마라탕"]
    context = {"food" : food,
                "check" : 1}

    return render(request, 'menus/food.html', context)

def drink(request):
    drink = ["cider", "coke", "miranda", "fanta", "eye of finetree"]
    context = {"drink" : drink,
                "check" : 2}

    return render(request, 'menus/drink.html', context)

def receipt(request):
    food = ["피자", "치킨", "국밥", "초밥", "민초흑당로제마라탕"]
    drink = ["cider", "coke", "miranda", "fanta", "eye of finetree"]
    order = request.GET["order"]
    check = request.GET["check"]
    if check == '1':
        lis = ["피자", "치킨", "국밥", "초밥", "민초흑당로제마라탕"]
    else:
        lis = ["cider", "coke", "miranda", "fanta", "eye of finetree"]
    context = {
        "lis" : lis,
        "order" : order
    }

    return render(request, 'menus/receipt.html', context)