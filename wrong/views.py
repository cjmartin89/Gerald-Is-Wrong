
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Occurrence
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator

# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class CreateOccurrence(CreateView):
    model = Occurrence
    fields = ['TimeWrong', 'Subject', 'Details']


class WrongView(generic.ListView):
    template_name = 'wrong/wrong_view.html'

    def get_queryset(self):
        qs = Occurrence.objects.all().order_by("-pk")
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(Subject__icontains=query)
        return qs

    # def get_total_time_wrong:
    #     total_time_wrong = 0
    #     total_time_wrong += Occurrence.TimeWrong
    #     return  total_time_wrong

    context_object_name = 'wrongs'


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


# def percentage_view(request):
#     occurrences = Occurrence.objects.all()
#
#     total_minutes_wrong = 1
#
#     context = {
#         'total_minutes_wrong' : total_minutes_wrong
#     }
#
#     # for wrong in occurrences:
#     #     total_minutes_wrong += Occurrence.TimeWrong
#
#     render(request, 'wrong/performance_view.html', context )