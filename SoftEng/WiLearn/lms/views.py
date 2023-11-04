from django.shortcuts import render, redirect
from .forms import AnnouncementForm, CourseForm, ProfileForm
from .models import Announcements, Courses, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from PIL import Image

# Create your views here.
User = get_user_model()
COMPARISON_DICT = {10: "00000", 100: "0000", 1000: "000", 10000: "00", 100000: "0"}

@login_required
def dashboard(request):
    user = request.user
    print(user.id)
    course = Courses.objects.filter(user_id=user.id)
    announcement = Announcements.objects.filter(user_id=user.id)

    return render(request, 'lms/dashboard.html', {'course': course, 'announcement': announcement})

@login_required
def inbox(request):
    return render(request, 'lms/inbox.html')


@login_required
def post_announcements(request):
    if request.method == 'POST':
        announcement_form = AnnouncementForm(request.POST)
        if announcement_form.is_valid():
            user = request.user
            teacher = User.objects.get(email=user.email)
            announcement = announcement_form.save(commit=False)

            title = announcement_form.cleaned_data['Announcement_Title']
            text = announcement_form.cleaned_data['Announcement_Content']
            announcement.title = title
            announcement.text = text
            announcement.user = teacher
            announcement.save()
            return redirect('lms:dashboard')
        else:
            print(announcement_form)
            print(announcement_form.errors)
            return render(request, 'lms/postannouncement.html', {'form': announcement_form})

    form = AnnouncementForm()
    return render(request, 'lms/postannouncement.html', {'form': form})



@login_required
def add_course(request):
    if request.method == 'POST':
        course_form = CourseForm(request.POST, request.FILES)
        print("HEELO")
        if course_form.is_valid():
            user = request.user
            teacher = User.objects.get(email=user.email)
            if teacher is not None:
                course = create_course_id(course_form, teacher)
                course.save()

            return redirect('lms:dashboard')
        else:
            print(course_form)
            print(course_form.errors)
            # put errors here to display in form
    form = CourseForm()
    return render(request, 'lms/addcourse.html', {'form': form})


def create_course_id(course_form,teacher):
    last = Courses.objects.all().last()
    if last:
        last.id += 1
        latest_id = last.id
    else:
        latest_id = 1

    course = course_form.save(commit=False)
    course.user = teacher
    for key, val in COMPARISON_DICT.items():
        if latest_id < key:
            course.course_id = f"{teacher.last_name}.{val}{latest_id}"
            break
        elif latest_id >= 100000:
            course.course_id = f"{teacher.last_name}.{latest_id}"
            break
    return course



@login_required
def profile(request):
    user = request.user
    prof = Profile.objects.filter(user_id=user.id).first()
    if not prof:
        pro = Profile.objects.create(user_id=user.id)
        pro.save()
        prof = Profile.objects.get(user_id=user.id)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=prof)
        if form.is_valid():
            if form.cleaned_data['image'] is not None:
                prof.img.delete(save=True)
                prof.img = form.cleaned_data['image']

            if form.cleaned_data['biography'] != '':
                prof.biography = form.cleaned_data['biography']

            if form.cleaned_data['contacts'] != '':
                prof.contacts = form.cleaned_data['contacts']

            prof.save()

    else:
        form = ProfileForm(instance=prof)

    return render(request, 'lms/profile.html', {'form': form, 'prof': prof})


@login_required
def inside_module(request):
    return render(request, 'lms/inside_module.html')

