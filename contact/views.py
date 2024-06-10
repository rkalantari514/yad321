from django.shortcuts import render, redirect
from .models import ContactUs
# Create your views here.
from contact.forms import CreateContactForm


def contact_page(request):
    contact_form = CreateContactForm(request.POST or None)

    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get('full_name')
        subject = contact_form.cleaned_data.get('subject')
        text = contact_form.cleaned_data.get('text')
        ContactUs.objects.create(full_name=full_name, subject=subject, text=text, is_read=False)
        # todo : show user a success message
        contact_form = CreateContactForm()
        return redirect ('/')

    context = {
        'contact_form': contact_form,
    }

    return render(request, 'contact_us/contact_us_page.html', context)
