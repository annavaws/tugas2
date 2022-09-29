import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    date = datetime.datetime.now()
    title = models.TextField()
    description = models.TextField()
    is_finished = models.CharField(
        max_length=100,
        choices=(("Selesai", "Selesai"),
                 ("Belum Selesai", "Belum selesai")),
        default="Belum Selesai",
    )
    # untuk tampilan admin
    def __str__(self) -> str:
        return self.title + "---" + str(self.date)

    def get_status(self) -> str:
        return "Selesai" if self.is_finished else "Belum Selesai"
