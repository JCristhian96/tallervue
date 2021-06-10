from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Models
from apps.beneficiarys.models import Beneficiario, Origin

class OriginAdmin(ImportExportModelAdmin):
    pass



class BeneficiarioAdmin(ImportExportModelAdmin):
    '''Admin View for Beneficiario'''

    list_display = ('dni', 'names', 'origin', 'created_at')
    list_filter = ('origin', )

    ordering = ('names', 'created_at')
    

admin.site.register(Beneficiario, BeneficiarioAdmin)
admin.site.register(Origin, OriginAdmin)