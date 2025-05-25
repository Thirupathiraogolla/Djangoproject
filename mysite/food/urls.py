from django.urls import path
from . import views

app_name='food'
urlpatterns = [
    path('',views.index, name='index'),
    path('details/<int:id>', views.details, name='details'),
    #adding items
    path('add/', views.add_item, name='add_item'),
    path('update/<int:item_id>/', views.update_item, name='update_item'),
    #delete
    path('delete/<int:item_id>/',views.delete_item, name='delete_item'),

]