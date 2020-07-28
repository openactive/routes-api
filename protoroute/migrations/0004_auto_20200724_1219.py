# Generated by Django 3.0.7 on 2020-07-24 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('protoroute', '0003_auto_20200724_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routeguide',
            name='accessibility_description',
        ),
        migrations.RemoveField(
            model_name='routeguidesegment',
            name='category',
        ),
        migrations.RemoveField(
            model_name='routeguidesegment',
            name='route_difficulty',
        ),
        migrations.RemoveField(
            model_name='routepoint',
            name='amenity',
        ),
        migrations.RemoveField(
            model_name='routepoint',
            name='transport_note',
        ),
        migrations.AddField(
            model_name='accessibilitydescription',
            name='route_guide',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rg_access_description', to='protoroute.RouteGuide'),
        ),
        migrations.AddField(
            model_name='accessibilitydescription',
            name='route_guide_segment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seg_access_description', to='protoroute.RouteGuideSegment'),
        ),
        migrations.AddField(
            model_name='amenityfeature',
            name='routepoint',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='protoroute.RoutePoint'),
        ),
        migrations.AddField(
            model_name='transportnote',
            name='routepoint',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='protoroute.RoutePoint'),
        ),
    ]