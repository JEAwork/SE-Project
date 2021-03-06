"""add phone number

Revision ID: 88843e976855
Revises: 5771687195c4
Create Date: 2022-06-08 01:46:34.797309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88843e976855'
down_revision = '5771687195c4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
