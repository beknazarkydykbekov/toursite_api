from django.contrib import admin
from .models import Tour, Order, TourImage


admin.site.register(Order)


class TourImageAdmin(admin.StackedInline):
    model = TourImage

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    inlines = [TourImageAdmin]

    class Meta:
        model = Tour

@admin.register(TourImage)
class TourImageAdmin(admin.ModelAdmin):
    pass