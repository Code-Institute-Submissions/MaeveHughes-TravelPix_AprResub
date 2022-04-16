"""Config for apps"""

from django.apps import AppConfig


class PhotologConfig(AppConfig):
    """Config for Photolog App"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'photolog'
