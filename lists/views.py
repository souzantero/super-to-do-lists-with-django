from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from lists.forms import  ExistingListItemForm, ItemForm
from lists.models import Item, List

def home_page(request):
    return render(request, "home.html", { 'form': ItemForm() })

def new_list(request):
    form = ItemForm(data = request.POST)
    
    if form.is_valid():
        created_list = List.objects.create()
        form.save(for_list = created_list)

        return redirect(created_list)
    
    return render(request, 'home.html', { 'form': form })

def view_list(request, list_id):
    recovered_list = List.objects.get(id = list_id)
    form = ExistingListItemForm(for_list = recovered_list)

    if request.method == 'POST':
        form = ExistingListItemForm(for_list = recovered_list, data = request.POST)

        if form.is_valid():
            form.save()

            return redirect(recovered_list)
    
    return render(request, 'list.html', {
        'list': recovered_list,
        'form': form
    })