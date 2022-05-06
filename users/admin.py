from django.contrib import admin
from .models import Profile, user_info, President_vote_count, vice_President_vote_count, senator_vote_count

# Register your models here.
admin.site.register(Profile),
admin.site.register(user_info),
admin.site.register(President_vote_count),
admin.site.register(vice_President_vote_count),
admin.site.register(senator_vote_count),