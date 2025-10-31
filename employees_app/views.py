from django.shortcuts import render
from .models import Employee
from django.db.models import Avg, Q
from datetime import date


def employee_overview(request):

    # Hier die entsprechenden Filter anlegen und die context-Variable definieren, um die Daten an das Template zu übergeben

    high_earners = Employee.objects.filter(salary__gte=5000)
    average_salary = Employee.objects.aggregate(avg_salary=Avg('salary'))['avg_salary'] or 0
    hired_this_year = Employee.objects.filter(hire_date__year=date.today().year)

    q = request.GET.get('q', '').strip()
    if q:
        employees = Employee.objects.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q))
    else:
        employees = Employee.objects.all()

    context = {
        'employees': employees,
        'high_earners': high_earners,
        'average_salary': average_salary,
        'hired_this_year': hired_this_year,
    }
    return render(request, 'employee_list.html', context)
