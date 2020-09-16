from django.db import models

    # TODO: remember that JSON output will inflate this data model
    # - adding @type (left implicit here)
    # - amenityFeature needs several more attributes autopopulated

    # note that a lot of fields listed as REQUIRED in the specification
    # are given as optional (blank=True) in the models. This is because
    # required fields mess with the flow of data submission and potentially
    # block it - the front end won't accept partially-defined objects,
    # all the classes are interdependent, and thus it becomes impossible
    # to actually submit anything

    # it would probably be possible to get around this with code in bespoke
    # serializer classes, but that's another can of worms.

    # note that the django ORM sometimes does not cope well with changes of
    # cardinality

class PersonAndOrganization(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    email = models.EmailField(verbose_name='Email', blank=True)
    website = models.URLField(verbose_name='Website', blank=True)

class TransportNote(models.Model):
    transport_mode = models.CharField(max_length=100, choices=[("Bus", "Bus"), ("Rail", "Rail"), ("Road", "Road"), ("Foot", "Foot"), ("Bicycle", "Bicycle")])
    description = models.CharField(max_length=500)
    routepoint = models.ForeignKey('RoutePoint', on_delete=models.CASCADE, blank=True, null=True, related_name='rp_transport_note')

class MapReference(models.Model):
    map_series = models.CharField(max_length=50)
    map_number = models.CharField(max_length=10)
    grid_reference = models.CharField(max_length=10)
    publisher = models.ForeignKey(PersonAndOrganization, on_delete=models.CASCADE, verbose_name='publisher', related_name='publisher', blank=True, null=True)
    routepoint = models.ManyToManyField('RoutePoint', related_name='rp_mapref')

class Provenance(models.Model):
    publisher = models.ForeignKey(PersonAndOrganization, on_delete=models.CASCADE, null=True, blank=True)
    provenance_url = models.URLField(verbose_name='Provenance')
    version = models.DateField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=250)
    route_guide = models.ForeignKey('RouteGuide', on_delete=models.CASCADE, null=True, blank=True, related_name='rg_provenance')
    route_guide_segment = models.ForeignKey('RouteGuideSegment', on_delete=models.CASCADE, null=True, blank=True, related_name='seg_provenance')

class Category(models.Model):
    content = models.CharField(max_length=30)

class Surface(models.Model):
    surface = models.CharField(max_length=30)

class SuggestedEquipment(models.Model):
    item = models.CharField(max_length=100)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    body = models.TextField()
    author = models.OneToOneField(PersonAndOrganization, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Author')
    image_url = models.URLField(blank=True, null=True, verbose_name='Image URL')

class GeoPath(models.Model):
    map_type = models.CharField(max_length=12, choices=[("RouteMap", "RouteMap"), ("ElevationMap", "ElevationMap"), ("CustomMap", "CustomMap")])
    url = models.URLField()
    encoding_format = models.CharField(max_length=40)
    # note that the only easy way to define a one-to-many relationship in django
    # is to treat the 'one' side of the equasion as a Foreign Key for the 'many' side.
    # in other words, a RouteGuide can have several GeoPaths, but a given GeoPath can
    # be associated with only one RouteGuide.
    route_guide = models.ForeignKey('RouteGuide', on_delete=models.CASCADE, null=True, blank=True, related_name='rg_geopath')
    route_guide_segment = models.ForeignKey('RouteGuideSegment', on_delete=models.CASCADE, null=True, blank=True, related_name='seg_geopath')

class MapImage(models.Model):
    map_type = models.CharField(max_length=12, choices=[("RouteMap", "RouteMap"), ("ElevationMap", "ElevationMap"), ("CustomMap", "CustomMap")])
    image = models.URLField()
    encoding_format = models.CharField(max_length=40)
    route_guide = models.ForeignKey('RouteGuide', on_delete=models.CASCADE, null=True, blank=True, related_name='rg_mapimage')
    route_guide_segment = models.ForeignKey('RouteGuideSegment', on_delete=models.CASCADE, null=True, blank=True, related_name='seg_mapimage')

class VerificationRecord(models.Model):
    verified_by = models.ManyToManyField(PersonAndOrganization, verbose_name='Verified By')
    date_verified = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Date Verified')
    route_guide = models.ForeignKey('RouteGuide', on_delete=models.CASCADE, blank=True, null=True, related_name='rg_verification_record')
    route_guide_segment = models.ForeignKey('RouteGuideSegment', on_delete=models.CASCADE, blank=True, null=True, related_name='seg_verification_record')

class AccessibilityDescription(models.Model):
    description = models.CharField(max_length=250)
    route_guide = models.ForeignKey('RouteGuide', on_delete=models.CASCADE, blank=True, null=True, related_name='rg_access_description')
    route_guide_segment = models.ForeignKey('RouteGuideSegment', on_delete=models.CASCADE, blank=True, null=True, related_name='seg_access_description')

class Activity(models.Model):
    prefLabel = models.CharField(max_length=100)
    identifier = models.URLField(verbose_name='Identifier')

class IndicativeDuration(models.Model):
    duration = models.CharField(max_length=10, verbose_name='Duration (8601)') # TODO: Add regex for validation
    activity = models.ForeignKey('Activity', on_delete=models.CASCADE, verbose_name='Activity', null=True)
    route_guide = models.ForeignKey('RouteGuide', on_delete=models.CASCADE, null=True, blank=True,related_name='rg_duration')
    route_guide_segment = models.ForeignKey('RouteGuideSegment', on_delete=models.CASCADE, null=True, blank=True, related_name='seg_duration')

class AmenityFeature(models.Model):
    name = models.CharField(max_length=75)
    routepoint = models.ForeignKey('RoutePoint', on_delete=models.CASCADE, blank=True, null=True, related_name='rp_amenity')

class GeoCoordinates(models.Model):
    latitude = models.FloatField(verbose_name='Latitude')
    longitude = models.FloatField(verbose_name='Longitude')
    postal_code = models.CharField(max_length=10, verbose_name='Post Code', null=True, blank=True)
    routepoint = models.OneToOneField('RoutePoint', on_delete=models.CASCADE, blank=True, null=True, related_name='rp_geo')

class RoutePoint(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    is_access_point = models.BooleanField()
    is_preferred_access_point = models.BooleanField(verbose_name='Is Preferred Access Point')
    description = models.TextField(blank=True, verbose_name='Description')
    headline = models.CharField(blank=True, max_length=200, verbose_name='Headline (Brief Description)')
    same_as = models.URLField(verbose_name='Same As', blank=True, null=True)
    is_start_point = models.BooleanField(verbose_name='Is Start Point', default=False)
    is_end_point = models.BooleanField(verbose_name='Is End Point', default=False)

class RouteGradient(models.Model):
    max_gradient = models.CharField(max_length=10)
    avg_gradient = models.CharField(max_length=10)
    total_elevation_gain = models.CharField(max_length=9, verbose_name='Total Elevation Loss')
    total_elevation_loss = models.CharField(max_length=9, verbose_name='Total Elevation Loss')
    gradient_term = models.CharField(max_length=100, verbose_name='Gradient Term')
    gradient_defurl = models.URLField(verbose_name='Gradient Definition URL')
    description = models.CharField(max_length=250)
    route_guide = models.OneToOneField('RouteGuide', on_delete=models.CASCADE, null=True, blank=True,related_name='rg_gradient')
    route_guide_segment = models.OneToOneField('RouteGuideSegment', on_delete=models.CASCADE, null=True, blank=True, related_name='seg_gradient')

class RouteDifficulty(models.Model):
    difficulty_term = models.CharField(max_length=15)
    description = models.CharField(max_length=250)
    difficulty_defurl = models.URLField(verbose_name='Difficulty Definition URL')
    route_guide = models.ForeignKey('RouteGuide', on_delete=models.CASCADE, null=True, blank=True, related_name='rg_difficulty')
    route_guide_segment = models.ForeignKey('RouteGuideSegment', on_delete=models.CASCADE, null=True, blank=True, related_name='seg_difficulty')

class RouteLegalAdvisory(models.Model):
    route_designation = models.OneToOneField('RouteDesignation', on_delete=models.CASCADE, verbose_name='Route Designation')
    description = models.CharField(max_length=250)
    legal_defurl = models.URLField(verbose_name='Legal Definition URL')
    route_guide = models.OneToOneField('RouteGuide', on_delete=models.CASCADE, null=True, blank=True, related_name='rg_legal_advisory')
    route_guide_segment = models.OneToOneField('RouteGuideSegment', on_delete=models.CASCADE, null=True, blank=True, related_name='seg_legal_advisory')

class RouteDesignation(models.Model):
    term = models.ManyToManyField('RouteDesignationTerm', verbose_name='Route Designation Term', related_name='terms')
    description = models.CharField(max_length=250)
    url = models.URLField(verbose_name='Formal Definition URL')
    legal_advisory = models.ForeignKey('RouteLegalAdvisory', on_delete=models.CASCADE, null=True, blank=True, related_name='rg_route_designation')

class RouteDesignationTerm(models.Model):
    term = models.CharField(max_length=100)

class Image(models.Model):
    caption = models.CharField(max_length=250, verbose_name='Caption')
    url = models.URLField(verbose_name='Image URL')
    encoding_format = models.CharField(max_length=40, verbose_name='Encoding Format')
    size = models.CharField(max_length=20, verbose_name='Size')
    width = models.IntegerField(verbose_name='Width')
    height = models.IntegerField(verbose_name='Height')
    route_guide = models.ForeignKey('RouteGuide', on_delete=models.CASCADE, null=True, blank=True, related_name='image')

class RouteSegmentGroup(models.Model):
    id_as_url = models.URLField(verbose_name='@id', blank=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    segments = models.ManyToManyField('RouteGuideSegment', verbose_name='Includes Segments', related_name='rg_route_segment_group')
    alternatives = models.ForeignKey('RouteSegmentGroup', on_delete=models.CASCADE, verbose_name='Alternative Group To', related_name='seg_route_segment_group')

class UserGeneratedContent(models.Model):
    creator = models.ForeignKey(PersonAndOrganization, on_delete=models.CASCADE, related_name='created_by')
    accountable_person = models.ForeignKey(PersonAndOrganization, on_delete=models.CASCADE)
    spatial_coverage = models.CharField(max_length=500)
    associated_media = models.CharField(max_length=500)
    route_guide = models.ForeignKey('RouteGuide', on_delete=models.CASCADE, null=True, blank=True, related_name='user_generated_content')

class RouteGuide(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name='Name')
    url = models.URLField(verbose_name='Trackback URL', blank=True)
    date_published = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False, verbose_name='Date Published')
    date_modified = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False, verbose_name='Date Modified')
    description = models.TextField(blank=True, verbose_name='Description')
    headline = models.CharField(blank=True, max_length=200, verbose_name='Headline (Brief Description)')
    distance = models.CharField(max_length=9, verbose_name='Distance')
    is_loop = models.BooleanField(verbose_name='Is Loop', default=True)
    id_as_url = models.URLField(verbose_name='ID (URL)')
    author = models.ManyToManyField(PersonAndOrganization, verbose_name='Author')
    activity = models.ManyToManyField(Activity, blank=True)
    categories = models.ManyToManyField('Category', verbose_name='Category', related_name="categories", blank=True)
    surfaces = models.ManyToManyField('Surface', verbose_name='Surface', related_name="surfaces", blank=True)
    suggested_equipment = models.ManyToManyField('SuggestedEquipment', verbose_name='Equipment', related_name="equipment", blank=True)
    additional_info = models.ManyToManyField('Article', verbose_name='Additional Info', blank=True, related_name="additional_info")
    route_point = models.ManyToManyField('RoutePoint', blank=True)

class RouteGuideSegment(models.Model):
    # TODO: check blank values permitted align with specification
    # TODO: rename this and related to RouteSegmentGuide **not** RouteGuideSegment
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name='Name')
    author = models.ManyToManyField(PersonAndOrganization, verbose_name='Author')
    url = models.URLField(verbose_name='Trackback URL', blank=True)
    date_published = models.DateField(blank=True, auto_now=False, auto_now_add=False, verbose_name='Date Published')
    date_modified = models.DateField(blank=True, auto_now=False, auto_now_add=False, verbose_name='Date Modified')
    description = models.TextField(blank=True, verbose_name='Description')
    headline = models.CharField(blank=True, max_length=200, verbose_name='Headline (Brief Description)')
    is_loop = models.BooleanField(verbose_name='Is Loop', default=True)
    id_as_url = models.URLField(verbose_name='ID (URL)')
    sequence = models.IntegerField(verbose_name='Segment Number')
    activity = models.ManyToManyField(Activity)
    additional_info = models.ManyToManyField('Article', verbose_name='Additional Info', blank=True, related_name="seg_additional_info")
    route_guide = models.ForeignKey('RouteGuide', on_delete=models.CASCADE, blank=True, null=True, related_name='seg_route_guide')
    point_of_interest = models.ManyToManyField('RoutePoint', blank=True)

class RouteRiskAdvisory(models.Model):
    risk_description = models.CharField(max_length=250)
    user_safety_feedback = models.CharField(max_length=500) # TODO: expand into schema:Review object
    is_maintained = models.BooleanField()
    risk_information_url = models.URLField()
    traffic_description = models.CharField(max_length=500)
    maintained_by = models.ForeignKey(PersonAndOrganization, on_delete=models.CASCADE, verbose_name='Is Maintained By', related_name='maintains', blank=True, null=True)
    known_risk = models.ForeignKey('KnownRisk', on_delete=models.CASCADE, blank=True, null=True)
    risk_modifier = models.ForeignKey('RiskModifier', on_delete=models.CASCADE, blank=True, null=True)
    risk_mitigator = models.ForeignKey('RiskMitigator', on_delete=models.CASCADE, blank=True, null=True)
    route_guide = models.OneToOneField('RouteGuide', on_delete=models.CASCADE, null=True, blank=True, related_name='rg_risk_advisory')
    route_guide_segment = models.ForeignKey('RouteGuideSegment', on_delete=models.CASCADE, null=True, blank=True, related_name='seg_risk_advisory')

class KnownRisk(models.Model):
    description = models.CharField(max_length=100)

class RiskModifier(models.Model):
    description = models.CharField(max_length=100)

class RouteAccessRestriction(models.Model):
    description = models.CharField(max_length=250)
    terms = models.ManyToManyField('RouteAccessRestrictionTerm', blank=True)
    information_url = models.URLField()
    timespan = models.CharField(max_length=50)
    route_guide = models.ForeignKey('RouteGuide', on_delete=models.CASCADE, null=True, blank=True, related_name='rg_access_restriction')
    route_guide_segment = models.ForeignKey('RouteGuideSegment', on_delete=models.CASCADE, null=True, blank=True, related_name='seg_access_restriction')

class RouteAccessRestrictionTerm(models.Model):
    description = models.CharField(max_length=250)

class RiskMitigator(models.Model):
    description = models.CharField(max_length=100)
