from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Quotes
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.db.models import Q

# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class CreateQuote(CreateView):
    model = Quotes
    fields = ['Person', 'Quote', 'DateTime']


class QuoteView(generic.ListView):
    template_name = 'quotes/quotes_view.html/'

    def get_queryset(self):
        qs = Quotes.objects.all().order_by("-pk")
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(Quote__contains=query) |
                Q(Person__icontains=query)
            )
        return qs

    context_object_name = 'quotes'


class QuoteDetail(generic.DetailView):
    model = Quotes
    template_name = 'quotes/quote_detail.html'


@method_decorator(csrf_exempt, name='dispatch')
class QuoteUpdate(UpdateView):
    model = Quotes
    fields = ['Person', 'Quote', 'DateTime']


@method_decorator(csrf_exempt, name='dispatch')
class QuoteDelete(DeleteView):
    model = Quotes
    success_url = reverse_lazy('quotes:quote-list')
