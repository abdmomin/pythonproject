from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from .forms import UserRegisterForm, UserUpdateForm, ContactForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hello {username}! Your account has been created. Please log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'Register'})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
        'title': 'Profile',
    }
    return render(request, 'users/profile.html', context)




@login_required
def contact(request):
    if request.method == 'GET':
        c_form = ContactForm()
    else:
        c_form = ContactForm(request.POST)
        if c_form.is_valid():
            subject = c_form.cleaned_data['subject']
            from_email = c_form.cleaned_data['from_email']
            message = c_form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['abd.almomin@gmail.com'])
                messages.success(request, f'Message Sent!')
            except BadHeaderError:
                messages.danger(request, f'Unable to send message!')
            return redirect('contact')
    return render(request, "users/contact.html", {'c_form': c_form, 'title': 'Contact'})
