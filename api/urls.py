from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet


router_v1 = DefaultRouter()

router_v1.register('api/v1/posts', PostViewSet, basename='PostView')
router_v1.register('api/v1/group', GroupViewSet, basename='GroupView')
router_v1.register('api/v1/follow', FollowViewSet, basename='FollowView')
router_v1.register(
    r'api/v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='CommentView')

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('', include(router_v1.urls)),
]
