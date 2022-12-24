from django.contrib.auth.models import User
from django.db.models import Model, ForeignKey, IntegerField, CharField, ManyToManyField, CASCADE


class Property(Model):
    key = CharField(max_length=64)
    value = CharField(max_length=200)

    def __str__(self):
        return '{}: {}'.format(self.key, self.value)


class Entity(Model):
    modified_by = ForeignKey(User, on_delete=CASCADE)
    value = IntegerField()
    properties = ManyToManyField(Property)
