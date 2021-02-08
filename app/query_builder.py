from sqlalchemy.orm.query import Query
from app.models import Home

class HomeQueryBuilder(Query):
    def get_x(self, *args):
        return self.count()

def get_query_builder(entities, *args, **kwargs):
    dispatch = {
        Home: HomeQueryBuilder
    }
    return dispatch.get(entities[0], Query)(entities, *args, **kwargs)