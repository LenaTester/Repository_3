import pytest

from restapi_lesson.user_data_class import User
from restapi_lesson.color_class import Color


@pytest.fixture
def create_user():
    return User("lindsay.ferguson@reqres.in", "Lindsay", "Ferguson")


@pytest.fixture
def create_color():
    return Color(2, "fuchsia rose", 2001, "#C74375", "17-2031")
