"""Student database unit tests."""

# std lib
import sqlite3

# 3rd party
import pytest

# custom
# import backend.databases as databases
from backend import databases


@pytest.fixture
def db():
    yield databases.StudentProfiles()

class TestStudentProfilesDB():
    def test_student_profile_db_connection(self, db):
        assert isinstance(db, databases.StudentProfiles)
        assert isinstance(db.connection, sqlite3.Connection)
        assert isinstance(db.cursor, sqlite3.Cursor)

    def test_first_name_lookup(self, db):
        profile = db.first_name_lookup("alice")
        assert isinstance(profile, list)
        assert profile[0][0] == "alice"

    def test_first_name_lookup_returns_unique_record(self, db):
        profiles = db.first_name_lookup("alice")
        assert len(profiles) == 1
