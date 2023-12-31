from django import forms
from .models import Announcements, Courses, Profile, Module, Assignments
from django_quill.forms import QuillFormField


class AnnouncementForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'announce'}))
    text = QuillFormField(widget=forms.TextInput(attrs={'class': 'announce'}))

    class Meta:
        model = Announcements
        fields = ['title', 'text']
        labels = {"title": "Announcement Title", "text": "Announcement Content"}





class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ('img',
                  'name',
                  'desc',
                  'enrollment_start',
                  'enrollment_end',
                  'course_start',
                  'course_end',
                  'lab_time',
                  'lab_day',
                  'lecture_time',
                  'lecture_day',)
        exclude = ['user']
        labels = {
            "img": "Course Image",
            "name": "Course Name",
            "desc": "Course Description",
            "enrollment_start": "Enrollment Start Date",
            "enrollment_end": "Enrollment End Date",
            "course_start": "Course Start Date",
            "course_end": "Course End Date",
            "lab_time": "Laboratory Time",
            "lab_day": "Laboratory Day",
            "lecture_time": "Lecture Time",
            "lecture_day": "Lecture Day",
        }

        widgets = {
            "img": forms.FileInput(attrs={'id': "courseImage"}),
            "name": forms.TextInput(attrs={'id': "courseName"}),
            "desc": forms.Textarea(attrs={'id': "courseDescription"}),
            "enrollment_start": forms.DateInput(attrs={'id': "enrollmentStartDate",'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)'}),
            "enrollment_end": forms.DateInput(attrs={'id': "enrollmentEndDate",'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)'}),
            "course_start": forms.DateInput(attrs={'id': "courseStartDate",'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)'}),
            "course_end": forms.DateInput(attrs={'id': "courseEndDate",'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)'}),"lab_time": forms.TextInput(attrs={'id': "labTime"}),
            "lab_day": forms.Select(attrs={'id': "labDay"}),
            "lecture_time": forms.TextInput(attrs={'id': "lectureTime"}),
            "lecture_day": forms.Select(attrs={'id': "lectureDay"}),

        }


class ProfileForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'img-pf'}))
    biography = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'pf'}))
    contacts = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'pf'}))

    class Meta:
        model = Profile
        fields = ['image', 'biography', 'contacts']


class ModuleForm(forms.ModelForm):
    module_title = forms.CharField(widget=forms.TextInput(attrs={'id': 'moduleName', 'class': 'pf'}))
    module_content = QuillFormField(widget=forms.Textarea(attrs={'id': 'moduleContent', 'class': 'pf'}))

    labels = {
        "module_title": "Module Title",
        "module_content": "Module Content",
    }

    class Meta:
        model = Module
        fields = ['module_title', 'module_content']


class EditModule(forms.ModelForm):
    module_content = QuillFormField(widget=forms.Textarea(attrs={'id': 'content', 'class': 'pf'}))

    labels = {
        "module_content": "Module Content",
    }

    class Meta:
        model = Module
        exclude = ['module_title']
        fields = ['module_content']


class AssignmentForm(forms.ModelForm):
    assign_title = forms.CharField(widget=forms.TextInput(attrs={'class': 'announce'}))
    assign_content = QuillFormField(widget=forms.TextInput(attrs={'class': 'announce'}))

    class Meta:
        model = Assignments
        fields = ['assign_title', 'assign_content']
        labels = {"assign_title": "Assignment Title", "assign_content": "Assignment Content"}
