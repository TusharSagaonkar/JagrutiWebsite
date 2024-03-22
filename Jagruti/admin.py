from django.contrib import admin
from .models import Employee,SocietyInformation

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'level', 'image')  # Define fields to display in the list view
    #verbose_name_plural = 'Board Of Director'  # Change the display name in the admin interface
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.order_by('level', 'name')  # Sort by level, then by name
        return queryset

class SocietyInformationAdmin(admin.ModelAdmin):
    list_display = ('data_heading', 'detail_info')  # Display all fields in the list view

  # Register models with their respective admin classes
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(SocietyInformation, SocietyInformationAdmin)


from .models import UploadedFile

@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'upload_date', 'file')
    search_fields = ('name', 'upload_date')


from .models import Scheme, Tenure

class TenureInline(admin.TabularInline):
    model = Tenure

class SchemeAdmin(admin.ModelAdmin):
    inlines = [
        TenureInline,
    ]

admin.site.register(Scheme, SchemeAdmin)
