from django.db import models
from django.utils import timezone
import datetime


class User(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    real_name = models.CharField(unique=False, max_length=235, blank=False, null=False)
    tz = models.CharField(max_length=235, blank=False, null=False)
    
    def __str__(self):
        return self.id
    
    def current_activity_data(self):
        activity_obj = ActivityPeriod.objects.filter(uid=self.id)
        for row in activity_obj:
            row.start_time = row.start_time.strftime("%b %d %Y %I:%M%p")
            row.end_time= row.end_time.strftime("%b %d %Y %I:%M%p")
        return activity_obj
class ActivityPeriod(models.Model):
    uid = models.ForeignKey('User', models.DO_NOTHING, null=True, blank=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
