import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from main.forms import ItemForm
from main.models import Item

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    
    context = {
        'app_name': 'Brew\'vin',
        'name': request.user.username,
        'class': 'PBP D',
        'menus': items,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register_user(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        else:
            messages.error(request, form.error_messages)
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def remove_stock(request, id):
    if request.method == 'POST':
        data = Item.objects.get(pk=id)

        if data:
            data.amount -= 1
            data.save()
            return HttpResponseRedirect(reverse('main:show_main'))
        else:
            return HttpResponse("ID does not exist")
    return HttpResponse('Request method is not valid')

def add_stock(request, id):
    if request.method == 'POST':
        data = Item.objects.get(pk=id)

        if data:
            data.amount += 1
            data.save()
            return HttpResponseRedirect(reverse('main:show_main'))
        else:
            return HttpResponse("ID does not exist")
    return HttpResponse('Request method is not valid')

def delete_item(request, id):
    if request.method == 'POST':
        data = Item.objects.get(pk=id)

        if data:
            data.delete()
            return HttpResponseRedirect(reverse('main:show_main'))
        else:
            return HttpResponse("ID does not exist")
    return HttpResponse('Request method is not valid')

@csrf_exempt
def create_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        taste = request.POST.get("taste")
        user = request.user

        new_product = Item(name=name, amount=amount, description=description, taste=taste, user=user)
        new_product.save()

        return JsonResponse({"status": True, "message": "Success!"}, status=200)

    return HttpResponseNotFound()

@csrf_exempt
def remove_item_ajax(request, id):
    if request.method == 'POST':
        data = Item.objects.get(pk=id)

        if data:
            data.delete()
            return HttpResponse("ID does not exist", status=201)
        else:
            return HttpResponse("ID does not exist")
    return HttpResponseNotFound()

@csrf_exempt
def increase_item_ajax(request, id):
    if request.method == 'POST':
        data = Item.objects.get(pk=id)

        if data:
            data.amount += 1
            data.save()
            return HttpResponse("ID does not exist", status=201)
        else:
            return HttpResponse("ID does not exist")
    return HttpResponseNotFound()

@csrf_exempt
def decrease_item_ajax(request, id):
    if request.method == 'POST':
        data = Item.objects.get(pk=id)

        if data:
            data.amount -= 1
            data.save()
            return HttpResponse("ID does not exist", status=201)
        else:
            return HttpResponse("ID does not exist")
    return HttpResponseNotFound()