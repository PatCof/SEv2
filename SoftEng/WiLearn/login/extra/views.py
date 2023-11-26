# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponseRedirect
# from django.shortcuts import render, redirect
# from django.contrib.auth import login
# from django.contrib import messages
# from .backends import EmailBackend
# from .forms import LoginForm
# # from lms.views import dashboard
# from django.conf import settings
# from django.urls import reverse
#
# # Create your views here.
#
#
# def main(request):
#     next_param = request.POST.get('next', 'lms:dashboard')
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = EmailBackend().authenticate(request, username=email, password=password)
#             if user:
#                 print(f"USER:{user}")
#                 login(request, user=user, backend='login.backends.EmailBackend')
#                 print(request.user.is_authenticated)
#                 return redirect(next_param)
#                 # return render(request, 'lms/dashboard.html')
#
#         else:
#             return render(request, 'login/index.html', {'form': form})
#             #CONCERN: SINCE POPUP NOT SURE PAANO IPAPAKITA NA MAY ERROR SA FORMS
#     else:
#         form = LoginForm()
#         return render(request, 'login/index.html', {'form': form, 'next': next_param})
#
#
# def courses(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = EmailBackend().authenticate(request, username=email, password=password)
#             if user:
#                 login(request, user=user, backend='login.backends.EmailBackend')
#                 return redirect('lms:dashboard')
#         else:
#             form = LoginForm()
#             messages.error(request, 'Invalid login credentials. Please try again.')
#             return render(request, 'login/index.html', {'form': form})
#
#     form = LoginForm()
#     return render(request, 'login/index.html', {'form': form})
#
#
#
