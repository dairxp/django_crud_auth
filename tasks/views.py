from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


# Create your views here.
def helloworld(request):
  title = "hello world"
  return render(request, "signup.html",{
    "form": UserCreationForm()}
  )

def bye(request):
  return render(request, "bye.html")
