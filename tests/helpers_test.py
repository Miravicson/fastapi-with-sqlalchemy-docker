from pytest import mark

from helpers.remove_nulls import remove_nulls


@mark.parametrize(
    "input, result",
    [
        ({"name": "vic", "age": None}, {"name": "vic"}),
        (
            {"foo": None, "bar": {"name": "Vic", "age": 24, "class": None}},
            {"bar": {"name": "Vic", "age": 24}},
        ),
    ],
)
def test_remove_nulls(input, result):
    assert remove_nulls(input) == result
