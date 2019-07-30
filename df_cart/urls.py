from django.urls import path
from . import views

urlpatterns=[
    path('',views.cart),
    path('add<int:gid>_<int:count>/',views.add),
    path('edit<int:cart_id>_<int:count>/',views.edit),
    path('delete<int:cart_id>/',views.delete),
]
