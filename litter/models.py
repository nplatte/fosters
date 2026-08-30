from django.db import models
from datetime import date

class Cat(models.Model):

    name = models.CharField(max_length=30)
    estimated_date_of_birth = models.DateField(blank=True, null=True)
    microchip = models.CharField(max_length=30, blank=True, null=True)
    microchip_inserted_on = models.DateField(blank=True, null=True)
    internal_id = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=30, blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True)
    litter = models.ForeignKey('Litter', on_delete=models.SET_NULL,blank=True, null=True)


class Litter(models.Model):

    name = models.CharField(max_length=50, default="")


class Vaccination(models.Model):

    name = models.CharField(max_length=50, default="")
    brand = models.CharField(max_length=50, blank=True, null=True)
    serial_number = models.CharField(max_length=50, blank=True, null=True)
    date_given = models.DateField(default=date.today)
    next_due = models.JSONField(blank=True, null=True)


class Test(models.Model):

    name = models.CharField(max_length=50, default="")
    date_administered = models.DateField(default=date.today)
    result = models.CharField(max_length=100, blank=True, null=True)


class Preventative(models.Model):

    type = models.CharField(max_length=30, default="")
    brand = models.CharField(max_length=30, blank=True, null=True)
    dosage = models.CharField(max_length=30, blank=True, null=True)
    date_given = models.DateField(default=date.today)
    next_due = models.DateField(blank=True, null=True)



class Treatment(models.Model):

    type = models.CharField(max_length=30, default="")
    issue = models.CharField(max_length=30, default="")
    dosage = models.CharField(max_length=30, blank=True, null=True)
    frequency = models.CharField(max_length=50, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)


class Exam(models.Model):

    type = models.CharField(max_length=100, default="")
    date_admitted = models.DateField(default=date.today)
    date_picked_up = models.DateField(blank=True, null=True)
    vet = models.CharField(max_length=50, blank=True, null=True)
    taken_by = models.CharField(max_length=30, default="Kate")
    notes = models.TextField(blank=True, null=True)



class Weight(models.Model):

    weight = models.IntegerField(default=0)
    unit = models.CharField(max_length=30, choices=[('g', 'g'), ('lb', 'lb')], default="lb")
    date = models.DateField(default=date.today)
    time = models.CharField(max_length=30, choices=[('am', 'am'), ('pm', 'pm')], blank=True, null=True)
