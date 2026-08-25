from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Employee
from .forms import EmployeeForm

def employee_list(request):
    query = request.GET.get('q', '')
    employees = Employee.objects.filter(first_name__icontains=query) | Employee.objects.filter(last_name__icontains=query) | Employee.objects.filter(email__icontains=query)
    employees = employees.order_by('-id')

    paginator = Paginator(employees, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'employee/employee_list.html', {'page_obj': page_obj, 'query': query})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee/employee_form.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee/employee_form.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee/employee_confirm_delete.html', {'employee': employee})