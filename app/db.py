from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.query_builder import get_query_builder

# an Engine, which the Session will use for connection
# resources
some_engine = create_engine("sqlite:///database.db")

# create a configured "Session" class
Session = sessionmaker(bind=some_engine)

# create a Session
session = Session(query_cls=get_query_builder)
