"""add foreign key to post table

Revision ID: 538100ab720b
Revises: 2457fb0d670a
Create Date: 2022-06-08 01:03:15.373827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '538100ab720b'
down_revision = '2457fb0d670a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", 
    local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_colum('posts', 'owner_id')
    pass
