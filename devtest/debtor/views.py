from django.shortcuts import render, get_object_or_404
#from chartit import DataPool, Chart
#from chartit import PivotDataPool, PivotChart
from .models import tbl_due_listing, tbl_profiles
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Context,loader
from django.views.generic import TemplateView
#from .tables  import super_table
#from django_tables2   import RequestConfig
from django.db.models import Sum, Avg, Min, Max

class debtors_table(TemplateView):
    template_name = 'debtor/table1.html'

    def get_context_data(self, **kwargs):
        context = super(debtors_table, self).get_context_data(**kwargs)
        context['my_tables']= tbl_profiles.objects.all()[:1000]
        return context

class customer_profile_table(TemplateView):
    template_name = 'debtor/table2.html'

    def get_context_data(self, **kwargs):
        context = super(customer_profile_table, self).get_context_data(**kwargs)
        context['my_tables']= tbl_due_listing.objects.all()[:1000]
        return context


# Create your views here.
