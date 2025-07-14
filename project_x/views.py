from django.shortcuts import render
from counter.models import VisitCounter

def index(request):
    counter, created = VisitCounter.objects.get_or_create(id=1)
    counter.count += 1
    counter.save()
    return render(request, 'index.html', {'counter': counter.count})
