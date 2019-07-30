

from django.urls import path,re_path

from . import views

urlpatterns = [
    path('add_goods/',views.add_goods),
    path('addgoods_handle/',views.addgoods_handle),
    ]

