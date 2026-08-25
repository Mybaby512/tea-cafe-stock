from django.shortcuts import render, redirect, get_object_or_404
from .models import TeaItem, Category
from .forms import TeaItemForm

def tea_list(request):
    query = request.GET.get('q', '')
    if query:
        items = TeaItem.objects.filter(name__icontains=query)
    else:
        items = TeaItem.objects.all()
    return render(request, 'tea_stock/tea_list.html', {'items': items, 'query': query})

def tea_add(request):
    if request.method == 'POST':
        form = TeaItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tea_list')
    else:
        form = TeaItemForm()
    return render(request, 'tea_stock/tea_form.html', {'form': form, 'title': 'เพิ่มเมนูชาใหม่'})

def tea_edit(request, pk):
    item = get_object_or_404(TeaItem, pk=pk)
    if request.method == 'POST':
        form = TeaItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('tea_list')
    else:
        form = TeaItemForm(instance=item)
    return render(request, 'tea_stock/tea_form.html', {'form': form, 'title': 'แก้ไขเมนูชา'})

def tea_delete(request, pk):
    item = get_object_or_404(TeaItem, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('tea_list')
    return render(request, 'tea_stock/tea_confirm_delete.html', {'item': item})