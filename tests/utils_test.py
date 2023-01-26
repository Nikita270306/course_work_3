from utils import *
import pytest


def test_get_posts_all():
    assert type(get_posts_all()) == list
    assert type(get_posts_all()[0]) == dict


def test_get_posts_by_user():
    assert type(get_posts_by_user('leo')) == list
    assert type(get_posts_by_user('leo')[0]) == dict
    with pytest.raises(ValueError):
        get_posts_by_user('sdfsdf')


def test_get_comments_by_post_id():
    assert type(get_comments_by_post_id(1)) == list
    assert type(get_comments_by_post_id(1)[0]) == dict
    with pytest.raises(ValueError):
        get_comments_by_post_id(56)
    assert get_comments_by_post_id(8) == []


def test_search_for_posts():
    assert type(search_for_posts('к')) == list
    assert type(search_for_posts('к')[0]) == dict
