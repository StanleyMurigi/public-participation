from django.contrib import admin
from .models import UserView, Comment, Vote, Profile, Discussion
# Register your models here.

admin.site.register(Discussion)
admin.site.register(UserView)
admin.site.register(Comment)
admin.site.register(Vote)
admin.site.register(Profile)
