from django.db import models

# Create your models here.


class Users_table(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    user_name = models.CharField(max_length = 20, primary_key = True)
    password = models.CharField(max_length = 20)
    phone_no = models.CharField(max_length = 10)
    address = models.CharField(max_length = 100)
    def __str__(self):
        return self.user_name

class visitor_entry_table(models.Model):
    name = models.CharField(max_length = 20)
    phone_number = models.CharField(max_length = 10)
    staff_to_contact = models.CharField(max_length = 20)
    staff_phone_number = models.CharField(max_length = 10)
    purpose = models.CharField(max_length = 200)
    entrance_date = models.DateField(auto_now=False, auto_now_add=False)
    entrance_time = models.TimeField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey(Users_table, on_delete = models.CASCADE)
    def __str__(self):
        return "person"


class visitor_exit_table(models.Model):
    receipt_no = models.OneToOneField(visitor_entry_table, on_delete = models.CASCADE, primary_key = True)
    name = models.CharField(max_length = 20)
    exit_time = models.TimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.name


class staff_vehicle_entry_table(models.Model):
    name =  models.CharField(max_length = 20)
    vehicle_number =  models.CharField(max_length = 20)
    phone_number =  models.CharField(max_length = 20)
    staff_type_choices = (("Regular", "Regular"),("Guest","Guest"))
    staff_type = models.CharField(max_length = 10, choices = staff_type_choices, default = "Regular")
    staff_to_contact = models.CharField(max_length = 20, blank = True)
    staff_phone_number = models.CharField(max_length = 20, blank = True)
    purpose = models.CharField(max_length = 200, blank = True)
    entrance_date = models.DateField(auto_now=False, auto_now_add=False)
    entrance_time = models.TimeField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey(Users_table, on_delete = models.CASCADE)
    def __str__(self):
        return "staff_vehicle"

class staff_vehicle_exit_table(models.Model):
    receipt_no = models.OneToOneField(staff_vehicle_entry_table, on_delete = models.CASCADE, primary_key = True)
    name = models.CharField(max_length = 200)
    exit_time = models.TimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.name

class other_vehicle_entry_table(models.Model):
    name = models.CharField(max_length = 20)
    vehicle_number =  models.CharField(max_length = 20)
    phone_number =  models.CharField(max_length = 20)
    staff_to_contact = models.CharField(max_length = 20)
    staff_phone_number = models.CharField(max_length = 10)
    purpose = models.CharField(max_length = 200)
    entrance_date = models.DateField(auto_now=False, auto_now_add=False)
    entrance_time = models.TimeField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey(Users_table, on_delete = models.CASCADE)
    def __str__(self):
        return "other_vehicle"

class other_vehicle_exit_table(models.Model):
    receipt_no = models.OneToOneField(other_vehicle_entry_table, on_delete = models.CASCADE, primary_key = True)
    name = models.CharField(max_length = 20)
    exit_time = models.TimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.name
