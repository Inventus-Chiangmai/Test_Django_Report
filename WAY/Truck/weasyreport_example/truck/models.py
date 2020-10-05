from django.db import models

class truck_type(models.Model):
    types = models.CharField(max_length=50)

class truck(models.Model):
    truck_type = models.ForeignKey(truck_type, on_delete=models.CASCADE)
    no = models.CharField(max_length=100)
    
class department(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)

class employee(models.Model):
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    sure_name = models.CharField(max_length=100)
    telephon = models.CharField(max_length=15)
    address = models.CharField(max_length=100)

class header_report(models.Model):
    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    truck = models.ForeignKey(truck, on_delete=models.CASCADE)
    promised_date = models.DateField()
    
class delivery_note(models.Model):
    no = models.CharField(max_length=50)

class list_report(models.Model):
    delivery_note = models.ForeignKey(delivery_note, on_delete=models.CASCADE)
    no = models.IntegerField()
    destination = models.CharField(max_length=100)
    delivery_date = models.DateField()
    remake = models.CharField(max_length=200)
    header_report = models.ForeignKey(header_report, on_delete=models.CASCADE)


