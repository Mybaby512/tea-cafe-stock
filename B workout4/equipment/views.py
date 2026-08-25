from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Equipment
from .forms import EquipmentForm

def equipment_list(request):
    query = request.GET.get('q', '')
    equipments = Equipment.objects.filter(name__icontains=query) | Equipment.objects.filter(code__icontains=query)
    equipments = equipments.order_by('-id')

    # ระบบแบ่งหน้า (Pagination) 5 รายการต่อหน้า
    paginator = Paginator(equipments, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'equipment/equipment_list.html', {'page_obj': page_obj, 'query': query})

def equipment_create(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm()
    return render(request, 'equipment/equipment_form.html', {'form': form, 'action_title': 'เพิ่มอุปกรณ์เข้าคลัง'})

def equipment_update(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'equipment/equipment_form.html', {'form': form, 'action_title': 'แก้ไขข้อมูลอุปกรณ์'})

def equipment_delete(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        equipment.delete()
        return redirect('equipment_list')
    return render(request, 'equipment/equipment_confirm_delete.html', {'equipment': equipment})