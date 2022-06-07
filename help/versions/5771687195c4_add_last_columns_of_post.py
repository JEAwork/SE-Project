"""add last columns of post

Revision ID: 5771687195c4
Revises: 538100ab720b
Create Date: 2022-06-08 01:08:24.717512

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5771687195c4'
down_revision = '538100ab720b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text
        ('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
