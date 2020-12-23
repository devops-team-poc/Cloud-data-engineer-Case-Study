from rest_framework import serializers

# Get the UserModel
from accounts.models import UberEatsMenu, TripAdvisorOutlet, UberEatsOutlet


class OutletSerializer(serializers.ModelSerializer):
    class Meta:
        model = UberEatsMenu
        fields = '__all__'


class TripAdvisorOutletSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripAdvisorOutlet
        fields = '__all__'


class UberEatsOutletSerializer(serializers.ModelSerializer):
    class Meta:
        model = UberEatsOutlet
        fields = '__all__'






