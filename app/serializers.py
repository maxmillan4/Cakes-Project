from rest_framework import serializers

from .models import Cakes,Category,Shape,Weight

class CategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = Category

        fields = '__all__'

class ShapeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Shape

        fields = '__all__'

class WeightSerializer(serializers.ModelSerializer):

    class Meta:

        model = Weight

        fields = '__all__'

class CategoryField(serializers.PrimaryKeyRelatedField):

    def use_pk_only_optimization(self):
        return False

    def to_representation(self, value):

        return CategorySerializer(value).data

class ShapeField(serializers.PrimaryKeyRelatedField):

    def use_pk_only_optimization(self):
        return False

    def to_representation(self, value):

        return ShapeSerializer(value).data

class WeightField(serializers.PrimaryKeyRelatedField):

    def use_pk_only_optimization(self):
        return False

    def to_representation(self, value):

        return WeightSerializer(value).data

class CakeSerializer(serializers.ModelSerializer):

    category = CategoryField(queryset=Category.objects.all())

    shape = ShapeField(queryset=Shape.objects.all())

    weight = WeightField(queryset=Weight.objects.all())

    class Meta:

        model = Cakes

        # fields = ['name','description','photo']
        fields = '__all__'
        # exclude = ''