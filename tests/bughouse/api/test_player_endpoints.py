import pytest

from django.core.urlresolvers import reverse

from rest_framework.test import APIClient

from bughouse.models import Player


@pytest.mark.django_db
def test_player_creation():
    client = APIClient()
    url = reverse('v1:player-list')
    response = client.post(url, {'name': 'jeff'}, format='json')

    # Should fail without an image
    assert Player.objects.filter(name='jeff').count() == 0

@pytest.mark.django_db
def test_player_name_update(factories):
    player = factories.PlayerFactory()
    original_name = player.name

    client = APIClient()
    url = reverse('v1:player-detail', kwargs={'pk': player.id})
    client.put(url, {'name': 'jeff'}, format='json')

    updated_player = Player.objects.get(id=player.id)
    assert updated_player.name == 'jeff'
    assert Player.objects.filter(name=original_name).count() == 0
