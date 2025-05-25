from django.shortcuts import render,redirect
from django.http import HttpResponse
from food.models import items
from .forms import item_form
# Create your views here.
def index(request):
    item=items.objects.all()
    content={
        'items':item
    }
    return render(request,'food/index.html',content)

def details(request,id):
    item=items.objects.get(id=id)
    content={
        'item':item
    }
    return render(request,'food/details.html',content)

def add_item(request):
    form =item_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
       
    return render(request,'food/item_add.html',{'form':form}) 

def update_item(request,item_id):
    item = items.objects.get(id=item_id)
    form = item_form(request.POST or None,instance=item)
    
    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/item_add.html',{'form':form,'item':item})

def delete_item(request,item_id):
    item=items.objects.get(id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request,'food/item_add.html',{'item':item})
    