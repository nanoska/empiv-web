from django.test import TestCase
from .models import Workshop, Location
from django.urls import reverse

class WorkshopModelTest(TestCase):
    def setUp(self):
        self.workshop = Workshop.objects.create(
            name="Taller de Instrumentos",
            description="Aprendizaje de instrumentos de viento",
            day="Monday",
            init_time="10:00:00",
            end_time="12:00:00",
            price=100.00,
            max_participants=20
        )

    def test_workshop_creation(self):
        self.assertEqual(self.workshop.name, "Taller de Instrumentos")
        self.assertEqual(self.workshop.price, 100.00)


# %%

class WorkshopCreateViewTest(TestCase):
    def setUp(self):
        # Crear una ubicación de prueba para asociarla con el taller
        self.location = Location.objects.create(name="Ubicación de prueba")

    def test_workshop_create_view(self):
        response = self.client.post(reverse("workshop_create"), {
            "name": "Nuevo Taller",
            "description": "Descripción del nuevo taller",
            "day": "Tuesday",
            "init_time": "14:00:00",
            "end_time": "16:00:00",
            "price": 150.00,
            "max_participants": 25,
            "location": self.location.id,  # Incluye una ubicación
            # "image" puede omitirse o agregar un archivo de imagen válido si es requerido
        })
        self.assertEqual(response.status_code, 302)  # Redirección después de crear
        self.assertTrue(Workshop.objects.filter(name="Nuevo Taller").exists())