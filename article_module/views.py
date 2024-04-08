from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from article_module.models import Article,ArticleVisit,ArticleCategory
from site_module.models import SiteBanner
from utlis.http_service import get_client_ip
from django.core.paginator import Paginator


class ArticleListView(ListView):
    template_name = 'article_module/article_list.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = SiteBanner.objects.filter(is_active=True,position=SiteBanner.SiteBannerPositions.article_list)
        return context

    def get_queryset(self):
        query = super(ArticleListView,self).get_queryset()
        category_name = self.kwargs.get('cat')
        if category_name is not None :
            query = query.filter(category__url_title__iexact=category_name)
        return query



class ArticleDetailView(DetailView):
    template_name = 'article_module/article_detail.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_article = self.object
        request = self.request

        user_ip = get_client_ip(self.request)
        user_id = None
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
        #'میگه قبلش برو چک کن ببین بازدید داشته این کاربر یا نه '
        has_been_visited = ArticleVisit.objects.filter(ip__iexact=user_ip,article_id=loaded_article.id).exists()
        if not has_been_visited:
            new_visit = ArticleVisit(ip=user_ip,user_id=user_id,article_id=loaded_article.id)
            new_visit.save()

        return context



def article_categories_component(request:HttpRequest):
    article_categories = ArticleCategory.objects.all()
    context = {
        'categories' : article_categories
    }
    return render(request,'article_module/components/article_components_categories.html',context)



def search(request):
    if request.method == 'GET':
        s = request.GET.get('search')

    # article_search = Article.objects.filter(title_in_english__icontains=s)
    article_search = Article.objects.filter((Q(title_in_persian__icontains=s) | Q(title_in_english__icontains=s) | Q(abstract__icontains=s)))[:12]

    context = {
            'article_search': article_search,

        }

    return render(request,'article_module/search_page.html',context)

    # if request.method == 'GET':
    #     q = request.GET.get('search')
    #
    # # article_search = Article.objects.filter(Q(title_in_english__iexact=q))
    # # context = {'article_search':article_search}





