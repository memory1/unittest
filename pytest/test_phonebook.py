from phonebook import Phonebook
import pytest

@pytest.fixture
def phonebook(request):
    phonebook = Phonebook()
    def cleanup_phonebook():
        phonebook.clear()
    request.addfinalizer(cleanup_phonebook)
    return phonebook


def test_lookup_entry(phonebook):
    phonebook.add("Bob", "12345")
    assert "12345" == phonebook.lookup("Bob")
