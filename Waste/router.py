from admins.views import Driver_register
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('drivers', Driver_register, basename='drivers')
