import pandas as pd
from django.core.management.base import BaseCommand
from network_graph.models.relationship_data import RelationshipData


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        file_path = 'network_graph/Datasets/Full_Stack_Developer_Task_Data.xlsx'
        data = pd.read_excel(file_path, sheet_name='RelationshipData')

        for _, row in data.iterrows():
            RelationshipData.objects.create(
                entity1_parent=row['Entity1_Parent'],
                entity1=row['Entity1'],
                entity1_type=row['Entity1_Type'],
                entity2_parent=row['Entity2_Parent'],
                entity2=row['Entity2'],
                entity2_type=row['Entity2_Type'],
                relationship=row['Relationship']
            )

        self.stdout.write(self.style.SUCCESS('Successfully loaded relationship data'))