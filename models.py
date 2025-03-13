from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey,Table
from sqlalchemy.orm import relationship


Base=declarative_base()


#creating an association table
employee_project = Table(
    'employee_project', Base.metadata,
    Column('employee_id', Integer, ForeignKey('employees.id')),
    Column('project_id', Integer, ForeignKey('projects.id'))
)


#Creating the employee model
class Employee(Base):
    __tablename__="employees"
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    email=Column(String,nullable=False)
    job_title=Column(String,nullable=False)
    age=Column(Integer,nullable=False)

    #Adding a foreign key
    project_id=Column(Integer,ForeignKey('projects.id'))
    department_id=Column(Integer,ForeignKey('departments.id'))

    #one-to-many relationship
    department = relationship("Department", backref="employees")

      # Many-to-Many relationship with Project
    projects = relationship("Project", secondary=employee_project, back_populates="employees")
    
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

    # Many-to-Many relationship with Employee
    employees = relationship("Employee", secondary=employee_project, back_populates="projects") 


 