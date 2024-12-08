from email.policy import default
from sqlalchemy import Boolean, Column, Integer, String
from owndatabase import Base



class ContactList(Base):
    __tablename__ = "contactlist5"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False,)  # Non-nullable name
    phone = Column(Integer, nullable=False)  # Primary key and non-nullable phone number

    