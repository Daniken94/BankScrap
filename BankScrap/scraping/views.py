from django.shortcuts import render
from django.views import View
from .models import Stats

# Index class is responsible for view records from database.
# In def post geting values from form and sort records by asc and desc

class Index(View):
    def get(self, request):
        stats = Stats.objects.all()
        return render(request, "index.html", {"stats": stats})
    def post(self, request):
        if str(request.POST.get("sort")) == "ASC":
            stats = Stats.objects.all().order_by('name')
            return render(request, "index.html", {"stats": stats})
        else:
            stats = Stats.objects.all().order_by('-name')
            return render(request, "index.html", {"stats": stats}) 
 