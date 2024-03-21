from django.shortcuts import render, HttpResponseRedirect
from Etudiant .forms import StudentRegistration
from django.views.decorators.csrf import csrf_protect
from Etudiant.models import User 
# Create your views here.
def add_show(request):
    if request.method == 'POST':
       fm = StudentRegistration(request.POST)
       if fm.is_valid():
           nm = fm.cleaned_data['name']
           em = fm.cleaned_data['email']
           pw = fm.cleaned_data['password']
           reg = User(name = nm, email = em, password = pw) 
           fm.save()
     
    else:
       fm = StudentRegistration()
       stud = User.objects.all()
    return render(request, 'etudiant/addandshow.html',{'form':fm, 'stu':stud})

# Create your views here.
def delete_data(request, id):
    if request.method == 'POST':
       pi = User.objects.get(pk=id)
       pi.delete()
       return HttpResponseRedirect('/')   
        


