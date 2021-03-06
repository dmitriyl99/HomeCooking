"""total amount for orders

Revision ID: cf5a5241d8f1
Revises: ee5483392dca
Create Date: 2019-06-27 04:00:13.029122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf5a5241d8f1'
down_revision = 'ee5483392dca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('total_amount', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'total_amount')
    # ### end Alembic commands ###
