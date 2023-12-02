from django.shortcuts import render, redirect
from .forms import AnnouncementForm, CourseForm, ProfileForm, ModuleForm, EditModule, AssignmentForm
from .models import Announcements, Courses, Profile, Module, Assignments
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import date

from PIL import Image

# Create your views here.
User = get_user_model()
COMPARISON_DICT = {10: "00000", 100: "0000", 1000: "000", 10000: "00", 100000: "0"}


@login_required
def dashboard(request):
    user = request.user
    course = Courses.objects.filter(user_id=user.id)
    announcement = Announcements.objects.filter(user_id=user.id)
    current_date = date.today()
    if request.method == 'POST':
        if 'announce_delete' in request.POST:
            print("HELLO")
            an_id = request.POST.get('id_val')
            Announcements.objects.filter(id=an_id).delete()

        elif 'course_delete' in request.POST:
            print("HIII")
            c_id = request.POST.get('id_val2')
            print(c_id)
            Courses.objects.filter(id=c_id).delete()

    context = {
                'course': course,
               'announcement': announcement,
               'date': current_date,
               }

    return render(request, 'lms/dashboard.html', context=context)


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

            title = announcement_form.cleaned_data['title']
            text = announcement_form.cleaned_data['text']
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
def edit_announcements(request, a_id):
    announce = Announcements.objects.filter(id=a_id).first()
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, instance=announce)
        if form.is_valid():
            text = form.cleaned_data['text']
            form.text = text
            form.save()
            return redirect('lms:dashboard')
        else:
            return render(request, 'lms/edit_announcement.html', {'form': form})
    form = AnnouncementForm(instance=announce)
    return render(request, 'lms/edit_announcement.html', {'form': form})


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


def create_course_id(course_form, teacher):
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
def edit_course(request, id):
    course = Courses.objects.filter(id=id).first()
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            course = form.save(commit=False)
            if form.cleaned_data['img'] is not None:
                course.img = form.cleaned_data['img']

            course.save()
            return redirect('lms:dashboard')
        else:
            print(form)
            print(form.errors)
            # put errors here to display in form
    form = CourseForm(instance=course)
    return render(request, 'lms/edit_course.html', {'form': form})


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

        return render(request, 'lms/profile.html', {'form': form, 'prof': prof})

    else:
        form = ProfileForm(instance=prof)

    return render(request, 'lms/profile.html', {'form': form, 'prof': prof})


@login_required
def inside_module(request, id):
    module = Module.objects.filter(course_id_id=id)
    assign = Assignments.objects.filter(course_id=id)
    m1, m2, m3, m4, m5, m6 = None, None, None, None, None, None,
    if module:
        m1 = [m for m in module if m.module_number == 1]
        m2 = [m for m in module if m.module_number == 2]
        m3 = [m for m in module if m.module_number == 3]
        m4 = [m for m in module if m.module_number == 4]
        m5 = [m for m in module if m.module_number == 5]
        m6 = [m for m in module if m.module_number == 6]

    context = {
        'id': id,
        'mod1': m1,
        'mod2': m2,
        'mod3': m3,
        'mod4': m4,
        'mod5': m5,
        'mod6': m6,
        'assign': assign
    }

    return render(request, 'lms/inside_module.html', context=context)


@login_required
def create_module(request, id, mod_num):
    if request.method == 'POST':
        create_form = ModuleForm(request.POST)
        if create_form.is_valid():
            mod = create_form.save(commit=False)
            course = Courses.objects.filter(id=id).first()
            module = Module.objects.filter(course_id_id=id, module_number=mod_num).last()
            if module:
                mod.module_page = module.module_page + 1
            else:
                mod.module_page = 1

            mod.course_id = course
            mod.module_number = mod_num
            mod.save()

            return redirect(reverse('lms:module', kwargs={'id': id}))
        else:
            print(create_form)
            print(create_form.errors)
            # put errors here to display in form/ Message framework django :|
    form = ModuleForm()
    return render(request, 'lms/createmodule.html', {'form': form, 'id': id})


@login_required
def modify_module(request, id, mod_num, mod_page):
    course = Courses.objects.filter(id=id).first()
    mod = Module.objects.filter(module_number=mod_num, course_id_id=id, module_page=mod_page).first()
    if request.method == 'POST':
        form = ModuleForm(request.POST, instance=mod)
        if form.is_valid():
            content = form.cleaned_data['module_content']
            mod.module_content = content
            mod.save()

    else:
        form = ModuleForm(instance=mod)

    prev_mod = Module.objects.filter(module_number=mod_num, course_id_id=id, module_page__lt=mod_page).last()
    next_mod = Module.objects.filter(module_number=mod_num, course_id_id=id, module_page__gt=mod_page).first()

    context = {
        'form': form,
        'course_name': course.name,
        'mod': mod,
        'prev_mod': prev_mod,
        'next_mod': next_mod,
        'id': id,
    }
    return render(request, 'lms/modulemodify.html', context=context)


@login_required
def create_assign(request, id):
    if request.method == 'POST':
        course = Courses.objects.filter(id=id).first()
        assign_form = AssignmentForm(request.POST)
        if assign_form.is_valid():
            newest_assign = Assignments.objects.filter(course_id=id).last()

            new_assign = assign_form.save(commit=False)
            new_assign.course = course
            if newest_assign:
                new_assign.assign_num = newest_assign.assign_num + 1
            else:
                new_assign.assign_num = 1

            new_assign.assign_title = assign_form.cleaned_data['assign_title']
            new_assign.assign_content = assign_form.cleaned_data['assign_content']
            new_assign.save()

            return redirect(reverse('lms:module', kwargs={'id': id}))
        else:
            print(assign_form)
            print(assign_form.errors)
    else:
        form = AssignmentForm()
    context = {
        'form': form,
        'id': id,
    }
    return render(request, 'lms/create_assignment.html', context=context)


@login_required
def edit_assign(request, id, assign_num):
    course = Courses.objects.filter(id=id).first()
    assign = Assignments.objects.filter(assign_num=assign_num, course_id=id).first()
    form = AssignmentForm(instance=assign)

    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assign)
        if form.is_valid():
            assign.assign_title = form.cleaned_data['assign_title']
            assign.assign_content = form.cleaned_data['assign_content']
            assign.save()

    prev_assign = Assignments.objects.filter(assign_num__lt=assign_num, course_id=id).last()
    next_assign = Assignments.objects.filter(assign_num__gt=assign_num, course_id=id).first()

    context = {
        'form': form,
        'course_name': course.name,
        'assign': assign,
        'prev_assign': prev_assign,
        'next_assign': next_assign,
        'id': id,
    }
    return render(request, 'lms/edit_assignment.html', context=context)




@login_required
def logout(request):
    logout(request)
    return render(request, 'login/index.html')
