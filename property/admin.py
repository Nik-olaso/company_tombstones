from django.contrib import admin
from .models import Tombstone, Users


@admin.register(
    Users,
    Tombstone,
)
class Users(admin.ModelAdmin):
    def queryset(self, request):
        queryset = Users.objects.all()
        return queryset


class Tombstone(admin.ModelAdmin):
    def queryset(self, request):
        queryset = Tombstone.objects.all()
        return queryset
