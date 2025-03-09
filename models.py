from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


Base=declarative_base()


#Creating the employee model
class Employee(Base):
    __tablename__="employees"
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    email=Column(String,nullable=False)
    job_title=Column(String,nullable=False)
    age=Column(Integer,nullable=False)

# creating the department model
class Department(Base):
    __tablename__="departments"
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False) 

#creating the project model
class Project(Base):
    __tablename__="projects"
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)   