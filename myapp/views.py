import os
from django.conf import settings
from django.shortcuts import get_object_or_404,redirect,render
from myapp.forms import resumeForm
from .models import resume
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.
def resume_build(request):
    form=resumeForm()
    if request.method=='POST':
        form1=resumeForm(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            return redirect('/')
    return render(request,'index.html',{'form':form})
def resume_list(request):
    data=resume.objects.all()
    return render(request, 'resume_list.html', {'data':data})
def view_resume(request,id):
   
    object=resume.objects.get(id=id)
    context={'resume':object}
    return render(request, 'resume.html', {'data':object})
    
# importing the necessary libraries
from django.http import HttpResponse
from django.views.generic import View
from .process import html_to_pdf 

#Creating a class based view
class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
         
        # getting the template
        pdf = html_to_pdf('resume.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')