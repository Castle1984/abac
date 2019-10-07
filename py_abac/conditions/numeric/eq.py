"""
    Numeric equal condition
"""

from marshmallow import post_load

from .base import NumericCondition, NumericConditionSchema, is_number


class Eq(NumericCondition):

    def is_satisfied(self, what):
        if not is_number(what):
            return False
        return what == self.value


class EqSchema(NumericConditionSchema):

    @post_load
    def post_load(self, data, **_):
        return Eq(**data)