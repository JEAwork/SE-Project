"""add user table

Revision ID: 2457fb0d670a
Revises: 9fa5b0a77abc
Create Date: 2022-06-08 00:55:09.184836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2457fb0d670a'
down_revision = '9fa5b0a77abc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), 
            server_default=sa.text('now()'),nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
