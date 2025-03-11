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

#command to andd a new department
@cli.command()
@click.option('--name',prompt='Department name')
def add_department(name):
    session=Session()
    department=Department(name=name)
    session.add(department)
    session.commit()
    click.echo("Department added")        



if __name__=='__main__':
    cli()



