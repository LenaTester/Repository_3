import pytest

from pythonProject.Repository_3.restapi_lesson.class_object.user_data_class import User
from pythonProject.Repository_3.restapi_lesson.class_object.color_class import Color


@pytest.fixture
def create_user():
    return User("lindsay.ferguson@reqres.in", "Lindsay", "Ferguson")


@pytest.fixture
def create_color():
    return Color(2, "fuchsia rose", 2001, "#C74375", "17-2031")
