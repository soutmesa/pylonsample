from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SampleManpowerList(Base):
    __tablename__ = "SampleManpowerList"
    __table_args__ = {'schema': 'test'}

    id = Column(Integer, primary_key=True, index=True)
    nric4Digit = Column(String(50))
    name = Column(String(50))
    manpowerId = Column(String(50), unique=True, index=True)
    designation = Column(String(50))
    project = Column(String(50))
    team = Column(String(50))
    supervisor = Column(String(50))
    joinDate = Column(Date)
    resignDate = Column(Date, nullable=True)
