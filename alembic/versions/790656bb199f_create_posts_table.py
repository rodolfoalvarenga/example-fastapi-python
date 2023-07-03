"""create posts table

Revision ID: 790656bb199f
Revises: 
Create Date: 2023-06-30 15:48:24.063119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '790656bb199f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False)) 
    pass


def downgrade():
    op.drop_table('posts')
    pass
