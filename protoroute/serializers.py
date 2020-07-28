from rest_framework import serializers

from .models import *

# general debugging note: if you define a serializer such that the cardinality
# of any of its fields does not match that defined in the `models.py` file
# a host of strange and misreported errors can result. if you find you make a migration
# or redefine a serialisation class and then find a host of inexplicable problems,
# this is the first thing to check

# note also that, if `fields` is set to "__all__", then fields without explicitly-defined serialisers
# will receive a default serialisation (IIRC HyperlinkedModelSerializer for complex objects)
# Very often this will not be what you want

# the 'AsLink' infix indicates serialisers that output as links within
# the API rather than inflated objects
class RouteGuideAsLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RouteGuide
        fields = ("__all__")

class RouteGuideSegmentAsLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RouteGuideSegment
        fields = ("__all__")

class RoutePointAsLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoutePoint
        fields = ("__all__")

class ProvenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provenance
        fields = ("__all__")

class PersonAndOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonAndOrganization
        fields = ("__all__")

class TransportNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportNote
        fields = ("__all__")

class MapReferenceSerializer(serializers.ModelSerializer):
    map_series = serializers.CharField(max_length=10)
    map_number = serializers.CharField(max_length=10)
    grid_reference = serializers.CharField(max_length=10, required=False)
    publisher = PersonAndOrganizationSerializer(many=False, required=False)
    routepoint = RoutePointAsLinkSerializer(many=True)

    class Meta:
        model = MapReference
        fields = ("__all__")

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("__all__")

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("__all__")

class GeoPathSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoPath
        fields = ("__all__")

class GeoCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoCoordinates
        fields = ("__all__")

class RouteGradientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteGradient
        fields = ("__all__")

class MapImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapImage
        fields = ("__all__")

class VerificationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationRecord
        fields = ("__all__")

class DistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distance
        fields = ("__all__")

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ("__all__")

class IndicativeDurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndicativeDuration
        fields = ("__all__")

class AmenityFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmenityFeature
        fields = ("__all__")

class RouteDifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteDifficulty
        fields = ("__all__")

class GeoCoordinates(serializers.ModelSerializer):
    class Meta:
        model = GeoCoordinates
        fields = ("__all__")

class RouteLegalAdvisorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteLegalAdvisory
        fields = ("__all__")

class RouteDesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteDesignation
        fields = ("__all__")

class UserGeneratedContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGeneratedContent
        fields = ("__all__")

class KnownRiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnownRisk
        fields = ("__all__")

class RiskModifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskModifier
        fields = ("__all__")

class RouteAccessRestrictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteAccessRestriction
        fields = ("__all__")

class RouteAccessRestrictionTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteAccessRestrictionTerm
        fields = ("__all__")

class RiskMitigatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskMitigator
        fields = ("__all__")

class RouteRiskAdvisorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteRiskAdvisory
        fields = ("__all__")

class RouteSegmentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteSegmentGroup
        fields = ("__all__")

class AccessibilityDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessibilityDescription
        fields = ("__all__")

class RoutePointSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    is_access_point = serializers.BooleanField(default=True)
    is_preferred_access_point = serializers.BooleanField(default=False)
    description = serializers.CharField(required=False)
    headline = serializers.CharField(max_length=200, required=False)
    same_as = serializers.URLField(required=False)
    rp_mapref = MapReferenceSerializer(many=True, required=False)
    rp_geo = GeoCoordinatesSerializer(many=True, required=False)
    rp_transport_note = TransportNoteSerializer(many=True, required=False)

    class Meta:
        model = RoutePoint
        exclude = ("id",)

class RouteGuideSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, required=False)
    url = serializers.URLField(required=False)
    date_published = serializers.DateField(required=False)
    date_modified = serializers.DateField(required=False)
    description = serializers.CharField(required=False)
    headline = serializers.CharField(max_length=200, required=False)
    is_loop = serializers.BooleanField(required=False)
    id_as_url = serializers.URLField(required=False)
    author = PersonAndOrganizationSerializer(many=True, required=False)
    rg_provenance = ProvenanceSerializer(many=True, required=False)
    rg_verification_record = VerificationRecordSerializer(many=True, required=False)
    start_point = RoutePointSerializer(many=False, required=False)
    end_point = RoutePointSerializer(many=False, required=False)
    point_of_interest = RoutePointSerializer(many=True, required=False)
    start_point = RoutePointSerializer(many=True, required=False)
    end_point = RoutePointSerializer(many=True, required=False)
    activity = ActivitySerializer(many=True, required=False)
    rg_geopath = GeoPathSerializer(many=True, required=False)
    rg_mapimage = MapImageSerializer(many=True, required=False)
    rg_distance = DistanceSerializer(many=True, required=False)
    rg_access_description = AccessibilityDescriptionSerializer(many=True, required=False)
    rg_gradient = RouteGradientSerializer(many=True, required=False)
    rg_difficulty = RouteDifficultySerializer(many=True, required=False)
    rg_risk_advisory = RouteRiskAdvisorySerializer(many=True, required=False)
    rg_legal_advisory = RouteLegalAdvisorySerializer(many=True, required=False)
    rg_route_designation = RouteDesignationSerializer(many=True, required=False)
    rg_access_restriction = RouteAccessRestrictionSerializer(many=True, required=False)
    rg_duration = IndicativeDurationSerializer(many=True, required=False)
    seg_route_guide = RouteGuideSegmentAsLinkSerializer(many=True, required=False)

    class Meta:
        model = RouteGuide
        exclude = ("id",)
        #fields = ("__all__")

class RouteGuideSegmentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, required=False)
    url = serializers.URLField(required=False)
    date_published = serializers.DateField(required=False)
    date_modified = serializers.DateField(required=False)
    description = serializers.CharField(required=False)
    headline = serializers.CharField(max_length=200, required=False)
    is_loop = serializers.BooleanField(required=False)
    id_as_url = serializers.URLField(required=False)
    author = PersonAndOrganizationSerializer(many=True, required=False)
    seg_provenance = ProvenanceSerializer(many=False, required=False)
    seg_verification_record = VerificationRecordSerializer(many=True, required=False)
    point_of_interest = RoutePointSerializer(many=True, required=False)
    start_point = RoutePointSerializer(many=True, required=False)
    end_point = RoutePointSerializer(many=True, required=False)
    activity = ActivitySerializer(many=True, required=False)
    seg_geopath = GeoPathSerializer(many=True, required=False)
    seg_mapimage = MapImageSerializer(many=True, required=False)
    seg_distance = DistanceSerializer(many=True, required=False)
    seg_access_description = AccessibilityDescriptionSerializer(many=True, required=False)
    seg_gradient = RouteGradientSerializer(many=True, required=False)
    seg_difficulty = RouteDifficultySerializer(many=True, required=False)
    seg_duration = IndicativeDurationSerializer(many=True, required=False)
    seg_risk_advisory = RouteRiskAdvisorySerializer(many=True, required=False)
    seg_legal_advisory = RouteLegalAdvisorySerializer(many=True, required=False)
    seg_route_designation = RouteDesignationSerializer(many=True, required=False)
    seg_access_restriction = RouteAccessRestrictionSerializer(many=True, required=False)
    sequence = serializers.CharField(required=False)
    additional_info = ArticleSerializer(many=True, required=False)
    route_guide = RouteGuideAsLinkSerializer(many=True, required=False)

    class Meta:
        model = RouteGuideSegment
        fields = ("__all__")
