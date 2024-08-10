from django.test import TestCase
from meetings.forms import MeetingForm
from meetings.models import Room
from datetime import date, time, timedelta

class TestMeetingForm(TestCase):

    def setUp(self):
        self.room = Room.objects.create(name="Room 1", floor=1, room_number=101)

    def test_form_is_valid(self):
        future_date = date.today() + timedelta(days=1)  # we are using future date
        form = MeetingForm({
            'title': 'Test Meeting',
            'date': future_date,
            'start_time': time(9, 0),
            'duration': 2,
            'room': self.room.id  # we are using room id
        })
        self.assertTrue(form.is_valid(), msg="Form is invalid")

    def test_form_is_invalid(self):
        form = MeetingForm({
            'title': '',
            'date': '',
            'start_time': '',
            'duration': '',
            'room': ''
        })
        self.assertFalse(form.is_valid(), msg="Form is valid")
