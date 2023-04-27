from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import DetailView
from django.views.generic.list import ListView
from jalali_date import datetime2jalali, date2jalali
from Article_Module.models import Article, ArticleCategory, ArticelComment


# class ArticlesView(View):
#     def get(self, request):
#         articles = Article.objects.filter(is_active=True)
#         context = {
#             'articles': articles
#         }
#         return render(request, 'article_module/articles_page.html', context)


class ArticlesListView(ListView):
    model = Article
    paginate_by = 2
    template_name = 'Article_module/Article_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticlesListView, self).get_context_data(*args, **kwargs)

        return context

    def get_queryset(self):
        query = super(ArticlesListView, self).get_queryset()
        category_name = self.kwargs.get('category')
        query = query.filter(is_active=True)


        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact=category_name)

        return query


def Article_Category_Component(request: HttpRequest):
    MainArticleCategorys :ArticleCategory = ArticleCategory.objects.prefetch_related('articlecategory_set').filter(is_active=True, parent_id=None)


    context = {
        'main_categorys': MainArticleCategorys
    }
    return render(request, 'Article_module/components/Article_Category_Components.html', context)



class ArticleDetailView(DetailView):
    model = Article
    template_name = 'Article_module/ArticleDetail_Page.html'
    def get_queryset(self):
        query = super(ArticleDetailView, self).get_queryset()

        query = query.filter(is_active=True)
        return query
    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        article: Article = kwargs.get('object')
        context['Comments'] = ArticelComment.objects.filter(article_id= article.id, parent_id=None).order_by('-create_date').prefetch_related('articelcomment_set')
        context['Comments_Count'] = ArticelComment.objects.filter(article_id= article.id).count()

        return context


####Ajax Jquery

def AddArticleComment(request: HttpRequest):
    print(request.GET)

    if request.user.is_authenticated:
        article_id = request.GET.get('article_id')
        article_comment = request.GET.get('article_comment')
        parent_id = request.GET.get('parent_id')
        # print(article_id,article_comment,parent_id)
        New_Comment = ArticelComment(article_id=article_id, text=article_comment, user_id=request.user.id,parent_id=parent_id)
        New_Comment.save()
        context = {
          "Comments": ArticelComment.objects.filter(article_id=article_id, parent_id=None).order_by('-create_date').prefetch_related('articelcomment_set'),
            "Comments_Count": ArticelComment.objects.filter(article_id=article_id).count()
        }
        print(article_comment)

        # return render(request, 'Article_module/Includes/Articla_comment_Parial.html', context)
        return render(request, 'Article_Module/Includes/Articla_comment_Parial.html', context)


    return HttpResponse('hello')
