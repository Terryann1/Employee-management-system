import click
from sqlalchemy.orm import sessionmaker
from models import Employee,Department,Project
from sqlalchemy import create_engine


engine= create_engine("sqlite:///employees.db")

Session=sessionmaker(bind=engine)

@click.group()
def cli():
     """
    CLI  for the Employee management System 

    """
     pass

#command to add a new employee
@cli.command()
@click.option('--name',prompt='Employee Name')
@click.option('--age',prompt='Employee Age',type=int)
@click.option('--email',prompt='Employee Email')
@click.option('--age',prompt='Employee job_title')

def add_employee(name,age,email,job_title):
    session=Session()
    employee=Employee(name=name, age=age,email=email,job_title=job_title)
    session.add(employee)
    session.commit()
    click.echo(f"Added student: {employee.name}")
    session.close()
     



if __name__=='__main__':
    cli()



