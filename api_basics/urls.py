from django.urls import path
from . import views


urlpatterns = [
    # path('article/',views.article_list),
    path('article/',views.ArticleAPIView.as_view()),
    # path('detail/<int:pk>/',views.article_detail)
    path('detail/<int:id>/',views.Articledetail.as_view())
]
