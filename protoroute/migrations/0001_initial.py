# Generated by Django 3.1 on 2020-10-08 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefLabel', models.CharField(max_length=100)),
                ('identifier', models.URLField(verbose_name='Identifier')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('image_url', models.URLField(blank=True, null=True, verbose_name='Image URL')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='KnownRisk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PersonAndOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('website', models.URLField(blank=True, verbose_name='Website')),
            ],
        ),
        migrations.CreateModel(
            name='RiskMitigator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RiskModifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RouteAccessRestrictionTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='RouteDesignation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('url', models.URLField(verbose_name='Formal Definition URL')),
            ],
        ),
        migrations.CreateModel(
            name='RouteDesignationTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RouteGuide',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('url', models.URLField(blank=True, verbose_name='Trackback URL')),
                ('date_published', models.DateField(null=True, verbose_name='Date Published')),
                ('date_modified', models.DateField(null=True, verbose_name='Date Modified')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('headline', models.CharField(blank=True, max_length=200, null=True, verbose_name='Headline (Brief Description)')),
                ('distance', models.CharField(max_length=9, verbose_name='Distance')),
                ('is_loop', models.BooleanField(blank=True, default=True, null=True, verbose_name='Is Loop')),
                ('id_as_url', models.URLField(verbose_name='ID (URL)')),
                ('activity', models.ManyToManyField(blank=True, to='protoroute.Activity')),
                ('additional_info', models.ManyToManyField(blank=True, related_name='additional_info', to='protoroute.Article', verbose_name='Additional Info')),
                ('author', models.ManyToManyField(blank=True, null=True, to='protoroute.PersonAndOrganization', verbose_name='Author')),
                ('categories', models.ManyToManyField(blank=True, related_name='categories', to='protoroute.Category', verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='RouteGuideSegment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Trackback URL')),
                ('date_published', models.DateField(blank=True, verbose_name='Date Published')),
                ('date_modified', models.DateField(blank=True, verbose_name='Date Modified')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('headline', models.CharField(blank=True, max_length=200, verbose_name='Headline (Brief Description)')),
                ('is_loop', models.BooleanField(default=True, verbose_name='Is Loop')),
                ('id_as_url', models.URLField(verbose_name='ID (URL)')),
                ('sequence', models.IntegerField(verbose_name='Segment Number')),
                ('activity', models.ManyToManyField(to='protoroute.Activity')),
                ('additional_info', models.ManyToManyField(blank=True, related_name='seg_additional_info', to='protoroute.Article', verbose_name='Additional Info')),
                ('author', models.ManyToManyField(to='protoroute.PersonAndOrganization', verbose_name='Author')),
            ],
        ),
        migrations.CreateModel(
            name='RoutePoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('is_access_point', models.BooleanField()),
                ('is_preferred_access_point', models.BooleanField(verbose_name='Is Preferred Access Point')),
                ('description', models.TextField(verbose_name='Description')),
                ('headline', models.CharField(blank=True, max_length=200, null=True, verbose_name='Headline (Brief Description)')),
                ('same_as', models.URLField(blank=True, null=True, verbose_name='Same As')),
                ('is_start_point', models.BooleanField(default=False, verbose_name='Is Start Point')),
                ('is_end_point', models.BooleanField(default=False, verbose_name='Is End Point')),
            ],
        ),
        migrations.CreateModel(
            name='SuggestedEquipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Surface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surface', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='VerificationRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_verified', models.DateField(verbose_name='Date Verified')),
                ('route_guide', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rg_verification_record', to='protoroute.routeguide')),
                ('route_guide_segment', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seg_verification_record', to='protoroute.routeguidesegment')),
                ('verified_by', models.ManyToManyField(to='protoroute.PersonAndOrganization', verbose_name='Verified By')),
            ],
        ),
        migrations.CreateModel(
            name='UserGeneratedContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spatial_coverage', models.CharField(max_length=500)),
                ('associated_media', models.CharField(max_length=500)),
                ('accountable_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='protoroute.personandorganization')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to='protoroute.personandorganization')),
                ('route_guide', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_generated_content', to='protoroute.routeguide')),
            ],
        ),
        migrations.CreateModel(
            name='TransportNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transport_mode', models.CharField(choices=[('Bus', 'Bus'), ('Rail', 'Rail'), ('Road', 'Road'), ('Foot', 'Foot'), ('Bicycle', 'Bicycle')], max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('routepoint', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rp_transport_note', to='protoroute.routepoint')),
            ],
        ),
        migrations.CreateModel(
            name='RouteSegmentGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_as_url', models.URLField(verbose_name='@id')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('alternatives', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seg_route_segment_group', to='protoroute.routesegmentgroup', verbose_name='Alternative Group To')),
                ('segments', models.ManyToManyField(related_name='rg_route_segment_group', to='protoroute.RouteGuideSegment', verbose_name='Includes Segments')),
            ],
        ),
        migrations.CreateModel(
            name='RouteRiskAdvisory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risk_description', models.CharField(max_length=250)),
                ('user_safety_feedback', models.CharField(max_length=500)),
                ('is_maintained', models.BooleanField()),
                ('risk_information_url', models.URLField()),
                ('traffic_description', models.CharField(max_length=500)),
                ('known_risk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='protoroute.knownrisk')),
                ('maintained_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maintains', to='protoroute.personandorganization', verbose_name='Is Maintained By')),
                ('risk_mitigator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='protoroute.riskmitigator')),
                ('risk_modifier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='protoroute.riskmodifier')),
                ('route_guide', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rg_risk_advisory', to='protoroute.routeguide')),
                ('route_guide_segment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seg_risk_advisory', to='protoroute.routeguidesegment')),
            ],
        ),
        migrations.CreateModel(
            name='RouteLegalAdvisory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('legal_defurl', models.URLField(verbose_name='Legal Definition URL')),
                ('route_designation', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='protoroute.routedesignation', verbose_name='Route Designation')),
                ('route_guide', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rg_legal_advisory', to='protoroute.routeguide')),
                ('route_guide_segment', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seg_legal_advisory', to='protoroute.routeguidesegment')),
            ],
        ),
        migrations.AddField(
            model_name='routeguidesegment',
            name='point_of_interest',
            field=models.ManyToManyField(blank=True, to='protoroute.RoutePoint'),
        ),
        migrations.AddField(
            model_name='routeguidesegment',
            name='route_guide',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seg_route_guide', to='protoroute.routeguide'),
        ),
        migrations.AddField(
            model_name='routeguide',
            name='route_point',
            field=models.ManyToManyField(blank=True, to='protoroute.RoutePoint'),
        ),
        migrations.AddField(
            model_name='routeguide',
            name='suggested_equipment',
            field=models.ManyToManyField(blank=True, related_name='equipment', to='protoroute.SuggestedEquipment', verbose_name='Equipment'),
        ),
        migrations.AddField(
            model_name='routeguide',
            name='surfaces',
            field=models.ManyToManyField(blank=True, related_name='surfaces', to='protoroute.Surface', verbose_name='Surface'),
        ),
        migrations.CreateModel(
            name='RouteGradient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_gradient', models.CharField(max_length=10)),
                ('avg_gradient', models.CharField(max_length=10)),
                ('total_elevation_gain', models.CharField(max_length=9, verbose_name='Total Elevation Loss')),
                ('total_elevation_loss', models.CharField(max_length=9, verbose_name='Total Elevation Loss')),
                ('gradient_term', models.CharField(max_length=100, verbose_name='Gradient Term')),
                ('gradient_defurl', models.URLField(verbose_name='Gradient Definition URL')),
                ('description', models.CharField(max_length=250)),
                ('route_guide', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rg_gradient', to='protoroute.routeguide')),
                ('route_guide_segment', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seg_gradient', to='protoroute.routeguidesegment')),
            ],
        ),
        migrations.CreateModel(
            name='RouteDifficulty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty_term', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=250)),
                ('difficulty_defurl', models.URLField(verbose_name='Difficulty Definition URL')),
                ('activity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='protoroute.activity', verbose_name='Activity')),
                ('route_guide', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rg_difficulty', to='protoroute.routeguide')),
                ('route_guide_segment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seg_difficulty', to='protoroute.routeguidesegment')),
            ],
        ),
        migrations.AddField(
            model_name='routedesignation',
            name='legal_advisory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rg_route_designation', to='protoroute.routelegaladvisory'),
        ),
        migrations.AddField(
            model_name='routedesignation',
            name='term',
            field=models.ManyToManyField(related_name='terms', to='protoroute.RouteDesignationTerm', verbose_name='Route Designation Term'),
        ),
        migrations.CreateModel(
            name='RouteAccessRestriction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('information_url', models.URLField()),
                ('timespan', models.CharField(max_length=50)),
                ('route_guide', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rg_access_restriction', to='protoroute.routeguide')),
                ('route_guide_segment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seg_access_restriction', to='protoroute.routeguidesegment')),
                ('terms', models.ManyToManyField(blank=True, to='protoroute.RouteAccessRestrictionTerm')),
            ],
        ),
        migrations.CreateModel(
            name='Provenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provenance_url', models.URLField(verbose_name='Provenance')),
                ('version', models.DateField()),
                ('description', models.CharField(max_length=250)),
                ('publisher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='protoroute.personandorganization')),
                ('route_guide', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rg_provenance', to='protoroute.routeguide')),
                ('route_guide_segment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seg_provenance', to='protoroute.routeguidesegment')),
            ],
        ),
        migrations.CreateModel(
            name='MapReference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map_series', models.CharField(max_length=50)),
                ('map_number', models.CharField(max_length=10)),
                ('grid_reference', models.CharField(max_length=10)),
                ('publisher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publisher', to='protoroute.personandorganization', verbose_name='publisher')),
                ('routepoint', models.ManyToManyField(related_name='rp_mapref', to='protoroute.RoutePoint')),
            ],
        ),
        migrations.CreateModel(
            name='MapImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map_type', models.CharField(choices=[('RouteMap', 'RouteMap'), ('ElevationMap', 'ElevationMap'), ('CustomMap', 'CustomMap')], max_length=12)),
                ('image', models.URLField()),
                ('encoding_format', models.CharField(max_length=40)),
                ('route_guide', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rg_mapimage', to='protoroute.routeguide')),
                ('route_guide_segment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seg_mapimage', to='protoroute.routeguidesegment')),
            ],
        ),
        migrations.CreateModel(
            name='IndicativeDuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.CharField(max_length=10, verbose_name='Duration (8601)')),
                ('activity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='protoroute.activity', verbose_name='Activity')),
                ('route_guide', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rg_duration', to='protoroute.routeguide')),
                ('route_guide_segment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seg_duration', to='protoroute.routeguidesegment')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=250, verbose_name='Caption')),
                ('url', models.URLField(verbose_name='Image URL')),
                ('encoding_format', models.CharField(max_length=40, verbose_name='Encoding Format')),
                ('size', models.CharField(max_length=20, verbose_name='Size')),
                ('width', models.IntegerField(verbose_name='Width')),
                ('height', models.IntegerField(verbose_name='Height')),
                ('route_guide', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image', to='protoroute.routeguide')),
            ],
        ),
        migrations.CreateModel(
            name='GeoPath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map_type', models.CharField(choices=[('RouteMap', 'RouteMap'), ('ElevationMap', 'ElevationMap'), ('CustomMap', 'CustomMap')], max_length=12)),
                ('url', models.URLField()),
                ('encoding_format', models.CharField(max_length=40)),
                ('route_guide', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rg_geopath', to='protoroute.routeguide')),
                ('route_guide_segment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seg_geopath', to='protoroute.routeguidesegment')),
            ],
        ),
        migrations.CreateModel(
            name='GeoCoordinates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(verbose_name='Latitude')),
                ('longitude', models.FloatField(verbose_name='Longitude')),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Post Code')),
                ('routepoint', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rp_geo', to='protoroute.routepoint')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='protoroute.personandorganization', verbose_name='Author'),
        ),
        migrations.CreateModel(
            name='AmenityFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('routepoint', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rp_amenity', to='protoroute.routepoint')),
            ],
        ),
        migrations.CreateModel(
            name='AccessibilityDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('route_guide', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rg_access_description', to='protoroute.routeguide')),
                ('route_guide_segment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seg_access_description', to='protoroute.routeguidesegment')),
            ],
        ),
    ]
