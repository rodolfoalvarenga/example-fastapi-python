"""add content column to posts table

Revision ID: 3398e5e22296
Revises: 790656bb199f
Create Date: 2023-06-30 16:26:35.112070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3398e5e22296'
down_revision = '790656bb199f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
