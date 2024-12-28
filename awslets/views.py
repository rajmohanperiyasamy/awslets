from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import ContactForm

# @login_required
# def home(request):
#  return render(request, "home.html", {})



def home(request):
 if request.method == "POST":
  contact_form = ContactForm(request.POST or None)
  import pdb
  pdb.set_trace()
  if contact_form.is_valid():
   contact_form.save()
   return redirect("/")
 else:
  contact_form = ContactForm()
 return render(request, "index.html", {"contact_form": contact_form})

@login_required
def signin(request):
 return redirect(home)
 # return render(request, "home.html", {})

def authView(request):
 if request.method == "POST":
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
   # form.save()
   new_user = form.save()
   new_user = authenticate(username=form.cleaned_data['username'],
                           password=form.cleaned_data['password1'],
                           )
   login(request, new_user)
   return redirect(home)
 else:
  form = UserCreationForm()
 return render(request, "registration/signup.html", {"form": form})