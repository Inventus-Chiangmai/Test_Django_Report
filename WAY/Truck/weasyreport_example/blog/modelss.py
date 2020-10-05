from django.db import models

class Header(models.Model):
    promised_date = models.DateField()
    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    truck = models.ForeignKey(truck, on_delete=models.CASCADE)

    def __str__(self):
        return self.promised_date

class employee(models.Model):
    name = models.CharField(max_length=100)
    sure_name = models.CharField(max_length=100)
    telephon = models.CharField(10)
    address = models.CharField(100)
    department = models.ForeignKey(department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class department(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(50)

    def __str__(self):
        return self.name

class truck(models.Model):
    no = models.CharField(max_length=100)
    truck_type = models.ForeignKey(truck_type, on_delete=models.CASCADE)

    def __str__(self):
        return self.no

class truck_type(models.Model):
    types = models.CharField(50)

    def __str__(self):
        return self.types

class list_report(models.Model):
    no = models.IntegerField()
    destination = models.CharField(100)
    delivery_date = models.DateField()
    delivery_note = models.ForeignKey(delivery_note, on_delete=models.CASCADE)
    remake = models.CharField()
    Header = models.ForeignKey(Header, on_delete=models.CASCADE)

    def __str__(self):
        return self.no

class delivery_note(models.Model):
    no = models.CharField(50)

    def __str__(self):
        return self.no