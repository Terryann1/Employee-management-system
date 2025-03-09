"""created initial tables

Revision ID: b179ae37f07f
Revises: 
Create Date: 2025-03-09 15:03:28.306248

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b179ae37f07f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('employees',
    sa.Column('id',sa.Integer(),nullable=False),
    sa.Column('name',sa.String(),nullable=False),
    sa.Column('email',sa.String(),nullable=False),
    sa.Column('age',sa.Integer(),nullable=False),
    sa.Column('job_title',sa.String(),nullable=False)
    
    )

    op.create_table('departments',
    sa.Column('id',sa.Integer(),nullable=False),
    sa.Column('name',sa.String(),nullable=False)
    
    )

    op.create_table('projects',
    sa.Column('id',sa.Integer(),nullable=False),
    sa.Column('name',sa.Integer(),nullable=False)
    
    )



def downgrade() -> None:
    op.drop_table('employees')
    op.drop_table('departments')
    op.drop_table('projects')
