"""create post table

Revision ID: 9795feed3f3e
Revises: baabc9f2a4ab
Create Date: 2022-06-08 00:41:01.495088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9795feed3f3e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa. Column ('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
