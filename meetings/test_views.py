from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from meetings.models import Room, Meeting
from datetime import datetime, timedelta

class TestMeetingViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="password"
        )
        self.room = Room.objects.create(name="Room 1", floor=1, room_number=101)
        future_date = datetime.now().date() + timedelta(days=1)  # we are using future date
        self.meeting = Meeting.objects.create(
            title="Test Meeting",
            description="Test Description",
            date=future_date,
            start_time=datetime.now().time(),
            duration=1,
            room=self.room,
            created_by=self.user
        )

    def test_meeting_create_view(self):
        self.client.login(username="testuser", password="password")
        future_date = datetime.now().date() + timedelta(days=1)  
        response = self.client.post(reverse('new'), {
            'title': 'New Meeting',
            'date': future_date,
            'start_time': '10:00',
            'duration': 1,
            'room': self.room.id  # we are using room id
        })
        if response.status_code != 302:
            print(response.content)
        self.assertEqual(response.status_code, 302)

    def test_meeting_edit_view(self):
        self.client.login(username="testuser", password="password")
        future_date = datetime.now().date() + timedelta(days=1)  
        response = self.client.post(reverse('edit_meeting', args=[self.meeting.id]), {
            'title': 'Updated Meeting',
            'date': future_date,
            'start_time': '11:00',
            'duration': 2,
            'room': self.room.id  
        })
        if response.status_code != 302:
            print(response.content)
        self.assertEqual(response.status_code, 302)
