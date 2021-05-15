from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import PersonForm
from .models import Person
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


def home(request):
    person = Person.objects.first()
    return render(request, 'home.html', {'title': 'Cico', 'person': person})

########### register here #####################################


def register(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            # password = form.cleaned_data.get('password')
            # phoneno = form.cleaned_data.get('phoneno')
            # details = form.cleaned_data.get('details')
            ######################### mail system #############################
            htmly = get_template('Email.html')
            d = {'username': username}
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(
                subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = PersonForm()
    return render(request, 'signup.html', {'form': form, 'title': 'register here'})

################ login forms###################################################


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        person = Person.objects.first()
        user = person.verify(username, password)
        if user is not None:
            return redirect('check')
        else:
        	return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'title': 'log in'})

def Logout(request):
    person = Person.objects.first()
    person.is_authenticated=False
    person.save()
    return render(request, 'home.html')

def check(request):
    person = Person.objects.first()
    if "checkin" in request.POST:
        person.checkin()
        return redirect('home')
    if "checkout" in request.POST:
        person.checkout()
        return redirect('home')
    return render(request, 'check.html', {'persons': person})
