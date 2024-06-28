from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from network_graph.models.relationship_data import RelationshipData
from network_graph.serializers.relationship_serializer import RelationshipDataSerializer
import pandas as pd
import plotly.express as px


class RelationshipDataListView(generics.ListAPIView):
    queryset = RelationshipData.objects.all()
    serializer_class = RelationshipDataSerializer

@api_view(['GET'])
def child_nodes_view(request, parent):
    children = RelationshipData.objects.filter(entity1_parent=parent)
    serializer = RelationshipDataSerializer(children, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def show_data_on_graph(request):
    data = RelationshipData.objects.all().values()
    df = pd.DataFrame(data)
    
    fig = px.sunburst(df, path=['entity1_parent', 'entity1', 'entity2_parent', 'entity2'])
    graph_json = fig.to_json()
    
    return Response(graph_json)