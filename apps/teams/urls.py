from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.teams.views import StaffRoleView, StaffMemberView, TeamView, StatsView


router = DefaultRouter()
router.register("staff-role", StaffRoleView)
router.register("staff-member", StaffMemberView)
router.register("team", TeamView)


urlpatterns = [
    path("", include(router.urls)),
    path("stats/", StatsView.as_view()),
]
