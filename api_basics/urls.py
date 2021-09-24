from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article',views.ArticleViewSet,basename='article')


urlpatterns = [
    path('viewset/',include(router.urls)),
    # path('article/',views.article_list),
    path('article/<int:id>',views.GenericAPIViews.as_view()),
    # path('detail/<int:pk>/',views.article_detail)
    path('detail/<int:id>/',views.Articledetail.as_view())
]
