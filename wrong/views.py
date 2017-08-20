from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Occurrence
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.shortcuts import render

# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class CreateOccurrence(CreateView):
    model = Occurrence
    fields = ['TimeWrong', 'Subject', 'Details']


def index(request):
        all_occurrences = Occurrence.objects.all().order_by("-pk")
        total_minutes_wrong = 0
        for wrong in all_occurrences:
            total_minutes_wrong += wrong.TimeWrong

        minutes_in_year = 525600
        minutes_right = minutes_in_year - total_minutes_wrong
        percentage_right = (minutes_right / minutes_in_year) * 100

        context = {
            'all_occurrences': all_occurrences,
            'percentage_right': percentage_right,
            'total_minutes_wrong': total_minutes_wrong,
        }
        query = request.GET.get("q")
        if query:
            all_occurrences = all_occurrences.filter(
                Q(Subject__icontains=query) |
                Q(Details__icontains=query))
            return render(request, 'wrong/wrong_view.html', {
                'all_occurrences': all_occurrences,
            })
        else:
            return render(request, 'wrong/wrong_view.html', context)




class WrongDetail(generic.DetailView):
    model = Occurrence
    template_name = 'wrong/wrong_detail.html'


@method_decorator(csrf_exempt, name='dispatch')
class WrongUpdate(UpdateView):
    model = Occurrence
    fields = ['TimeWrong', 'Subject', 'Details']


@method_decorator(csrf_exempt, name='dispatch')
class WrongDelete(DeleteView):
    model = Occurrence
    success_url = reverse_lazy('wrong:wrong-list')
