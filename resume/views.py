from django.shortcuts import render
from .forms import ContactForm
from .models import Contact


def home(request):
    if request.method == 'POST':
        filled_form = ContactForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = f"Thanks for your message"
            filled_form = ContactForm()
        else:
            note = "Sending message failed, try again"
        return render(request, 'resume/home.html', {'contactform': filled_form, 'note': note})
    else:
        form = ContactForm()
        return render(request, 'resume/home.html', {'contactform': form})

