from django.urls import path
from Article_Module.views import ArticlesListView, ArticleDetailView, AddArticleComment

urlpatterns = [
    path('', ArticlesListView.as_view(), name='Articles_Url'),
    path('cat/<str:category>', ArticlesListView.as_view(), name='articles_by_category_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='ArticlesDetail_Url'),
    path('add_article_comment', AddArticleComment, name='add-Article_comment_url')
]
