from django.urls import path
from resume_generator.views import accept, resume

app_name =  "resume_generator"
urlpatterns = [
    path('', accept, name="accept"),
    path('<int:id>', resume, name="resume"),
]
