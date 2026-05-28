"""
Extends Value with an audio column.
"""
from zope.interface import implementer
import sqlalchemy as sa
import sqlalchemy.orm  # noqa: F401  # pylint: disable=W0611

from clld.db.meta import CustomModelMixin
from clld.db.models.common import Value
from clld.interfaces import IValue

__all__ = ['Counterpart']


@implementer(IValue)
class Counterpart(CustomModelMixin, Value):
    """The audio column will should hold the URL to the audio file."""
    pk = sa.Column(sa.Integer, sa.ForeignKey('value.pk'), primary_key=True)
    audio = sa.Column(sa.Unicode)
