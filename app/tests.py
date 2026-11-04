from django.test import TestCase

from .models import Cakes, Category, Shape, Weight
from .serializers import CakeSerializer


class CakeSerializerTests(TestCase):

    def test_category_field_accepts_primary_key_and_returns_category_data(self):
        category = Category.objects.create(name='Birthday')
        field = CakeSerializer().fields['category']

        self.assertEqual(field.run_validation(category.pk), category)
        self.assertEqual(
            field.to_representation(category),
            {'id': category.pk, 'name': 'Birthday'},
        )

    def test_cake_serialization_returns_related_model_data(self):
        category = Category.objects.create(name='Birthday')
        shape = Shape.objects.create(name='Round')
        weight = Weight.objects.create(name='1 kg')
        cake = Cakes.objects.create(
            name='Chocolate Cake',
            description='Rich chocolate cake',
            category=category,
            shape=shape,
            weight=weight,
            price=1000,
        )

        data = CakeSerializer(cake).data

        self.assertEqual(data['category'], {'id': category.pk, 'name': 'Birthday'})
        self.assertEqual(data['shape'], {'id': shape.pk, 'name': 'Round'})
        self.assertEqual(data['weight'], {'id': weight.pk, 'name': '1 kg'})


# Create your tests here.
