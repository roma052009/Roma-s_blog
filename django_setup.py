import os
import django


os.environ.setdefault(key="DJANGO_SETTINGS_MODULE", value="MyBlog.settings")
django.setup()