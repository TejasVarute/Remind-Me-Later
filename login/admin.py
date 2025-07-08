from django.contrib import admin
from .models import UserData, Developer

admin.site.register(UserData)

@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        self.first_name, self.last_name = str(Developer.objects.get()).split()
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and obj.first_name == self.first_name and obj.last_name == self.last_name:
            return False
        return super().has_delete_permission(request, obj)
    
    def get_readonly_fields(self, request, obj=None):
        if obj and obj.first_name == self.first_name and obj.last_name == self.last_name:
            return [f.name for f in self.model._meta.fields]
        return super().get_readonly_fields(request, obj)