from django.shortcuts import render
from .models import VisitCounter

def index(request):
    counter = VisitCounter.objects.get(pk=1)
    counter.count += 1
    counter.save()
    print(counter.count)
    return render(request, 'index.html', context={
        'count': counter.count,
    })