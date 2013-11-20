from django.db import models
from django.contrib import admin
import datetime

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    done = models.BooleanField(default=False)

class ItemAdmin(admin.ModelAdmin):
    list_display = ["name","priority","difficulty","created","done"]
    search_field = ["name"]

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __unicode__(self):
        return self.choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields':['question']}),
        ('Date information',{'fields':['pub_date'],'classes':['collapse']}),
        ]
    inlines = [ChoiceInline]


admin.site.register(Item,ItemAdmin)
admin.site.register(Poll,PollAdmin)
