from django.shortcuts import render

# Create your views here.
def show_main(request):
    # context = {
    #     'name': 'Arabica',
    #     'amount': 69,
    #     'description': 'Most common coffee beans around the world',
    #     'taste': 'Full of flavour and aroma, depends on the environment where it grows'
    # }
    context = {
        'app_name': 'Brew\'vin',
        'name': 'Arvin',
        'class': 'PBP D',
    }

    return render(request, "main.html", context)