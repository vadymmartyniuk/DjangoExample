from rest_framework import routers

from lab6.api.views import Lab6ApiViewSet


app_name = 'api_lab6'

router = routers.DefaultRouter()
router.register(r'', Lab6ApiViewSet, basename='create')
urlpatterns = router.urls
