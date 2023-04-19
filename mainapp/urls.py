from rest_framework.routers import DefaultRouter
from .views import OrderView, TourView

router = DefaultRouter()

router.register('order', OrderView, basename='orders')
router.register('tour', TourView, basename='tours')


urlpatterns = router.urls