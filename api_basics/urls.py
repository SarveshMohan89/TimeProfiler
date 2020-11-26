from django.urls import path, include
from .views import  article_list, article_detail, ArticleAPIView, ArticleDetails,ArticleView,GenericAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('article', ArticleView, basename='article')


urlpatterns = [
    #path('article/', article_list),
    #path('detail/<int:pk>/', article_detail),
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetails.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),


]