from django.shortcuts import render, redirect
from django.http import HttpResponse
from food.models import *
from django.template import loader
from food.forms  import create_item

# Create your views here.

def hello(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    context = {
        'item_list':item_list,  
        }
    return HttpResponse(template.render(context, request))

def item_view(request):
    items = Item.objects.all()
    return render(request,'food/item.html', {'items':items})

def detail_view(request,item_id):
    try:
        item = Item.objects.get(id=item_id)
    except:
        return "Item does not exist"
    return render(request,'food/detail.html',{'item':item})

# def create_view(request):
#     if request.method == 'POST':
#         submitted_form = create_item(request.POST)
#         if submitted_form.is_valid:
#             submitted_form.save()
#         return redirect('food:hello')
#     form = create_item()
#     context = {
#         'form':form,
#     }
#     return render(request, 'food/create_item.html',context)

def create_view(request):
    form = create_item(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:hello')
    return render(request, 'food/create_item.html',{'form':form})

def update_view(request, item_id):
    # get item
    item = Item.objects.get(id=item_id)
    # get form
    form = create_item(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:hello')
    return render(request, 'food/create_item.html', {'form':form, 'item':item})
        

def delete_view(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:item_view')
    return render(request,'food/delete_confirmation.html', {'item':item})
    
    