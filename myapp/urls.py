from django.urls import include, path
from myapp import views
from myapp.views import GeneratePdf

urlpatterns = [
    path('',views.resume_build),
    path('resumelist/',views.resume_list),
    path('resume/<int:id>',views.view_resume,name="resume"),
    path('generate-pdf/', GeneratePdf.as_view(), name='generate-pdf'),

]
