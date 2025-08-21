from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    Float,
    Integer,
    String,
    Text,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# Replace 'sqlite:///rfg.db' with your path to database
engine = create_engine("sqlite:///rfg.db", convert_unicode=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    email = Column(Text)
    username = Column(String(255))


class Thing(Base):
    __tablename__ = "thing"
    id = Column(Integer, primary_key=True)
    text = Column(Text)
    string = Column(String(255))
    boolean = Column(Boolean)
    date = Column(Date)
    datetime = Column(DateTime)
    floaty = Column(Float)
    integer = Column(Integer)

    # not supported by sqlite
    # myenum = Column(Enum(MyEnum))
    # arrayString = Column(ARRAY(String))


Base.metadata.create_all(engine)

# end
