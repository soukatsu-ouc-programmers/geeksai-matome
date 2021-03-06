import os
import psycopg2
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

data_list = ['abe', 'kaito', 'haruka']

# conn = psycopg2.connect(DATABASE_URL, sslmode='require')

DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)

# test = table('test',
#             column('id'),
#             column('name'))
# test = Table(
#     'test',
#     MetaData(),
#     Column('id', INTEGER, primary_key=True),
#     Column('name', TEXT, nullable=False),
# )
Base = declarative_base()
# class Actor(Base):
#     __tablename__ = 'actor'
#     actor_id = Column(Integer, primary_key=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     last_update = Column(DateTime)
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'
class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    name = Column(String)


SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# Base.metadata.create_all(engine)

# actor = Actor()
# actor.first_name = 'yuma'
# actor.last_name = 'kasahara'

# sample = Test(name='sasaki')
session.bulk_save_objects(
    [Test(name=d) for d in data_list], return_defaults=True
)

# session.add(actor)
# session.add(sample)
# query = session.query(Actor)
# query = session.query(Test)

session.commit()
# my_actor = query.first()
# print(my_actor.name)

# q = 'select * from test'
# q = 'insert into test (name) values (\'yuma2\');'
# q = select([column('name')], from_obj=table('test'))
# q = select([test.c.id, test.c.name])
# q = select([test.c.name], whereclause=(test.c.id<2))
# q = test.select(test.c.id<3)
# q = test.select().where(test.c.id<3)
# q = test.select(test.c.id<3).order_by(test.c.name)
# print(str(q))
# print(str(test.c.id==1))

# res = engine.execute(q)
# print(res.rowcount)
# print(list(res))


# db_session = scoped_session(
#     sessionmarker(
#         autocommit=False,
#         autoflush = False,
#         bind = engine
#     )
# )

# # # モデル作成
# # class Test(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     name = db.Column(db.Text)

# #     def __init__(self, name):
# #         self.name = name
    
# #     def __repr__(self):
# #         return self.name

# test_table = table('test')

# stmt = (
#     insert()
# )
