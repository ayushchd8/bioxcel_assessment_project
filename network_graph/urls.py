from django.urls import path
from network_graph.views.relationship_data import RelationshipDataListView, child_nodes_view, show_data_on_graph

urlpatterns = [
    path('relationships/', RelationshipDataListView.as_view(), name='relationships-list'),
    path('children/<str:parent>/', child_nodes_view, name='children-list'),
    path('graph/', show_data_on_graph, name='show-graph'),
]