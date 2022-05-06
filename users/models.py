from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)   
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path) 

        if img.height > 300 or img.width > 300:  
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



class user_info(models.Model):
    class Meta:
        verbose_name_plural = 'User Information'

    Mobel_User_Name = models.CharField(max_length=256, blank=True, null=True)
    Mobel_Email_Address = models.CharField(max_length=256, blank=True, null=True)
    Mobel_Password = models.CharField(max_length=256, blank=True, null=True)


    def __str__(self):
        return str(self.id)
class President_vote_count(models.Model):
    class Meta:
        verbose_name_plural = 'President vote'

    user_con = models.ForeignKey(user_info, on_delete=models.CASCADE, blank=True,null=True)
    person_get_vote = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return str(self.id)
class vice_President_vote_count(models.Model):
    class Meta:
        verbose_name_plural = 'vice President vote'

    user_con = models.ForeignKey(user_info, on_delete=models.CASCADE, blank=True, null=True)
    person_get_vote = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return str(self.id)
class senator_vote_count(models.Model):
    class Meta:
        verbose_name_plural = 'senator vote'

    user_con = models.ForeignKey(user_info, on_delete=models.CASCADE, blank=True, null=True)
    person_get_vote_1 = models.CharField(max_length=256, blank=True, null=True)
    person_get_vote_2 = models.CharField(max_length=256, blank=True, null=True)
    person_get_vote_3 = models.CharField(max_length=256, blank=True, null=True)
    person_get_vote_4 = models.CharField(max_length=256, blank=True, null=True)
    person_get_vote_5 = models.CharField(max_length=256, blank=True, null=True)
    person_get_vote_6 = models.CharField(max_length=256, blank=True, null=True)
    person_get_vote_7 = models.CharField(max_length=256, blank=True, null=True)
    person_get_vote_8 = models.CharField(max_length=256, blank=True, null=True)
    person_get_vote_9 = models.CharField(max_length=256, blank=True, null=True)
    person_get_vote_10 = models.CharField(max_length=256, blank=True, null=True)
    person_get_vote_11 = models.CharField(max_length=256, blank=True, null=True)
    person_get_vote_12 = models.CharField(max_length=256, blank=True, null=True)
    person_get_vote_13 = models.CharField(max_length=256, blank=True, null=True)
    person_get_vote_14 = models.CharField(max_length=256, blank=True, null=True)
    person_get_vote_15 = models.CharField(max_length=256, blank=True, null=True)
    person_get_vote_16 = models.CharField(max_length=256, blank=True, null=True)
    person_get_vote_17 = models.CharField(max_length=256, blank=True, null=True)
    person_get_vote_18 = models.CharField(max_length=256, blank=True, null=True)
    person_get_vote_19 = models.CharField(max_length=256, blank=True, null=True)
    person_get_vote_20 = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return str(self.id)