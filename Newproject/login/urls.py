from django.urls import path
from . import views

urlpatterns =[
    path('',views.display,name='display'),
    path('login/',views.new, name='login'),
    path('index/',views.index,name='index'),
    path('select/', views.select, name='select')
]
