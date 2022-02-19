from re import template
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from .models import Articles, Category
from django.core.paginator import Paginator
from django.views.generic.list import ListView
from django.views.generic import DetailView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

#def # (request, page =1):
 #   articles_list = Articles.objects.published()
  #  paginator = Paginator(articles_list, 4) 
   # articles = paginator.get_page(page)
    #context = {"articles": articles }
    #return render(request, 'home.html', context)
class ArticleListView(ListView):
    queryset = Articles.objects.published()
    template_name = "home.html"
    paginate_by = 3 
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Articles.objects.published()
        else:
            return Articles.objects.filter(author=self.request.user)
class ArticleDetail(DetailView):
     template_name = 'articles_detail.html'
     def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Articles, slug=slug, status="p")
    

#def detail(request, slug):
 #   context = {"article": get_object_or_404(Articles, slug=slug, status="p")}
  #  return render(request, 'detail.html', context)

#def category(request, slug, page=1):
 #      category =  get_object_or_404(Category, slug=slug, status=True)
  #     articles_list = category.articles.published()
   #    paginator = Paginator(articles_list, 4) 
    #   articles = paginator.get_page(page)
     #  context = { "category": category,  "articles": articles}
      # return render(request, 'category.html', context)
      
class CategoryList(ListView):
    template_name = 'category.html'
    paginate_by = 3
    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.published()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category 
        return context
    
    
class AuthorList(ListView):
    template_name = 'author.html'
    paginate_by = 3
    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.articles.published()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author 
        return context
    

     
         