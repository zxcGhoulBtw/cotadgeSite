from django.db import models


class task(models.Model):
    title = models.CharField("НазваниеO", max_length= 50)
    task = models.TextField("Описание")

    def _str_(self):
        return self.title
