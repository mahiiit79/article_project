from django.db.models import Count
from django.shortcuts import render
from django.views.generic.base import TemplateView

from article_module.models import Article
from utlis.convertors import group_list
from site_module.models import SiteSetting


class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_articles = Article.objects.all().order_by('id')[:12]
        context['latest_articles'] = group_list(latest_articles)
        article = Article.objects.all()[0]

        most_visit_articles = Article.objects.filter().annotate(visit_count=Count('articlevisit')).order_by('-visit_count')[:4]
        context['most_visit_articles'] = group_list(most_visit_articles)
        return context







def site_header_component(request):
    setting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_setting': setting
    }

    return render(request,'shared/site_header_component.html',context)


def site_footer_component(request):
     setting = SiteSetting.objects.filter(is_main_setting=True).first()
     context = {
         'site_setting': setting
     }

     return render(request,'shared/site_footer_component.html',context)