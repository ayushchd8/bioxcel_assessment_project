from rest_framework import serializers
from network_graph.models.relationship_data import RelationshipData

class RelationshipDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelationshipData
        fields = '__all__'