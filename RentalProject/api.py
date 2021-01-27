from rest_framework import routers
from rental import api_views as rental_views

router = routers.DefaultRouter()
router.register('friends', rental_views.FriendViewSet)
router.register('belongings', rental_views.BelongingViewset)
router.register('borrowings', rental_views.BorrowedViewset)
