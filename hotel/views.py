from django.shortcuts import render, redirect
from hotel.forms import ContactForm, MyForm
from django.core.mail import send_mail
from django.template import Context
from django.template.loader import get_template


def index(request):
    form_class = ContactForm
    book_class = MyForm
    context = {
        'appName': 'Home',
        'form': form_class,
        'book': book_class
    }
    return render(request, 'hotel/index.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            contact_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            details = form.cleaned_data['details']

            # template = get_template('hotel/contact_template')
            # context = Context({
            #     'contact_name': name,
            #     'contact_email': contact_email,
            #     'form_content': details,
            # })
            # content = template.render(context)

            send_mail(
                '[ENQUIRY] ' + name + ': ' + subject,
                details,
                contact_email,
                ['test@lao-orchid.com'],
                fail_silently=False,
            )

            return redirect('index')

    return render(request, 'hotel/contact.html')


def booking(request):
    form_class = ContactForm
    context = {
        'appName': 'Home',
        'form': form_class
    }
    return render(request, 'hotel/index.html', context)
