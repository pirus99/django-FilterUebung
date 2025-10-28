from django.urls import path
from .views import employee_overview

urlpatterns = [
    path('', employee_overview, name='employee_overview'),
]