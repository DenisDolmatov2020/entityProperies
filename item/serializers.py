from rest_framework import serializers
from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer

from item.models import Entity, Property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('key', 'value')


'''
    def to_representation(self, instance):
        response = super().to_representation(instance)
        return {response['key']: response['value']}
'''


class EntitySerializer(ModelSerializer):
    value = IntegerField(required=False)
    properties = PropertySerializer(many=True)

    class Meta:
        model = Entity
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        properties = {}
        for p in response['properties']:
            properties[p['key']] = p['value']

        response['properties'] = properties

        return response

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
