from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'route-guide', views.RouteGuideViewSet)
router.register(r'provenance', views.ProvenanceViewSet)
router.register(r'route-guide-segment', views.RouteSegmentGuideViewSet)
router.register(r'verification-record', views.VerificationRecordViewSet)
router.register(r'transport-note', views.TransportNoteViewSet)
router.register(r'person-and-organization', views.PersonAndOrganizationViewSet)
router.register(r'map-reference', views.MapReferenceViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'article', views.ArticleViewSet)
router.register(r'geopath', views.GeoPathViewSet)
router.register(r'map-image', views.MapImageViewSet)
router.register(r'distance', views.DistanceViewSet)
router.register(r'accessibility-description', views.AccessibilityDescriptionViewSet)
router.register(r'activity', views.ActivityViewSet)
router.register(r'indicative-duration', views.IndicativeDurationViewSet)
router.register(r'amenity-feature', views.AmenityFeatureViewSet)
router.register(r'geocoordinates', views.GeoCoordinatesViewSet)
router.register(r'route-point', views.RoutePointViewSet)
router.register(r'route-gradient', views.RouteGradientViewSet)
router.register(r'route-difficulty', views.RouteDifficultyViewSet)
router.register(r'route-legal-advisory', views.RouteLegalAdvisoryViewSet)
router.register(r'route-designation', views.RouteDesignationViewSet)
router.register(r'route-segment-group', views.RouteSegmentGroupViewSet)
router.register(r'user-generated-content', views.UserGeneratedContentViewSet)
router.register(r'route-risk-advisory', views.RouteRiskAdvisoryViewSet)
router.register(r'known-risk', views.KnownRiskViewSet)
router.register(r'route-access-restriction', views.RouteAccessRestrictionViewSet)
router.register(r'route-access-restriction-term', views.RouteAccessRestrictionTermViewSet)
router.register(r'risk-mitigator', views.RiskMitigatorViewSet)
router.register(r'risk-modifier', views.RiskModifierViewSet)

urlpatterns = [
    path('test', views.index, name='index'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
