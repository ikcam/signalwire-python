from unittest import TestCase
import os, pytest
from signalwire.rest import Client as signalwire_client
import vcr

@pytest.fixture(scope="module")
def client():
  client = signalwire_client('signalwire-account-123', '123456', signalwire_space_url = 'myaccount.signalwire.com')
  return client

@vcr.use_cassette()
def test_accounts(client):
  account = client.api.accounts('signalwire-account-123').fetch()
  assert(account.friendly_name == 'LAML testing') 
    

@vcr.use_cassette()
def test_applications(client):
  applications = client.applications.list()
  assert(applications[0].sid == '34f49a97-a863-4a11-8fef-bc399c6f0928')

@vcr.use_cassette()
def test_local_numbers(client):
  numbers = client.available_phone_numbers("US") \
                .local \
                .list(in_region="WA")
  assert(numbers[0].phone_number == '+12064015921')

@vcr.use_cassette()
def test_toll_free_numbers(client):
  numbers = client.available_phone_numbers("US") \
                .toll_free \
                .list(area_code="310")
  assert(numbers[0].phone_number == '+13103590741')

@vcr.use_cassette()
def test_conferences(client):
  conferences = client.conferences.list()

  assert(conferences[0].sid == 'a811cb2c-9e5a-415d-a951-701f8e884fb5')

@vcr.use_cassette()
def test_conference_members(client):
  participants = client.conferences('a811cb2c-9e5a-415d-a951-701f8e884fb5') \
                     .participants \
                     .list()

  assert(participants[0].call_sid == '7a520324-684d-435c-87c2-ea7975f371d0')

@vcr.use_cassette()
def test_incoming_phone_numbers(client):
  incoming_phone_numbers = client.incoming_phone_numbers.list()

  assert(incoming_phone_numbers[0].phone_number == '+18990000001')

@vcr.use_cassette()
def test_messages(client):
  message = client.messages.create(
      from_='+15059999999',
      to='+15058888888',
      media_url='https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png'
  )

  assert(message.sid == 'cbad786b-fdcd-4d2a-bcb2-fff9df045008')

@vcr.use_cassette()
def test_media(client):
  media = client.messages('0da01046-5cca-462f-bc50-adae4e1307e1').media.list()
  assert(media[0].sid == 'a1ee4484-99a4-4996-b7df-fd3ceef2e9ec')

@vcr.use_cassette()
def test_recordings(client):
  recordings = client.recordings.list()
  assert(recordings[0].call_sid == 'd411976d-d319-4fbd-923c-57c62b6f677a')

@vcr.use_cassette()
def test_transcriptions(client):
  transcriptions = client.transcriptions.list()
  assert(transcriptions[0].recording_sid == 'e4c78e17-c0e2-441d-b5dd-39a6dad496f8')

@vcr.use_cassette()
def test_queues(client):
  queues = client.queues.list()
  assert(queues[0].sid == '2fd1bc9b-2e1f-41ac-988f-06842700c10d')

@vcr.use_cassette()
def test_queue_members(client):
  members = client.queues('2fd1bc9b-2e1f-41ac-988f-06842700c10d').members.list()
  assert(members[0].call_sid == '24c0f807-2663-4080-acef-c0874f45274d')