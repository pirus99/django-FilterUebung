import datetime
from employees_app.models import Department, Employee

# Departments
sales = Department.objects.create(name='Sales')
engineering = Department.objects.create(name='Engineering')
hr = Department.objects.create(name='HR')
marketing = Department.objects.create(name='Marketing')

# Employees
Employee.objects.create(name="Max Müller", salary=3200.00, department=sales, hire_date=datetime.date(2021, 3, 1))
Employee.objects.create(name="Anna Schmidt", salary=2800.00, department=engineering, hire_date=datetime.date(2022, 7, 10))
Employee.objects.create(name="Clara Wagner", salary=4100.00, department=sales, hire_date=datetime.date(2020, 6, 15))
Employee.objects.create(name="David Fischer", salary=5000.00, department=engineering, hire_date=datetime.date(2019, 1, 20))
Employee.objects.create(name="Emma Becker", salary=2300.00, department=hr, hire_date=datetime.date(2023, 1, 5))
Employee.objects.create(name="Frank Zimmermann", salary=3900.00, department=marketing, hire_date=datetime.date(2021, 11, 11))
Employee.objects.create(name="Greta Meier", salary=3100.00, department=sales, hire_date=datetime.date(2023, 8, 8))
Employee.objects.create(name="Henry Schneider", salary=2700.00, department=hr, hire_date=datetime.date(2022, 2, 2))