# contacts/urls.py
from django.urls import path
from .views import contacts_list, contact_details, help_page

urlpatterns = [
    path("", contacts_list, name="contacts_list"),
    path("contacts/<int:contact_id>/", contact_details, name="contact_details"),
    path("help/", help_page, name="help_page"),
]
