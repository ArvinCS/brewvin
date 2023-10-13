"""
URL configuration for brewvin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from main.views import add_stock, create_item, create_item_ajax, decrease_item_ajax, delete_item, increase_item_ajax, login_user, logout_user, register_user, remove_item_ajax, remove_stock, show_json, show_json_by_id, show_main, show_xml, show_xml_by_id

app_name = "main"
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_item/', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('remove_stock/<int:id>/', remove_stock, name='remove_stock'),
    path('add_stock/<int:id>/', add_stock, name='add_stock'),
    path('delete_item/<int:id>/', delete_item, name='delete_item'),
    path('create-ajax/', create_item_ajax, name='create_item_ajax'),
    path('remove-ajax/<int:id>/', remove_item_ajax, name='remove_item_ajax'),
    path('increase-ajax/<int:id>/', increase_item_ajax, name='increase_item_ajax'),
    path('decrease-ajax/<int:id>/', decrease_item_ajax, name='decrease_item_ajax')
]
