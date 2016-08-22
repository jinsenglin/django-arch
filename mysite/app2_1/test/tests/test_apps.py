from app2_1 import apps


def test_config_menu():
    assert hasattr(apps.App21Config, 'menu')
    assert 'dashboard' in apps.App21Config.menu
    assert 'panel' in apps.App21Config.menu
    assert 'name' in apps.App21Config.menu
    assert 'order' in apps.App21Config.menu
    assert 'path' in apps.App21Config.menu
    assert 'scope' in apps.App21Config.menu
