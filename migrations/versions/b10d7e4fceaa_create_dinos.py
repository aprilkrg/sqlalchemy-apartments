"""create-dinos

Revision ID: b10d7e4fceaa
Revises: 
Create Date: 2022-01-04 14:56:18.657886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b10d7e4fceaa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String, nullable=False, unique=True),
        sa.Column('password', sa.String, nullable=False)
    )


def downgrade():
    op.drop_table('users')
