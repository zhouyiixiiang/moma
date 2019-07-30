
from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    #path('<int:question_id>/', views.detail, name='detail'),
    #path('<int:question_id>/results/', views.results, name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
    path('',views.order),
    path('order_handle/', views.order_handle),
    path('pay<int:oid>/',views.pay),
    ]


