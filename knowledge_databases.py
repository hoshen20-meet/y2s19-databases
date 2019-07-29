from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(topic, title, rating):
        new_article = Knowledge(topic = topic , title = title, rating = rating)
        session.add(new_article)
        session.commit()

def query_all_articles():
	new_article = session.query(Knowledge).all()
	return new_article

def query_article_by_topic(topic):
	new_article = session.query(Knowledge).filter_by(topic = topic).first()
                
	return new_article
                                
def delete_article_by_topic(topic):
	new_article = session.query(Knowledge).filter_by(topic = topic).delete()
	session.commit()

def delete_all_articles():
	new_article = session.query(Knowledge).delete()
	
	session.commit()


def edit_article_rating():
	new_article = session.query(Knowledge).filter_by(rating=rating).first()
	new_article.rating = input("whats the new rating?")
	session.commit()

