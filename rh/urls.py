# blog/urls.py
from rest_framework.routers import DefaultRouter
from .views import PessoaViewSet

router = DefaultRouter()
router.register(r'pessoas', PessoaViewSet)

urlpatterns = router.urls
