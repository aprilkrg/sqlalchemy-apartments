"""create-table

Revision ID: e0a68d2e4b90
Revises: b10d7e4fceaa
Create Date: 2022-01-04 15:48:33.194804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0a68d2e4b90'
down_revision = 'b10d7e4fceaa'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'dinos',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False, unique=True),
        sa.Column('type', sa.String)
    )


def downgrade():
    pass
