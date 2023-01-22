from datetime import timezone
from django.db import models
from indian_cities.dj_city import cities
from geosky import geo_plug
from django.contrib.auth.models import User
from django.utils import timezone


# # Create your models here.
# state_choices = (("Andhra Pradesh", "Andhra Pradesh"), ("Arunachal Pradesh ", "Arunachal Pradesh "), ("Assam", "Assam"), ("Bihar", "Bihar"), ("Chhattisgarh", "Chhattisgarh"), ("Goa", "Goa"), ("Gujarat", "Gujarat"), ("Haryana", "Haryana"), ("Himachal Pradesh", "Himachal Pradesh"), ("Jammu and Kashmir ", "Jammu and Kashmir "), ("Jharkhand", "Jharkhand"), ("Karnataka", "Karnataka"), ("Kerala", "Kerala"), ("Madhya Pradesh", "Madhya Pradesh"), ("Maharashtra", "Maharashtra"), ("Manipur", "Manipur"), ("Meghalaya", "Meghalaya"), ("Mizoram", "Mizoram"), ("Nagaland", "Nagaland"), ("Odisha", "Odisha"),
#                  ("Punjab", "Punjab"), ("Rajasthan", "Rajasthan"), ("Sikkim", "Sikkim"), ("Tamil Nadu", "Tamil Nadu"), ("Telangana", "Telangana"), ("Tripura", "Tripura"), ("Uttar Pradesh", "Uttar Pradesh"), ("Uttarakhand", "Uttarakhand"), ("West Bengal", "West Bengal"), ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"), ("Chandigarh", "Chandigarh"), ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"), ("Daman and Diu", "Daman and Diu"), ("Lakshadweep", "Lakshadweep"), ("National Capital Territory of Delhi", "National Capital Territory of Delhi"), ("Puducherry", "Puducherry"))

class Stops(models.Model):
    stop_id = models.AutoField(primary_key=True)
    route_number = models.IntegerField(unique=True)
    scheduled_start_time = models.TimeField()
    street = models.CharField(max_length=30, null=True, blank=True)
    apt_plot = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(choices=cities, null=False, max_length=20)
    state = geo_plug.all_Country_StateNames()
    zip_code = models.IntegerField(null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    scheduled_arrival_time = models.TimeField()
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s %s" % (self.stop_id, self.route_number)

    class Meta:
        db_table = "Stops"


class School(models.Model):
    id = models.AutoField(primary_key=True)
    school_id = models.CharField(max_length=30, unique=True)
    stop_id = models.ForeignKey(
        Stops,
        to_field="stop_id",
        related_name="stop_id_school",
        on_delete=models.CASCADE,
    )
    school_name = models.CharField(max_length=30, null=True, blank=True)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    updated_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='updated_by_user')
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='created_by_user')
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s %s" % (self.school_id, self.school_name)

    class Meta:
        db_table = "School"

