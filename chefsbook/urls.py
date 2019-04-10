from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from chefsbook.chefsbookApi import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'table', views.TableViewSet)
router.register(r'position', views.OrderPositionViewSet)
router.register(r'order', views.OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
