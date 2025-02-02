from django.contrib import admin
from .models import FAQ

# Register the FAQ model in the admin
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'question_hi', 'question_bn')

admin.site.register(FAQ, FAQAdmin)


