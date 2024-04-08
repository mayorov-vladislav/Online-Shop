"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from app import settings
from rest_framework import routers
from carts.views import *
from goods.views import *
from main import views
from orders.views import *
from users.views import *



# --------------- ROUTER API SETTINGS ---------------
router = routers.DefaultRouter()
# --------------- CARTS ---------------
router.register(r'api/v1/cart', CartApi),
# --------------- GOODS ---------------
router.register(r'api/v1/categories', CategoryApi),
router.register(r'api/v1/products', ProductApi),
# --------------- ORDERS ---------------
router.register(r'api/v1/orders', OrderApi),
router.register(r'api/v1/order-items', OrderItemApi),
# --------------- USERS ---------------
router.register(r'api/v1/users', UserApi),
# --------------- ROUTER API SETTINGS ---------------

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('catalog/', include('goods.urls', namespace='catalog')),
    path('user/', include('users.urls', namespace='user')),
    path('cart/', include('carts.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('', include(router.urls))
]


if settings.DEBUG: 
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
        ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    