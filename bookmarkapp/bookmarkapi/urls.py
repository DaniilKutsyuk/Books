from bookmarkapi.views import BookmarkViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', BookmarkViewSet, basename='bookmarks')
urlpatterns = router.urls
