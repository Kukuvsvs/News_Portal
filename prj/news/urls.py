from django.urls import path
from .views import index, details

urlpatterns =[
    path('news_list/', index, name='index'),
    path('new/<str:slug>', details, name='details'),
]
