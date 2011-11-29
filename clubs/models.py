from django.db import models

class Location(models.Model):
    location_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __unicode__(self):
        return self.location_name

class College(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    def get_absolute_url(self):
        return "/college/%s/" % self.name_slug
    def __unicode__(self):
        return self.name

class Major(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    def get_absolute_url(self):
        return "/major/%s/" % self.name_slug
    def __unicode__(self):
        return self.name

class Advisor(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    title = models.CharField(max_length=250) 
    def __unicode__(self):
        return self.name

class Organization(models.Model):
    name = models.CharField(max_length=255)
    name_slug = models.SlugField()
    pub_date = models.DateTimeField('date published')
    pertaining_college = models.ManyToManyField(College)
    pertaining_major = models.ManyToManyField(Major)
    advisor = models.ManyToManyField(Advisor)
    meeting_dates = models.TextField()
    location = models.ForeignKey(Location)
    application = models.BooleanField()
    fee = models.BooleanField()
    def get_absolute_url(self):
        return "/club/%s/" % self.name_slug
    def __unicode__(self):
        return self.name

class Question(models.Model):
    organization = models.ForeignKey(Organization)
    question = models.CharField(max_length=255)
    answer = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.question
