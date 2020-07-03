from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import *
from .models import *

def index(request):
    return HttpResponse("Hello, world. You're at the ProtoRoute index.")

class RouteGuideViewSet(viewsets.ModelViewSet):
    queryset = RouteGuide.objects.all().order_by('name')
    serializer_class = RouteGuideSerializer

class ProvenanceViewSet(viewsets.ModelViewSet):
    queryset = Provenance.objects.all().order_by('description')
    serializer_class = ProvenanceSerializer

class RouteSegmentGuideViewSet(viewsets.ModelViewSet):
    queryset = RouteGuideSegment.objects.all().order_by('name')
    serializer_class = RouteGuideSegmentSerializer

class RoutePointViewSet(viewsets.ModelViewSet):
    queryset = RoutePoint.objects.all().order_by('name')
    serializer_class = RoutePointSerializer

class PersonAndOrganizationViewSet(viewsets.ModelViewSet):
    queryset = PersonAndOrganization.objects.all().order_by('name')
    serializer_class = PersonAndOrganizationSerializer

class TransportNoteViewSet(viewsets.ModelViewSet):
    queryset = TransportNote.objects.all().order_by('transport_mode')
    serializer_class = TransportNoteSerializer

class MapReferenceViewSet(viewsets.ModelViewSet):
    queryset = MapReference.objects.all().order_by('id')
    serializer_class = MapReferenceSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('content')
    serializer_class = CategorySerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('headline')
    serializer_class = ArticleSerializer

class GeoPathViewSet(viewsets.ModelViewSet):
    queryset = GeoPath.objects.all().order_by('id')
    serializer_class = GeoPathSerializer

class MapImageViewSet(viewsets.ModelViewSet):
    queryset = MapImage.objects.all().order_by('id')
    serializer_class = MapImageSerializer

class VerificationRecordViewSet(viewsets.ModelViewSet):
    queryset = VerificationRecord.objects.all().order_by('date_verified')
    serializer_class = VerificationRecordSerializer

class DistanceViewSet(viewsets.ModelViewSet):
    queryset = Distance.objects.all().order_by('id')
    serializer_class = DistanceSerializer

class ProvenanceViewSet(viewsets.ModelViewSet):
    queryset = Provenance.objects.all().order_by('id')
    serializer_class = ProvenanceSerializer

class AccessibilityDescriptionViewSet(viewsets.ModelViewSet):
    queryset = AccessibilityDescription.objects.all().order_by('id')
    serializer_class = AccessibilityDescriptionSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('prefLabel')
    serializer_class = ActivitySerializer

class IndicativeDurationViewSet(viewsets.ModelViewSet):
    queryset = IndicativeDuration.objects.all().order_by('id')
    serializer_class = IndicativeDurationSerializer

class AmenityFeatureViewSet(viewsets.ModelViewSet):
    queryset = AmenityFeature.objects.all().order_by('name')
    serializer_class = AmenityFeatureSerializer

class GeoCoordinatesViewSet(viewsets.ModelViewSet):
    queryset = GeoCoordinates.objects.all().order_by('id')
    serializer_class = GeoCoordinatesSerializer

class RoutePointViewSet(viewsets.ModelViewSet):
    queryset = RoutePoint.objects.all().order_by('name')
    serializer_class = RoutePointSerializer

class RouteGradientViewSet(viewsets.ModelViewSet):
    queryset = RouteGradient.objects.all().order_by('id')
    serializer_class = RouteGradientSerializer

class RouteDifficultyViewSet(viewsets.ModelViewSet):
    queryset = RouteDifficulty.objects.all().order_by('id')
    serializer_class = RouteDifficultySerializer

class RouteLegalAdvisoryViewSet(viewsets.ModelViewSet):
    queryset = RouteLegalAdvisory.objects.all().order_by('id')
    serializer_class = RouteLegalAdvisorySerializer

class RouteDesignationViewSet(viewsets.ModelViewSet):
    queryset = RouteDesignation.objects.all().order_by('id')
    serializer_class = RouteDesignationSerializer

class RouteSegmentGroupViewSet(viewsets.ModelViewSet):
    queryset = RouteSegmentGroup.objects.all().order_by('id')
    serializer_class = RouteSegmentGroupSerializer

class UserGeneratedContentGroupViewSet(viewsets.ModelViewSet):
    queryset = UserGeneratedContent.objects.all().order_by('id')
    serializer_class = UserGeneratedContentSerializer

class RouteRiskAdvisoryViewSet(viewsets.ModelViewSet):
    queryset = RouteRiskAdvisory.objects.all().order_by('id')
    serializer_class = RouteRiskAdvisorySerializer

class KnownRiskViewSet(viewsets.ModelViewSet):
    queryset = KnownRisk.objects.all().order_by('id')
    serializer_class = KnownRiskSerializer

class RiskModifierViewSet(viewsets.ModelViewSet):
    queryset = RiskModifier.objects.all().order_by('id')
    serializer_class = RiskModifierSerializer

class RouteAccessRestrictionViewSet(viewsets.ModelViewSet):
    queryset = RouteAccessRestriction.objects.all().order_by('id')
    serializer_class = RouteAccessRestrictionSerializer

class RouteAccessRestrictionTermViewSet(viewsets.ModelViewSet):
    queryset = RouteAccessRestrictionTerm.objects.all().order_by('id')
    serializer_class = RouteAccessRestrictionTermSerializer

class RiskMitigatorViewSet(viewsets.ModelViewSet):
    queryset = RiskMitigator.objects.all().order_by('id')
    serializer_class = RiskMitigatorSerializer

class UserGeneratedContentViewSet(viewsets.ModelViewSet):
    queryset = UserGeneratedContent.objects.all().order_by('id')
    serializer_class = UserGeneratedContentSerializer
