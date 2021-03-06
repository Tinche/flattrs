from hypothesis import given
from hypothesis.strategies import composite
from hypothesis.strategies._internal.core import booleans

from flattr import model_from_bytes, model_to_bytes

from .models_tableswithtables import ContainsTable, OptionalTable
from .test_common import common1s


@composite
def contains_tables(draw):
    return ContainsTable(draw(common1s()))


@composite
def optional_tables(draw):
    return OptionalTable(draw(common1s()) if draw(booleans()) else None)


@given(contains_tables())
def test_contains_tables(inst):
    assert inst == model_from_bytes(inst.__class__, model_to_bytes(inst))


@given(optional_tables())
def test_optional_tables(inst):
    assert inst == model_from_bytes(inst.__class__, model_to_bytes(inst))
