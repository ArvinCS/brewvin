from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from main.views import logout_user
from django.contrib.auth.forms import UserCreationForm

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return JsonResponse({
                    "username": user.username,
                    "status": True,
                    "message": "Login sukses!"
                }, status=200)
            else:
                return JsonResponse({
                    "status": False,
                    "message": "Login gagal, akun dinonaktifkan."
                }, status=401)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, periksa kembali email atau kata sandi."
            }, status=401)
    return JsonResponse({
        "status": False,
        "message": "Method not allowed."
    }, status=405)

@csrf_exempt
def register(request):    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                "status": True,
                "message": "Berhasil mendaftar akun baru!"
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Maaf, username atau password tidak valid. Silahkan coba lagi."
            }, status=401)
    return JsonResponse({
        "status": False,
        "message": "Method not allowed."
    }, status=405)

@csrf_exempt
def logout(request):
    logout_user(request)
    return JsonResponse({
        "status": True,
        "message": "Successfully Logged Out!"
    }, status=200)
