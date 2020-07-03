from rest_framework import serializers

from .models import *

class RouteGuideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RouteGuide
        fields = ("__all__")

class RouteGuideSegmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RouteGuideSegment
        fields = ("__all__")

class ProvenanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provenance
        fields = ("__all__")

class PersonAndOrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonAndOrganization
        fields = ("__all__")

class TransportNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TransportNote
        fields = ("__all__")

class MapReferenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapReference
        fields = ("__all__")

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ("__all__")

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ("__all__")

class GeoPathSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeoPath
        fields = ("__all__")

class GeoCoordinatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeoCoordinates
        fields = ("__all__")

class RouteGradientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RouteGradient
        fields = ("__all__")

class MapImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MapImage
        fields = ("__all__")

class VerificationRecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VerificationRecord
        fields = ("__all__")

class DistanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Distance
        fields = ("__all__")

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ("__all__")

class IndicativeDurationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IndicativeDuration
        fields = ("__all__")

class AmenityFeatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AmenityFeature
        fields = ("__all__")

class RouteDifficultySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RouteDifficulty
        fields = ("__all__")

class GeoCoordinates(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GeoCoordinates
        fields = ("__all__")

class RouteLegalAdvisorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RouteLegalAdvisory
        fields = ("__all__")

class RouteDesignationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RouteDesignation
        fields = ("__all__")

class UserGeneratedContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserGeneratedContent
        fields = ("__all__")

class KnownRiskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KnownRisk
        fields = ("__all__")

class RiskModifierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RiskModifier
        fields = ("__all__")

class RouteAccessRestrictionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RouteAccessRestriction
        fields = ("__all__")

class RouteAccessRestrictionTermSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RouteAccessRestrictionTerm
        fields = ("__all__")

class RiskMitigatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RiskMitigator
        fields = ("__all__")

class RouteRiskAdvisorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RouteRiskAdvisory
        fields = ("__all__")

class RouteSegmentGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RouteSegmentGroup
        fields = ("__all__")

class AccessibilityDescriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccessibilityDescription
        fields = ("__all__")

class RoutePointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoutePoint
        fields = ("__all__")
