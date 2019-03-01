import os
import pytest
import haip.config as config
import haip.template as template

basedir = os.path.dirname(__file__)

@pytest.fixture
def setup():
    config.load(basedir + os.sep + 'etc')

@pytest.mark.asyncio
async def test_config_not_found():
    with pytest.raises(config.HaipConfigException):
        await template.render('me.txt', firstname='Reinhard', lastname='Hainz')

@pytest.mark.asyncio
async def test_simple_ok(setup):
    output = await template.render('me.txt', firstname='Reinhard', lastname='Hainz')
    assert 'Reinhard' in output

@pytest.mark.asyncio
async def test_json(setup):
    output = await template.render('me.json', firstname='Reinhard', lastname='Hainz')
    assert output['firstname'] == 'Reinhard'

@pytest.mark.asyncio
async def test_sql(setup):
    output = await template.render('me.sql', lastname="Hainz'")
    assert "Hainz\\'" in output
