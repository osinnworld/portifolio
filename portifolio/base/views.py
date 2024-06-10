from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('message')
        number = request.POST.get('number')

        if not (1 < len(name) < 30):
            messages.error(request, 'Length of name should be greater than 1 and less than 30 characters')
            return redirect('home')

        if not (1 < len(email) < 40):
            messages.error(request, 'Invalid email. Please try again.')
            return redirect('home')

        if not (1 < len(number) < 13):
            messages.error(request, 'Invalid number. Please try again.')
            return redirect('home')

        Contact.objects.create(name=name, email=email, content=content, number=number)
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('home')

    return redirect('home')
