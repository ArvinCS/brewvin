from django.test import Client, TestCase

from main.models import Item

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/')
        self.assertTemplateUsed(response, 'main.html')
    
    def test_assign_item(self):
        # Create item
        Item.objects.create(
            name = 'Arabica',
            amount = 1,
            description = 'Most common coffee beans in Indonesia',
            taste = 'Aromatic but bittersweet'
        )

        # Validate created item
        arabica = Item.objects.get(name = 'Arabica')
        self.assertEqual(arabica.amount, 1)
        self.assertEqual(arabica.description, 'Most common coffee beans in Indonesia')
        self.assertEqual(arabica.taste, 'Aromatic but bittersweet')