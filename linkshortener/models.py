from django.db import models


class Link(models.Model):
    old_link = models.URLField(blank=True, null=True)
    new_link = models.URLField(blank=True, null=True)
    num_views = models.PositiveIntegerField(default=0, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.old_link + " num of views: " + str(self.num_views)

