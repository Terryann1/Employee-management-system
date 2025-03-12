import click
from sqlalchemy.orm import sessionmaker
from models import Employee,Department,Project

from sqlalchemy import create_engine


engine= create_engine("sqlite:///employees.db")

Session=sessionmaker(bind=engine)

@click.group()
def cli():
     """
     Employee management System 

    """
     pass

#command to add a new employee
@cli.command()
@click.option('--name',prompt='Employee Name')
@click.option('--age',prompt='Employee Age',type=int)
@click.option('--email',prompt='Employee Email')
@click.option('--job_title',prompt='Employee job_title')
@click.option('--project_id',prompt='Project iD',type=int)
@click.option('--department_id',prompt='Department ID',type=int)

def add_employee(name,age,email,job_title,project_id,department_id):
    session=Session()
    employee=Employee(name=name, age=age,email=email,job_title=job_title,project_id=project_id,department_id=department_id)
    session.add(employee)
    session.commit()
    click.echo(f"Added employee: {employee.name}")
    session.close()

# #command to add a new project
@cli.command()
@click.option('--name',prompt='Project name')

def add_project(name):
    session=Session()
    project=Project(name=name)
    session.add(project)
    session.commit()
    click.echo("Project added")
    session.close() 

#command to add a new department
@cli.command()
@click.option('--name',prompt='Department name')
def add_department(name):
    session=Session()
    department=Department(name=name)
    session.add(department)
    session.commit()
    click.echo("Department added") 


 #Command for generating a list of employees 
@cli.command()
def list_employees():
    session=Session()

    #Fetch from the database
    employees=session.query(Employee).all()

    #creating a list of employees
    if not employees:
        click.echo("No employees found")
    click.echo("List of all employees:")
    click.echo("{:<20} {:<5} {:<20} {:<25} {:<10}".format("Name", "Age", "Job Title", "Project ID", "Department ID"))
    click.echo("-" * 85)
    for e in employees:
         click.echo("{:<20} {:<5} {:<20} {:<25} {:<10}".format(e.name,e.age,e.email,e.job_title,e.project_id,e.department_id
           
        ))
    session.close()
         

#command for deleting an employeee
@cli.command()
@click.option('--id',prompt='Enter employee ID',type=int)
def delete_employee(id):
    session=Session()

     # Fetch the employee by ID
    delete_employee = session.query(Employee).filter(Employee.id == id).first()
    
    if delete_employee:
        session.delete(delete_employee)
        session.commit()
        click.echo(f"Employee with ID {id} has been deleted")

    else:
        click.echo(f"Employee with ID {id} does not exist")
        session.close() 

#command for updating an employee's details
@cli.command()
@click.option('--id',prompt='Enter ID',type=int)
@click.option('--new_email',prompt='Enter new email',type=str)
def update_employee(id,new_email):
    session=Session()

    #fetch from the database
    employee=session.query(Employee).filter(Employee.id==id).first()
    if employee:

        #setting the new email
        employee.email=new_email
        session.commit()
        click.echo(f"Employee with ID {id} email has been updated to {new_email}.")
    else:
        click.echo(f"Employee with ID {id} does not exist.")
        session.close()

#find an object by attribute
@cli.command()
@click.option('--id',prompt='Enter Employee ID',type=int)
def find_by_attribute(id):
    session=Session()
    employee_attribute=session.query(Employee).filter(Employee.id == id).first()
    session.commit()
    if employee_attribute:
        click.echo(f"Employee with ID {id} has attributes:{employee_attribute.name} | {employee_attribute.email} | {employee_attribute.job_title} | {employee_attribute.project_id} | {employee_attribute.department_id}")
    else:
        click.echo("Employee not found")    
    session.close()

   

    





         
    
           




if __name__=='__main__':
    cli()



