from django.shortcuts import render
from .models import Profile
from django.http import Http404, HttpResponseRedirect
# Create your views here.
def accept(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        summary = request.POST.get("summary","")
        school = request.POST.get("school","")
        degree = request.POST.get("degree","")
        university = request.POST.get("university","")
        prework = request.POST.get("prework","")
        skills = request.POST.get("skills","")
        print(name,email,phone,skills,school,university,degree,prework,summary)
        profile = Profile.objects.create(name=name, email=email, phone=phone, summary=summary,
                                degree=degree, school=school, university=university,
                                pre_work=prework,skills=skills)
        print(profile)
        return HttpResponseRedirect(f'/resume/{profile.id}')
    context = {
        "page":"resume"
    }
    return render(request,'resume_generator/accept.html',context)


def resume(request, id):
    try:
        profile = Profile.objects.all()[0]
    except:
        raise Http404
    return render(request, 'resume_generator/resume.html', {'profile':profile})