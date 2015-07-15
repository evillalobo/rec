from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from .models import Departamento, Categoria
from cargabase.forms import DepartamentoForm, CategoriaForm, RecursoNaturalForm,\
    RecursoCulturalForm
from cargabase.models import RecursoCultural, RecursoNatural

# Create your views here.
def index(request):
    return render(request, 'cargabase/index.html')

# Departamentos

class DepartamentoDetail(DetailView):
    model = Departamento
    
    def get_success_url(self):
        return reverse_lazy('departamento-list',
                            kwargs={'pk':self.object.departamento.id})
    
class DepartamentoCreate(CreateView):
    model = Departamento
    form_class = DepartamentoForm
    
    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(
                self.get_context_data(form = form))
    
    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form):
        return self.render_to_response(
                self.get_context_data(form = form))

class DepartamentoUpdate(UpdateView):
    model = Departamento
    form_class = DepartamentoForm
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(
                self.get_context_data(object=self.object,
                                      form=form))
        
    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form):
        return self.render_to_response(
                self.get_context_data(form = form))

class DepartamentoList(ListView):
    model = Departamento
    
    def get_context_data(self, **kwargs):
        context = super(DepartamentoList, self).get_context_data(**kwargs)
        return context
    
    def get_queryset(self):
        return ListView.get_queryset(self)

# Categorias

class CategoriaDetail(DetailView):
    model = Categoria
    
    def get_success_url(self):
        return reverse_lazy('categoria-list',
                            kwargs={'pk':self.object.categoria.id})

class CategoriaCreate(CreateView):
    model = Categoria
    form_class = CategoriaForm
    
    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(
                self.get_context_data(form = form))
    
    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form):
        return self.render_to_response(
                self.get_context_data(form = form))

class CategoriaList(ListView):
    model = Categoria
    
    def get_context_data(self, **kwargs):
        context = super(CategoriaList, self).get_context_data(**kwargs)
        context['categoria'] = Categoria.objects.all()
        return context
    
    def get_queryset(self):
        return ListView.get_queryset(self)

class CategoriaUpdate(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(
                self.get_context_data(object=self.object,
                                      form=form))
        
    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form):
        return self.render_to_response(
                self.get_context_data(form = form))

# Recurso Natural

class RecursoNaturalDetail(DetailView):
    model = RecursoNatural
    
    def get_success_url(self):
        return reverse_lazy('recursonatural-list',
                            kwargs={'pk':self.object.recursonatural.id})

class RecursoNaturalCreate(CreateView):
    model = RecursoNatural
    form_class = RecursoNaturalForm
    
    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(
                self.get_context_data(form = form))
    
    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form):
        return self.render_to_response(
                self.get_context_data(form = form))

class RecursoNaturalList(ListView):
    model = RecursoNatural
    
    def get_context_data(self, **kwargs):
        context = super(RecursoNaturalList, self).get_context_data(**kwargs)
        context['recursonatural'] = RecursoNatural.objects.all()
        return context
    
    def get_queryset(self):
        return ListView.get_queryset(self)

class RecursoNaturalUpdate(UpdateView):
    model = RecursoNatural
    form_class = RecursoNaturalForm
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(
                self.get_context_data(object=self.object,
                                      form=form))
        
    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form):
        return self.render_to_response(
                self.get_context_data(form = form)) 

#Recurso Cultural
class RecursoCulturalDetail(DetailView):
    model = RecursoCultural
    
    def get_success_url(self):
        return reverse_lazy('recursocultural-list',
                            kwargs={'pk':self.object.recursocultural.id})

class RecursoCulturalCreate(CreateView):
    model = RecursoCultural
    form_class = RecursoCulturalForm
    
    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(
                self.get_context_data(form = form))
    
    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if (form.is_valid()):
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form):
        return self.render_to_response(
                self.get_context_data(form = form))
        
class RecursoCulturalList(ListView):
    model = RecursoCultural
    
    def get_context_data(self, **kwargs):
        context = super(RecursoCulturalList, self).get_context_data(**kwargs)
        context['recursocultural'] = RecursoCultural.objects.all()
        return context
    
    def get_queryset(self):
        return ListView.get_queryset(self)
    
class RecursoCulturalUpdate(UpdateView):
    model = RecursoCultural
    form_class = RecursoCulturalForm
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(
                self.get_context_data(object=self.object,
                                      form=form))
        
    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form):
        return self.render_to_response(
                self.get_context_data(form = form)) 

