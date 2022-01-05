"""create-owner-model

Revision ID: dc0f6dfbcc3f
Revises: c899f605fb80
Create Date: 2022-01-05 11:26:46.925883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc0f6dfbcc3f'
down_revision = 'c899f605fb80'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'owners',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('age', sa.Integer)
    )


def downgrade():
    op.drop_table('owners')
