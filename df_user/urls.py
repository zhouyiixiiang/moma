

from django.urls import path,re_path

from . import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('login_handle/', views.login_handle),
    path('register/',views.register),
    path('register_handle/',views.register_handle),
    path('register_exist/', views.register_exist),
    #path('order<pindex>/', views.order),
    re_path('order(?P<pindex>\w*)/', views.order),
    #re_path(r'order(?d+)/$', views.order),
    path('info/', views.info),
    path('logout/',views.logout),
    path('download/',views.file_download),
    path('site/', views.site),
    ]

