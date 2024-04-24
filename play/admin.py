from django.contrib import admin
from .models import Play, Seats


# Register your models here.
@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    pass


@admin.register(Seats)
class SeatsAdmin(admin.ModelAdmin):
    pass
