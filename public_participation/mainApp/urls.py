from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, DiscussionViewSet, UserViewViewSet, VoteViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'discussions', DiscussionViewSet)
router.register(r'userviews', UserViewViewSet)
router.register(r'votes', VoteViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
