import pytest


@pytest.mark.django_db
def test_profiles(member):
    from byro.plugins.profile.models import MemberProfile

    profiles = member.profiles

    assert len(profiles) == 1
    assert isinstance(profiles[0], MemberProfile)
