from django.views.generic.edit import FormView
from .forms import FileFieldForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        user = UserProfile.objects.get(user__id=user_id)
        for afile in request.FILES.getlist('files'):
            pic = Picture()
            pic.user= user 
            pic.image = afile
            pic.save()

        # return redirect("path_to_where_you_want_to_go_after_upload")
    return render(request=request,template_name='index.html') 