from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

Base = declarative_base()
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


class CarModel(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True)
    title = Column(String)
    price_usd = Column(Float)
    odometer = Column(Integer)
    username = Column(String)
    image_url = Column(String)
    image_count = Column(Integer)
    car_number = Column(String)
    car_vin = Column(String)
    datetime_found = Column(DateTime)


def init_db():
    Base.metadata.create_all(engine)
