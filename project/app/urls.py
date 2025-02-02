

from django.urls import path
from . import views

urlpatterns = [
    # Admin URLs
    path('custom-admin/', views.custom_admin_dashboard, name='custom_admin'),
    path('custom-admin/add/', views.add_faq, name='add_faq'),
    path('custom-admin/update/<int:faq_id>/', views.update_faq, name='update_faq'),
    path('custom-admin/delete/<int:faq_id>/', views.delete_faq, name='delete_faq'),

    # Public-facing URLs
    path('', views.welcome, name='welcome'),  # Welcome page
    path('faqs/', views.faq_page, name='faq_list'),  # FAQ list page (updated to match view name)
]
