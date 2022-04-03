from db import Base
from sqlalchemy.dialects.mysql import BOOLEAN, DATETIME, INTEGER, VARCHAR
from sqlalchemy.schema import Column


class Example(Base):
    __tablename__ = "example"

    id = Column(INTEGER, primary_key=True)
    example_string = Column(VARCHAR)
    example_number = Column(INTEGER)
    example_datetime = Column(DATETIME)
    example_boolean = Column(BOOLEAN)
