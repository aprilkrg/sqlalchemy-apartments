"""apt-model

Revision ID: c899f605fb80
Revises: 703378ecebb2
Create Date: 2022-01-05 11:11:43.376579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c899f605fb80'
down_revision = '703378ecebb2'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'apartments',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('units', sa.Integer),
        sa.Column('owner_id', sa.Integer, sa.ForeignKey('owners.id'))
    )


def downgrade():
    op.drop_table('apartments')
