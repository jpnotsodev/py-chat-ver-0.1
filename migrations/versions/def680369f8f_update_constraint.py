"""Update Constraint

Revision ID: def680369f8f
Revises: 079e5e1cb2a7
Create Date: 2022-03-19 21:43:47.675486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'def680369f8f'
down_revision = '079e5e1cb2a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('history', 'username',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('history', 'username',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    # ### end Alembic commands ###