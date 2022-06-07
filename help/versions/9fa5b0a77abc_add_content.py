"""add content

Revision ID: 9fa5b0a77abc
Revises: 9795feed3f3e
Create Date: 2022-06-08 00:50:08.209716

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fa5b0a77abc'
down_revision = '9795feed3f3e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
