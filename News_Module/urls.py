from django.urls import path
from News_Module.views import NewsListView, NewsDetailView, AddNewsComment

urlpatterns = [
    path('', NewsListView.as_view(), name='News_Url'),
    path('cat/<str:category>', NewsListView.as_view(), name='news_by_category_list'),
    path('<int:pk>/', NewsDetailView.as_view(), name='newsDetail_Url'),
    path('add_news_comment', AddNewsComment, name='add-news_comment_url')
]
