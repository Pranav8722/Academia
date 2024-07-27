from django.shortcuts import render
from .models import StudyGroup

def study_groups_list(request):
    query = request.GET.get('q')
    if query:
        study_groups = StudyGroup.objects.filter(name__icontains=query)
    else:
        study_groups = StudyGroup.objects.all()
    return render(request, 'study_groups/study_groups_list.html', {'study_groups': study_groups})
