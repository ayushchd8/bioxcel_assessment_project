from django.db import models

class RelationshipData(models.Model):
    entity1_parent = models.CharField(max_length=100)
    entity1 = models.CharField(max_length=50)
    entity1_type = models.CharField(max_length=50)
    entity2_parent = models.CharField(max_length=100)
    entity2 = models.CharField(max_length=50)
    entity2_type = models.CharField(max_length=50)
    relationship = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.entity1} - {self.relationship} - {self.entity2}"