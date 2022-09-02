from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testapp.models import Company
#from django.core.urls import revere_lazy
from django.urls import reverse_lazy, reverse

# Create your views here.

class Company_name(ListView):
    model = Company

    # default html page->company_list.html

class Comany_Detail_View(DetailView):
    model = Company
    # default html page->company_detail.html

class CompanyCreateView(CreateView):
    model = Company
    fields = ('name','location','ceo')
    # default html page->company_form.html

class CompanyUpdateView(UpdateView):
    model = Company
    fields = ('name','ceo')

class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('companies')
    # default html page->company_confirm_delete.html
    #why revere_lazy
    #it will wait until deletion completed
