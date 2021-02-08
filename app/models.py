import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Home(Base):
    __tablename__ = "home"
    id = sa.Column(sa.Integer, primary_key=True)
    floors = sa.Column(sa.Integer, default=1)
    address = sa.Column(sa.String)
