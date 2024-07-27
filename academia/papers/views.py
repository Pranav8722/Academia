from django.shortcuts import render
from .models import Paper

def papers_list(request):
    query = request.GET.get('q')
    if query:
        papers = Paper.objects.filter(title__icontains=query)
    else:
        papers = Paper.objects.all()
    return render(request, 'papers/papers_list.html', {'papers': papers})
