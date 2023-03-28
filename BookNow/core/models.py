from django.db import models
# Create your models here.

class Meeting1(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)


class MeetingRoom1(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)    


class Event2(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)


class Event3(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)


class Event4(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)

# class Event4(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255, null=True, blank=True)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     start_time = models.TimeField()
#     end_time = models.TimeField()


