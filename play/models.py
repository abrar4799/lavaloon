from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Play(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    available_seats = models.IntegerField()

    def __str__(self):
        return self.title


class Seats(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    remaining_seats = models.IntegerField()
    play_date = models.DateField()


class PlayBooking(models.Model):
    user = models.EmailField()
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    play_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ensure uniqueness of user and play_date combination
        unique_together = ('user', 'play_date')


"""
Restrict by email + date
Idempotency keys

[3:54 PM] Muhammad Haggag
Duplicate reservations:
Restrict by email + date
Idempotency keys
 
[3:55 PM] Muhammad Haggag
Parallel reservations:
Multiple users reserving at the same time when only one seat remains
#   DB Locking 

"""




