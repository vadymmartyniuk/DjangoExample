from rest_framework import serializers

from lab6.models import Lab6


class Lab6Serializer(serializers.ModelSerializer):
    x1_res = serializers.SerializerMethodField()
    y1_res = serializers.SerializerMethodField()
    x2_res = serializers.SerializerMethodField()
    y2_res = serializers.SerializerMethodField()

    class Meta:
        model = Lab6
        fields = '__all__'

    def get_x1_res(self, obj):
        x1_res, _ = self.euler_method(obj)
        return x1_res

    def get_y1_res(self, obj):
        _, y1_res = self.euler_method(obj)
        return y1_res

    def get_x2_res(self, obj):
        # Call your custom method to calculate this value
        x2_res, _ = self.euler_cauchy_method(obj)
        return x2_res

    def get_y2_res(self, obj):
        # Call your custom method to calculate this value
        _, y2_res = self.euler_cauchy_method(obj)
        return y2_res

    def euler_method(self, obj):
        # Your implementation here
        return [1, 2, 3], [3, 2, 1]

    def euler_cauchy_method(self, obj):
        # Your implementation here
        return [4, 5, 6], [6, 5, 4]