from django.contrib import admin
from .models import truck_type, truck, department, employee, header_report, delivery_note,list_report

admin.site.register(truck_type)
admin.site.register(truck)
admin.site.register(department)
admin.site.register(employee)
admin.site.register(header_report)
admin.site.register(delivery_note)
admin.site.register(list_report)

