from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

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
        exclude = ['id', 'route_guide', 'route_guide_segment']
        depth = 1

class PersonAndOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonAndOrganization
        exclude = ['id']

class TransportNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportNote
        exclude = ['id', 'routepoint']

class MapReferenceSerializer(WritableNestedModelSerializer):
    map_series = serializers.CharField(max_length=10)
    map_number = serializers.CharField(max_length=10)
    grid_reference = serializers.CharField(max_length=10, required=False)
    publisher = PersonAndOrganizationSerializer(many=False, required=False)

    class Meta:
        model = MapReference
        exclude = ['routepoint']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['id']

class SurfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surface
        exclude = ['id']

class SuggestedEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuggestedEquipment
        exclude = ['id']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ['id']
        depth = 1

class GeoPathSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoPath
        exclude = ['id', 'route_guide', 'route_guide_segment']

class GeoCoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoCoordinates
        exclude = ['id', 'routepoint']

class RouteGradientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteGradient
        exclude = ['id', 'route_guide', 'route_guide_segment']

class MapImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapImage
        exclude = ['id', 'route_guide', 'route_guide_segment']

class VerificationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationRecord
        exclude = ['id', 'route_guide', 'route_guide_segment']
        depth = 1

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        exclude = ['id']

class IndicativeDurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndicativeDuration
        exclude = ['id', 'route_guide', 'route_guide_segment']
        depth = 2

class AmenityFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmenityFeature
        exclude = ['id', 'routepoint']

class RouteDifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteDifficulty
        exclude = ['id', 'route_guide', 'route_guide_segment']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        exclude = ['id', 'route_guide']

class RouteLegalAdvisorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteLegalAdvisory
        exclude = ['id', 'route_guide', 'route_guide_segment']
        depth = 2

class RouteDesignationTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteDesignationTerm
        fields = ['term']

class RouteDesignationSerializer(serializers.ModelSerializer):
    term = RouteDesignationTermSerializer(many=True, required=False)
    class Meta:
        model = RouteDesignation
        fields = ['description', 'url', 'term']
        depth = 1

class UserGeneratedContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGeneratedContent
        exclude = ['id', 'route_guide']
        depth = 1

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
        exclude = ['id', 'route_guide', 'route_guide_segment']
        depth = 1

class RouteAccessRestrictionTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteAccessRestrictionTerm
        exclude = ['id']

class RiskMitigatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskMitigator
        fields = ("__all__")

class RouteRiskAdvisorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteRiskAdvisory
        exclude = ['id', 'route_guide', 'route_guide_segment']
        depth = 1

class RouteSegmentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteSegmentGroup
        fields = ("__all__")

class AccessibilityDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessibilityDescription
        exclude = ['id', 'route_guide', 'route_guide_segment']

class RoutePointSerializer(WritableNestedModelSerializer):
    name = serializers.CharField(required=True)
    is_access_point = serializers.BooleanField(default=True)
    is_preferred_access_point = serializers.BooleanField(default=False)
    description = serializers.CharField(required=False)
    headline = serializers.CharField(max_length=200, required=False)
    same_as = serializers.URLField(required=False)
    rp_mapref = MapReferenceSerializer(many=True, required=False)
    rp_geo = GeoCoordinatesSerializer(required=False)
    rp_transport_note = TransportNoteSerializer(many=True, required=False)
    rp_amenity = AmenityFeatureSerializer(many=True, required=False)

    class Meta:
        model = RoutePoint
        exclude = ("id",)

class RouteGuideSerializer(WritableNestedModelSerializer):
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
    route_point = RoutePointSerializer(many=True, required=False)
    activity = ActivitySerializer(many=True, required=False)
    rg_geopath = GeoPathSerializer(many=True, required=False)
    rg_mapimage = MapImageSerializer(many=True, required=False)
    rg_access_description = AccessibilityDescriptionSerializer(many=True, required=False)
    rg_gradient = RouteGradientSerializer(required=False)
    rg_difficulty = RouteDifficultySerializer(many=True, required=False)
    rg_risk_advisory = RouteRiskAdvisorySerializer(required=False)
    rg_legal_advisory = RouteLegalAdvisorySerializer(required=False)
    rg_route_designation = RouteDesignationSerializer(many=True, required=False)
    rg_access_restriction = RouteAccessRestrictionSerializer(many=True, required=False)
    rg_duration = IndicativeDurationSerializer(many=True, required=False)
    additional_info = ArticleSerializer(many=True, required=False)
    surfaces = SurfaceSerializer(many=True, required=False)
    image = ImageSerializer(many=True, required=False)
    suggested_equipment = SuggestedEquipmentSerializer(many=True, required=False)
    categories = CategorySerializer(many=True, required=False)
    user_generated_content = UserGeneratedContentSerializer(many=True, required=False)
    seg_route_guide = RouteGuideSegmentAsLinkSerializer(many=True, required=False)

    class Meta:
        model = RouteGuide
        fields = ("__all__")

class RouteGuideSegmentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200, required=False)
    url = serializers.URLField(required=False)
    date_published = serializers.DateField(required=False)
    date_modified = serializers.DateField(required=False)
    description = serializers.CharField(required=False)
    headline = serializers.CharField(max_length=200, required=False)
    distance = serializers.CharField(max_length=9, required=True)
    is_loop = serializers.BooleanField(required=False)
    id_as_url = serializers.URLField(required=False)
    author = PersonAndOrganizationSerializer(many=True, required=False)
    seg_provenance = ProvenanceSerializer(many=False, required=False)
    seg_verification_record = VerificationRecordSerializer(many=True, required=False)
    point_of_interest = RoutePointSerializer(many=True, required=False)
    activity = ActivitySerializer(many=True, required=False)
    seg_geopath = GeoPathSerializer(many=True, required=False)
    seg_mapimage = MapImageSerializer(many=True, required=False)
    seg_distance = serializers.CharField(max_length=9, required=True)
    seg_access_description = AccessibilityDescriptionSerializer(many=True, required=False)
    seg_gradient = RouteGradientSerializer(required=False)
    seg_difficulty = RouteDifficultySerializer(many=True, required=False)
    seg_duration = IndicativeDurationSerializer(many=True, required=False)
    seg_risk_advisory = RouteRiskAdvisorySerializer(required=False)
    seg_legal_advisory = RouteLegalAdvisorySerializer(required=False)
    seg_route_designation = RouteDesignationSerializer(many=True, required=False)
    seg_access_restriction = RouteAccessRestrictionSerializer(many=True, required=False)
    sequence = serializers.CharField(required=False)
    additional_info = ArticleSerializer(many=True, required=False)
    route_guide = RouteGuideAsLinkSerializer(many=True, required=False)

    class Meta:
        model = RouteGuideSegment
        fields = ("__all__")
