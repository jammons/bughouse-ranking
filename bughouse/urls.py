from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from . import views


urlpatterns = patterns(
    '',
    url(r'^api/', include('bughouse.api.urls')),
    url(r'^$', views.ReportGameView.as_view(), name='report-game'),
    url(r'^player-roster/$', views.PlayerRosterView.as_view(), name='player-roster'),
    url(r'^team-leaderboard/$', views.TeamLeaderboard.as_view(), name='team-leaderboard'),
    url(
        r'^individual-leaderboard/$', views.IndividualLeaderboard.as_view(),
        name='individual-leaderboard',
    ),
    url(
        r'^player-rating-visualizations/$', views.PlayerRatingsVisualization.as_view(),
        name='player-rating-visualizations',
    ),
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
