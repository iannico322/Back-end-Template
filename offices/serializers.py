from rest_framework import serializers
from .models import Office


class OfficeSerializer(serializers.ModelSerializer):
    # Derived from the actual accounts.UserAccount rows pointing at this
    # office, instead of the stored `numUsers` column — nothing kept that
    # column in sync (no signals, no increment on user create/delete/move),
    # so it just reflected whatever was last typed into the office form.
    numUsers = serializers.SerializerMethodField()

    class Meta:
        model = Office
        fields = ['officeID', 'name', 'officeMail', 'street', 'city', 'province', 'region', 'numUsers']

    def get_numUsers(self, obj):
        return obj.useraccount_set.count()
