"""Confirmed field for user

Revision ID: 7797c99238da
Revises: e00a5c096f0d
Create Date: 2019-09-09 20:45:45.300508

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7797c99238da'
down_revision = 'e00a5c096f0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###