from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from .models import *
from .forms import *
from django.urls import reverse, reverse_lazy
from xhtml2pdf import pisa
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from weasyprint import HTML, CSS
import os
from django.conf import settings


class RenderPdf(View):
    
     def get(self, request, *args, **kwargs):
        total_eqps = Par2000T.objects.count() + Consoles.objects.count() + Radios.objects.count() + CentralAudio.objects.count() + Diversos.objects.count() + Ems.objects.count() + Telefonia.objects.count()
        context = {
            'objectPar2000T': Par2000T.objects.order_by('pk').all(),
            'objectConsoles': Consoles.objects.order_by('pk').all(),
            'objectRadios': Radios.objects.order_by('pk').all(),
            'objectCentralAudio': CentralAudio.objects.order_by('pk').all(),
            'objectDiversos': Diversos.objects.order_by('pk').all(),
            'objectEms': Ems.objects.order_by('pk').all(),
            'objectTelefonia': Telefonia.objects.order_by('pk').all(),
            'total_eqps': total_eqps
        }
        
        template  = get_template('view_pdf.html')

        html = template.render(context)
        css_url = os.path.join(settings.BASE_DIR, 'staticfiles\\bootstrap-5.0.0-beta3-dist\\css\\bootstrap.min.css')
        pdf = HTML(string=html).write_pdf(stylesheets=[CSS(css_url)])

        return HttpResponse(pdf, content_type='application/pdf')
  
  
# Create your views 
class IndexListView(ListView):

    template_name = 'disponibilidade.html'
    context_object_name = 'objectPar2000T'

    def get_queryset(self):
        return Par2000T.objects.order_by('pk').all()

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        context['objectConsoles'] = Consoles.objects.order_by('pk').all()
        context['objectRadios'] = Radios.objects.order_by('pk').all()
        context['objectCentralAudio'] = CentralAudio.objects.order_by('pk').all()
        context['objectDiversos'] = Diversos.objects.order_by('pk').all()
        context['objectEms'] = Ems.objects.order_by('pk').all()
        context['objectTelefonia'] = Telefonia.objects.order_by('pk').all()
        return context

class Par2000TUpdate(UpdateView):
    model = Par2000T
    template_name = 'editar.html'
    form_class = Par2000TForm
    context_object_name = 'object' 
    success_url = reverse_lazy('listar_disponibilidade')

    def get_context_data(self, **kwargs):
        context = super(Par2000TUpdate, self).get_context_data(**kwargs)
        context['url_cont'] = 'mudar_par2000t'
        return context



class ConsolesUpdate(UpdateView):
    model = Consoles
    template_name = 'editar.html'
    form_class = ConsolesForm
    context_object_name = 'object' 
    success_url = reverse_lazy('listar_disponibilidade')

    def get_context_data(self, **kwargs):
        context = super(ConsolesUpdate, self).get_context_data(**kwargs)
        context['url_cont'] = 'mudar_consoles'
        return context

class RadiosUpdate(UpdateView):
    model = Radios
    template_name = 'editar.html'
    form_class = RadiosForm
    context_object_name = 'object' 
    success_url = reverse_lazy('listar_disponibilidade')

    def get_context_data(self, **kwargs):
        context = super(RadiosUpdate, self).get_context_data(**kwargs)
        context['url_cont'] = 'mudar_radios'
        return context

class CentralAudioUpdate(UpdateView):
    model = CentralAudio
    template_name = 'editar.html'
    form_class = CentralAudioForm
    context_object_name = 'object' 
    success_url = reverse_lazy('listar_disponibilidade')

    def get_context_data(self, **kwargs):
        context = super(CentralAudioUpdate, self).get_context_data(**kwargs)
        context['url_cont'] = 'mudar_centralaudio'
        return context

class DiversosUpdate(UpdateView):
    model = Diversos
    template_name = 'editar.html'
    form_class = DiversosForm
    context_object_name = 'object' 
    success_url = reverse_lazy('listar_disponibilidade')

    def get_context_data(self, **kwargs):
        context = super(DiversosUpdate, self).get_context_data(**kwargs)
        context['url_cont'] = 'mudar_diversos'
        return context

class EmsUpdate(UpdateView):
    model = Ems
    template_name = 'editar.html'
    form_class = EmsForm
    context_object_name = 'object' 
    success_url = reverse_lazy('listar_disponibilidade')

    def get_context_data(self, **kwargs):
        context = super(EmsUpdate, self).get_context_data(**kwargs)
        context['url_cont'] = 'mudar_ems'
        return context

class TelefoniaUpdate(UpdateView):
    model = Telefonia
    template_name = 'editar.html'
    form_class = TelefoniaForm
    context_object_name = 'object' 
    success_url = reverse_lazy('listar_disponibilidade')

    def get_context_data(self, **kwargs):
        context = super(TelefoniaUpdate, self).get_context_data(**kwargs)
        context['url_cont'] = 'mudar_telefonia'
        return context

