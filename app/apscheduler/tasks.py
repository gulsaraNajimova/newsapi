from app.models.news_model import NewsModel
from app.core.containers import Container

db = Container.db()

def delete_news_nextday():
    with db.session() as session:
        session.query(NewsModel).delete()
        session.commit()
