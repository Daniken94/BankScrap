from django.shortcuts import render
from django.views import View
from .models import Stats


class Index(View):
    def get(self, request):
        stats = Stats.objects.all()
        return render(request, "index.html", {"stats": stats})
    def post(self, request):
        if request.POST.get("asc"):
            stats = Stats.objects.all().order_by('name')

            return render(request, "index.html", {"stats": stats}) 


        if request.POST.get("desc"):
            stats = Stats.objects.all().order_by('-name')

            return render(request, "index.html", {"stats": stats})   
 