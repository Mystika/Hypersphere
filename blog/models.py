from django.contrib.auth.models import models

class Blog(models.Model):
    username = models.CharField(max_length=20,unique=True)
    created_date = models.DateTimeField()
    is_active = models.IntegerField()
    is_locked = models.IntegerField()
    last_visits = models.DateTimeField()

    class Meta:
        db_table = 'Blogs'
