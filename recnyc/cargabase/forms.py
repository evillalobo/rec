from django import forms
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Reset, Layout, Field, ButtonHolder

from .models import Departamento, Categoria, RecursoNatural
from cargabase.models import RecursoCultural

class DepartamentoForm (forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DepartamentoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('nombre', placeholder='Nombre'),
            Field('descripcion', placeholder='Descripcion'),
            Field('imagen', placeholder='Imagen'),
            Field('circuitos', placeholder='Circutos'),
            ButtonHolder(Submit('depto_submit', _('Guardar')),
                         Reset('depto_cancel', _('Cancelar'), onclick='history.go(-1);'),
            ))
    class Meta:
        model = Departamento
        fields = ['nombre',
                  'descripcion',
                  'imagen',
                  'circuitos']

class CategoriaForm (forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoriaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('categoria', placeholder='Categoria'),
            Field('descripcion', placeholder='Descripcion'),
            Field('departamento', placeholder='Departamento al que pertenece'),
            ButtonHolder(Submit('depto_submit', _('Guardar')),
                         Reset('depto_cancel', _('Cancelar'), onclick='history.go(-1);'),
            ))
    class Meta:
        model = Categoria
        fields = ['categoria',
                  'descripcion',
                  'departamento',
                  ]

class RecursoNaturalForm (forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecursoNaturalForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('nombre', placeholder='Nombre del Recurso Natural'),
            Field('descripcion', placeholder='Descripcion'),
            Field('imagen', placeholder='Imagen'),
            Field('departamento', placeholder='Departamento al que pertenece'),
            Field('categoria', placeholder='Categoria del Recurso Natural'),
            ButtonHolder(Submit('depto_submit', _('Guardar')),
                         Reset('depto_cancel', _('Cancelar'), onclick='history.go(-1);'),
            ))
    class Meta:
        model = RecursoNatural
        fields = ['nombre',
                  'descripcion',
                  'imagen',
                  'departamento',
                  'categoria',
                  ]
        
class RecursoCulturalForm (forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecursoCulturalForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Field('nombre', placeholder='Nombre del Recurso Natural'),
            Field('historia', placeholder='Historia'),
            Field('direccion', placeholder='Dirección'),
            Field('punto', placeholder='Lugar>'),
            Field('departamento', placeholder='Departamento'),
            Field('categoria', placeholder='Categoría'),
            ButtonHolder(Submit('depto_submit', _('Guardar')),
                         Reset('depto_cancel', _('Cancelar'), onclick='history.go(-1);'),
            ))
    class Meta:
        model = RecursoCultural
        fields = ['nombre',
                  'historia',
                  'direccion',
                  'departamento',
                  'punto',
                  'categoria'
                  ]