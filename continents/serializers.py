"""Serializers from DRF"""
from rest_framework import serializers
from continents.models import Continent


class ContinentSerializer(serializers.ModelSerializer):
    """Serialization and desiaralization
    :param Continent: data structure for the continents
    of the world"""

    first_image = serializers.SerializerMethodField('get_first_image')
    second_image = serializers.SerializerMethodField('get_second_image')
    third_image = serializers.SerializerMethodField('get_third_image')

    class Meta:
        """Custom settings"""
        model = Continent
        fields = ('name', 'place', 'population', 'overview', 'languages',
                  'first_image', 'second_image', 'third_image')
    """Code for succesful to deploying to Heroku"""
    def get_first_image(self, obj):
        request = self.context.get("request")
        image_path = obj.first_image
        host = request._request.META.get('HTTP_HOST')
        new_image_path = "https://{}/static/{}".format(host, image_path)
        return new_image_path

    def get_second_image(self, obj):
        request = self.context.get("request")
        image_path = obj.second_image
        host = request._request.META.get('HTTP_HOST')
        new_image_path = "https://{}/static/{}".format(host, image_path)
        return new_image_path

    def get_third_image(self, obj):
        request = self.context.get("request")
        image_path = obj.third_image
        host = request._request.META.get('HTTP_HOST')
        new_image_path = "https://{}/static/{}".format(host, image_path)
        return new_image_path
