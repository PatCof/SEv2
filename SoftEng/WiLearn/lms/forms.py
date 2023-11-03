from django import forms
from .models import Announcements, Courses, Profile
from django_quill.forms import QuillFormField


class AnnouncementForm(forms.ModelForm):
    Announcement_Title = forms.CharField(widget=forms.TextInput(attrs={'class': 'announce'}))
    Announcement_Content = QuillFormField(widget=forms.TextInput(attrs={'class': 'announce'}))
    # text = forms.CharField(widget=forms.Textarea(attrs={'id':'quill-editor'}))

    class Meta:
        model = Announcements
        fields = ['Announcement_Title', 'Announcement_Content']
        labels = {"Announcement_Title": "Announcement Title", "Announcement_Content": "Announcement Content"}

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
            "lab_day": forms.TextInput(attrs={'id': "labDay"}),
            "lecture_time": forms.TextInput(attrs={'id': "lectureTime"}),
            "lecture_day": forms.TextInput(attrs={'id': "lectureDay"}),
        }


class ProfileForm(forms.ModelForm):
    image = forms.ImageField()
    biography = QuillFormField()
    contacts = QuillFormField()

    class Meta:
        model = Profile
        fields = ['image', 'biography', 'contacts']

