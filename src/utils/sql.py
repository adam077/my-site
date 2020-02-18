from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.setting import db_conn

# 创建对象的基类:
Base = declarative_base()


class User(Base):
    __tablename__ = 'u_test'

    id = Column('id', Integer, primary_key=True)
    name = Column(String(20))


engine = create_engine(db_conn, echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()
# session.add(User(id='5', name='Bob'))
# session.commit()

# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id == '1').one()
print('type:', type(user))
print('name:', user.name)
all = session.query(User).filter(User.name == 'sun').all()
print(len(all))
for i in all:
    print('i:', i.name)
# 关闭Session:
session.close()

'''
最基础的东西
https://www.liaoxuefeng.com/wiki/1016959663602400/1017803857459008
连接池
https://www.cnblogs.com/lianggege123/articles/9210147.html

CREATE TABLE "public"."u_test" (
"id" BIGINT PRIMARY KEY,
"name" varchar(20) COLLATE "default"
)

INSERT INTO "public"."u_test" ("id", "name") VALUES ('1', 'zhao');
INSERT INTO "public"."u_test" ("id", "name") VALUES ('2', 'qian');
INSERT INTO "public"."u_test" ("id", "name") VALUES ('3', 'sun');
INSERT INTO "public"."u_test" ("id", "name") VALUES ('4', 'sun');

'''
