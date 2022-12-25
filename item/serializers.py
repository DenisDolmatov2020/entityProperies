from abc import ABC

from django.db.models import Manager
from rest_framework import serializers
from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer

from item.models import Entity, Property


class PropertyListSerializer(serializers.ListSerializer, ABC):

    def to_representation(self, data):
        props = data.all() if isinstance(data, Manager) else data

        return {
            prop.key: prop.value for prop in props
        }


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        list_serializer_class = PropertyListSerializer
        model = Property
        fields = ('key', 'value')


class EntitySerializer(ModelSerializer):
    value = IntegerField(required=False)
    properties = PropertySerializer(many=True)

    class Meta:
        model = Entity
        fields = '__all__'

    def create(self, validated_data):
        value = validated_data.pop('value')
        modified_by = validated_data.pop('modified_by')
        data = validated_data.pop('data', {})
        if data:
            value = data['value']
        entity = Entity.objects.create(value=value, modified_by=modified_by)

        props = validated_data.pop('properties', [])
        if props:
            props_created = Property.objects.bulk_create(
                Property(**prop)
                for prop in props
            )

            entity.properties.set(props_created)
        return entity
