from zope.interface import implementer
import sqlalchemy as sa
import sqlalchemy.orm  # noqa: F401

from clld.db.meta import CustomModelMixin
from clld.db.models.common import Value
from clld.interfaces import IValue

__all__ = ['Counterpart']


@implementer(IValue)
class Counterpart(CustomModelMixin, Value):
    pk = sa.Column(sa.Integer, sa.ForeignKey('value.pk'), primary_key=True)
    audio = sa.Column(sa.Unicode)
