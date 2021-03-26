from django.urls import include, path
from rest_framework import routers, urlpatterns
from rest_framework.routers import DefaultRouter
from questions.api import views as qv

router = DefaultRouter()
router.register(r"questions", qv.QuestionViewSet)


urlpatterns = [
    path("", include(router.urls)),

    path("questions/<slug:slug>/answer/",
         qv.AnswerCreateAPIView.as_view(),
         name="answer-create"),
    path("questions/userquestions/",
         qv.UserQuestionsListAPIView.as_view(),
         name="user-questions"),

    path("answers/<int:pk>/",
         qv.AnswerRUDAPIView.as_view(),
         name="answer-detail"),

    path("questions/<slug:slug>/answers/",
         qv.AnswerListAPIView.as_view(),
         name="answer-list"),

    path("answers/<int:pk>/like/",
         qv.AnswerLikeAPIView.as_view(),
         name="answer-like"),

    path("users/<int:pk>/questions/",
         qv.UserQuestionsListAPIView.as_view(),
         name="user-questions"),

    path("users/<int:pk>/answers/",
         qv.UserAnswersListAPIView.as_view(),
         name="user-answers"),

    path("category/",
         qv.CategoryListAPIView.as_view(),
         name="categories"),

    path("category/<int:pk>/questions/",
         qv.CategoryQuestionsListAPIView.as_view(),
         name="category-questions"),




]
