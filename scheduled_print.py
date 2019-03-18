from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, DateTime, ForeignKey, Numeric, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine = create_engine("mysql+pymysql://SupportQa:cbc726de6accda94ba7e56d2768d9d68@mysql.opsigo.id:7706/Qa_1_Db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class log_print_inv(Base):
    __tablename__='log_print_inv'
    InvNo = Column(String())
    PrintDate = datetime.utcnow()
    Status = 'printed'
    CreationDate = datetime.utcnow()


log = log_print_inv(InvNo = 'TK-01-2019-01-00001',
                    PrintDate = datetime.utcnow(),
                    Status = 'printed',
                    CreationDate = datetime.utcnow()
                    )

session.add(log)
session.commit()