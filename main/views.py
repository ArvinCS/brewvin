from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'Brew\'vin',
        'name': 'Arvin',
        'class': 'PBP D',
    }

    return render(request, "main.html", context)