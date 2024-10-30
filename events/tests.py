from django.test import TestCase
from .models import Event, Location
from django.urls import reverse


class EventModelTest(TestCase):
    def setUp(self):
        self.location = Location.objects.create(
            name="Auditorio Principal",
            address="Calle Falsa 123",
            city="Ciudad Ejemplo",
            state="Estado Ejemplo"
        )
        self.event = Event.objects.create(
            name="Concierto de Prueba",
            short_description="Un concierto único",
            description="Detalles del concierto",
            date="2024-12-25",
            time="19:00:00",
            location=self.location,
            state="vigente"
        )

    def test_event_creation(self):
        self.assertEqual(self.event.name, "Concierto de Prueba")
        self.assertEqual(self.event.state, "vigente")
        self.assertEqual(self.event.location.name, "Auditorio Principal")


class LocationModelTest(TestCase):
    def setUp(self):
        self.location = Location.objects.create(
            name="Sala de Ensayo",
            address="Av. Música 456",
            city="Ciudad Musical",
            state="Estado Musical",
            capacity=50
        )

    def test_location_creation(self):
        self.assertEqual(self.location.name, "Sala de Ensayo")
        self.assertEqual(self.location.capacity, 50)


# %%

class EventListViewTest(TestCase):
    def setUp(self):
        Event.objects.create(name="Evento Test 1", date="2024-12-20", state="vigente", time="19:00:00")
        Event.objects.create(name="Evento Test 2", date="2024-12-21", state="pasado", time="20:00:00")

    def test_event_list_view(self):
        response = self.client.get(reverse("events"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Evento Test 1")
        self.assertContains(response, "Evento Test 2")

