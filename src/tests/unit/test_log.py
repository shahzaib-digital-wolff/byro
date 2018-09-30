import pytest

from byro.common.models import LogEntry


@pytest.mark.django_db
def test_log_create(member):
    a = LogEntry.objects.create(content_object=member, action_type="test.test_log_create", data={'source': 'test'})

    assert a
    assert a.pk
    assert LogEntry.objects.get(pk=a.pk)
    assert LogEntry.objects.filter(action_type="test.test_log_create").count() == 1


@pytest.mark.django_db
def test_log_filter_content_object(member):
    LogEntry.objects.create(content_object=member, action_type="test.test_log_filter_content_object", data={'source': 'test'})

    assert LogEntry.objects.filter(content_object=member, action_type="test.test_log_filter_content_object").count() == 1


@pytest.mark.django_db
def test_log_immutable(member):
    LogEntry.objects.create(content_object=member, action_type="test.test_log_immutable", data={'source': 'test'})

    a = LogEntry.objects.get(action_type="test.test_log_immutable")

    with pytest.raises(Exception):
        a.action_type = "Fnord"
        a.save()

    with pytest.raises(Exception):
        a.delete()


@pytest.mark.django_db
def test_log_user(user, member):
    a = LogEntry.objects.create(user=user, content_object=member, action_type="test.test_log_user")

    assert a in LogEntry.objects.filter(user=user)

    with pytest.raises(Exception):
        LogEntry.objects.create(content_object=member, action_type="test.test_log_user")

    assert LogEntry.objects.filter(user=user).first().data['source'] == str(user)