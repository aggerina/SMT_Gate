from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import DetailView
from django.views.generic.list import ListView
from jalali_date import datetime2jalali, date2jalali
from News_Module.models import News, NewsCategory, NewsComment


# class ArticlesView(View):
#     def get(self, request):
#         articles = Article.objects.filter(is_active=True)
#         context = {
#             'articles': articles
#         }
#         return render(request, 'article_module/articles_page.html', context)


class NewsListView(ListView):
    model = News
    paginate_by = 2
    template_name = 'News_Module/News_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super(NewsListView, self).get_context_data(*args, **kwargs)

        return context

    def get_queryset(self):
        query = super(NewsListView, self).get_queryset()
        category_name = self.kwargs.get('category')
        query = query.filter(is_active=True)


        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact=category_name)

        return query


def News_Category_Component(request: HttpRequest):
    MainNewsCategorys :NewsCategory = NewsCategory.objects.prefetch_related('newscategory_set').filter(is_active=True, parent_id=None)


    context = {
        'main_categorys': MainNewsCategorys
    }
    return render(request, 'News_Module/components/News_Category_Components.html', context)



class NewsDetailView(DetailView):
    model = News
    template_name = 'News_Module/NewsDetail_Page.html'
    def get_queryset(self):
        query = super(NewsDetailView, self).get_queryset()

        query = query.filter(is_active=True)
        return query
    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        news: News = kwargs.get('object')
        context['Comments'] = NewsComment.objects.filter(News_id=news.id, parent_id=None).order_by('-create_date').prefetch_related('newscomment_set')
        context['Comments_Count'] = NewsComment.objects.filter(News_id= news.id).count()

        return context


####Ajax Jquery

def AddNewsComment(request: HttpRequest):
    print(request.GET)

    if request.user.is_authenticated:
        news_id = request.GET.get('news_id')
        news_comment = request.GET.get('news_comment')
        parent_id = request.GET.get('parent_id')
        # print(article_id,article_comment,parent_id)
        New_Comment = NewsComment(News_id=news_id, text=news_comment, user_id=request.user.id,parent_id=parent_id)
        New_Comment.save()
        context = {
          "Comments": NewsComment.objects.filter(News_id=news_id, parent_id=None).order_by('-create_date').prefetch_related('newscomment_set'),
            "Comments_Count": NewsComment.objects.filter(News_id=news_id).count()
        }
        print(news_comment)

        # return render(request, 'Article_module/Includes/Articla_comment_Parial.html', context)
        return render(request, 'News_Module/Includes/Articla_comment_Parial.html', context)


    return HttpResponse('hello')
