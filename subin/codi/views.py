from django.views.generic import *
from codi.models import Codi, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import CodiInlineFormSet
from mysite.views import OwnerOnlyMixin

class CategoryLV(ListView):
    model=Category
    
class CategoryDV(DetailView):
    model = Category
    
class CodiDV(DetailView):
    model = Codi
    
class CategoryCV(LoginRequiredMixin, CreateView):
    model=Category
    fields = ('name', 'description')
    success_url = reverse_lazy('codi:index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = CodiInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = CodiInlineFormSet()
        return context
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['formset']
        for codiform in formset:
            codiform.instance.owner = self.request.user
        if formset.is_valid() :
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))
        
class CategoryChangeLV(LoginRequiredMixin, ListView):
    template_name='codi/category_change_list.html'
    
    def get_queryset(self) :
        return Category.objects.filter(owner=self.request.user)
    
class CategoryUV(OwnerOnlyMixin, UpdateView):
    model = Category
    fields = ('name', 'description')
    success_url = reverse_lazy('codi:index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = CodiInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else :
            context['formset'] = CodiInlineFormSet(instance=self.object)
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else :
            return self.render_to_response(self.get_context_data(form=form))
        
class CategoryDelV(OwnerOnlyMixin, DeleteView):
    model=Category
    success_url=reverse_lazy('codi:index')
    
class CodiCV(LoginRequiredMixin, CreateView):
    model=Codi
    fields=('category', 'title', 'image', 'description', 'url')
    success_url=reverse_lazy('codi:index')
    
    def form_valid(self, form):
        form.instance.owner=self.request.user
        return super().form_valid(form)
    
class CodiChangeLV(LoginRequiredMixin, ListView):
    template_name='codi/codi_change_list.html'
    
    def get_queryset(self):
        return Codi.objects.filter(owner=self.request.user)
    
class CodiUV(OwnerOnlyMixin, UpdateView):
    model=Codi
    fields=('category', 'title', 'image', 'description', 'url')
    success_url=reverse_lazy('codi:index')
    
class CodiDelV(OwnerOnlyMixin, DeleteView):
    model=Codi
    success_url=reverse_lazy('codi:index')