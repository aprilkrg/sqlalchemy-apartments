"""try-apt-again

Revision ID: a6103fbd8b73
Revises: dc0f6dfbcc3f
Create Date: 2022-01-05 11:31:09.907283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6103fbd8b73'
down_revision = 'dc0f6dfbcc3f'
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
