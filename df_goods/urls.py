from django.urls import path
from . import views
from df_goods.views import *

urlpatterns = [
    path('', views.index),
    path('list<int:tid>_<int:pindex>_<int:sort>/', views.list),
    path('<int:id>/', views.detail),
    path('search/', MySearchView()),
]
