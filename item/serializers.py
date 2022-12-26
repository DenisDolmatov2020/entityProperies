from django.db.models import Manager
from rest_framework.fields import IntegerField, HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer, ListSerializer

from item.models import Entity, Property


class PropertyListSerializer(ListSerializer):

    def to_representation(self, data):
        props = data.all() if isinstance(data, Manager) else data

        return {
            prop.key: prop.value for prop in props
        }


class PropertySerializer(ModelSerializer):
    class Meta:
        list_serializer_class = PropertyListSerializer
        model = Property
        fields = ('key', 'value')


class EntitySerializer(ModelSerializer):
    value = IntegerField(required=False)
    modified_by = HiddenField(default=CurrentUserDefault())
    properties = PropertySerializer(many=True)

    class Meta:
        model = Entity
        fields = '__all__'

    def create(self, validated_data):
        value = validated_data.pop('value', '')
        if not value:
            value = self.initial_data.get("data[value]")
        props = validated_data.pop('properties', [])
        entity = Entity.objects.create(**validated_data, value=value)

        if props:
            props_created = Property.objects.bulk_create(
                Property(**prop)
                for prop in props
            )

            entity.properties.set(props_created)
        return entity
