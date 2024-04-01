from django.contrib import admin
from django.urls import path, include
from .admin import admin_site
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('faculties', views.FacultyViewSet, basename='faculties')
router.register('majors', views.MajorViewSet, basename='majors')
router.register('information', views.InformationViewSet, basename='information')
router.register('informationsection', views.InformationSecViewSet, basename='informationsection')
router.register('comments', views.CommentsViewSet, basename='comments')
router.register('questions', views.QuestionsViewSet, basename='questions')
router.register('marks', views.MarkViewSet, basename='marks')
router.register('users', views.UserViewSet, basename='users')
router.register('banners', views.BannerViewSet, basename='banners')
router.register('university', views.UniversityViewSet, basename='university')
router.register('livestream', views.LivestreamViewSet, basename='livestream')

urlpatterns = [
    #path('', admin.site.urls),
    path('admin/', admin_site.urls),
    path('', include(router.urls)),
]
