from app.db import session
from app.models import Home

print(session.query(Home).all())