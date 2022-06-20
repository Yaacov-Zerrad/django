from django.shortcuts import get_object_or_404, render
from .models import Articles
from.form import modelForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



class ArticlesCreateView(CreateView):
    form_class = modelForm
    model = Articles
    # success_url = '/blog'
    def form_valid(self, form):
        """for vlidat if condition"""
        return super().form_valid(form)
    
    
    
    
class ArticlesUpdateView(UpdateView):
    form_class = modelForm
    model = Articles
    # template_name = ".html"
    success_url = '/blog'
    
    def form_valid(self, form):
        """for validat if condition"""
        return super().form_valid(form)
    
    
    
class ArticlesDeleteView(DeleteView):
    model = Articles
    success_url = '/blog'
    
    # def get_success_url(self) -> str:
    #     return super().get_success_url()








class ArticlesListView(ListView):
    queryset = Articles.objects.all()
    
    
    
    
class ArticlesDetailView(DetailView):
    model = Articles
    template_name = "blog/article_detail.html"
    
    def get_object(self):
        id_ = self.kwargs.get('pk')    
        return get_object_or_404(Articles, id=id_)
    
    


