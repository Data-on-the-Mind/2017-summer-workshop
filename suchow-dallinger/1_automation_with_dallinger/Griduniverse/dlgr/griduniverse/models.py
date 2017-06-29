from dallinger.models import Info
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import JSONB


class Event(Info):
    """An event."""

    __mapper_args__ = {
        "polymorphic_identity": "event"
    }

    details = Column(JSONB)

    def __init__(self, origin, details):
        super(Event, self).__init__(origin)
        self.details = details
