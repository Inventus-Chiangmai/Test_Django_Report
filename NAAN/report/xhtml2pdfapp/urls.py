
from django.contrib import admin
from django.urls import path, include

from .views import truck_control_pdf, replacement_order_pdf, delivery_note_pdf

urlpatterns = [
    path('generate/truck_control/',truck_control_pdf.as_view()),
    path('generate/replacement_order/',replacement_order_pdf.as_view()),
    path('generate/delivery_note/',delivery_note_pdf.as_view()),
]