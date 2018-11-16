from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from accounts.forms import (
							RegisterationForm,
							EditProfileForm,
							StudentProfileForm,
						)
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import Assignment


def student_asmt(request):
	asmts = Assignment.objects
	return render(request, 'students/view_student_asmt.html',{'asmts':asmts})