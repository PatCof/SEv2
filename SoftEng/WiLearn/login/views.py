from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .backends import EmailBackend
from .forms import LoginForm
from django.urls import reverse
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy


# Create your views here.
def main(request):
    next_param = request.GET.get('next', reverse('lms:dashboard'))
    print(f"Auth: {request.user.is_authenticated}")

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = EmailBackend().authenticate(request, username=email, password=password)
            if user is not None:
                print(f"USER:{user}")
                login(request, user=user, backend='login.backends.EmailBackend')
                print(request.user.is_authenticated)
                return redirect(next_param)
            else:
                # messages.error(request, messages.ERROR,'User does not Exist!')
                messages.error(request,'User does not Exist!')
                return render(request, 'login/index.html', {'form': form})

     # CONCERN: SINCE POPUP NOT SURE PAANO IPAPAKITA NA MAY ERROR SA FORMS// FIX THE PROPER FORMS
    else:
        form = LoginForm()
        return render(request, 'login/index.html', {'form': form})



def courses(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = EmailBackend().authenticate(request, username=email, password=password)
            if user:
                login(request, user=user, backend='login.backends.EmailBackend')
                return redirect('lms:dashboard')
        else:
            form = LoginForm()
            messages.error(request, 'Invalid login credentials. Please try again.')
            return render(request, 'login/courses.html', {'form': form})

    form = LoginForm()
    return render(request, 'login/courses.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('login:main')


class PassResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('login:password_reset_done')

class PassResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class PassResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('login:password_reset_confirm')

class PassResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'