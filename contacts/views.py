from django.shortcuts import render
from .models import Contact


def contacts_list(request):
    contact_list = Contact.objects.order_by("first_name")
    contact_dict = {"contacts": contact_list}
    return render(request, "contacts/index.html", context=contact_dict)


def contact_details(request, contact_id):
    return render(request, "contacts/contacts.html")


def help_page(request):
    return render(request, "contacts/help.html")
