from django.contrib import admin
from .models import post
from .models import comment
from .models import ans
from .models import feeds
from .models import social_media_account
from .models import profile_picture
from .models import feedbacks
from .models import contact_form_model
from .models import doctor




admin.site.register(post)
admin.site.register(comment)
admin.site.register(ans)
admin.site.register(feeds)
admin.site.register(social_media_account)
admin.site.register(profile_picture)
admin.site.register(feedbacks)
admin.site.register(contact_form_model)
admin.site.register(doctor)
