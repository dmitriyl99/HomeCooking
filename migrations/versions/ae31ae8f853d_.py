"""empty message

Revision ID: ae31ae8f853d
Revises: 04debcbe38ff
Create Date: 2019-04-28 16:10:21.515537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae31ae8f853d'
down_revision = '04debcbe38ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('address', sa.String(length=100), nullable=True))
    op.add_column('orders', sa.Column('confirmed', sa.Boolean(), nullable=True))
    op.add_column('orders', sa.Column('payment_method', sa.String(length=50), nullable=True))
    op.add_column('orders', sa.Column('shipping_method', sa.String(length=50), nullable=True))
    op.drop_column('orders', 'type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('type', sa.INTEGER(), nullable=True))
    op.drop_column('orders', 'shipping_method')
    op.drop_column('orders', 'payment_method')
    op.drop_column('orders', 'confirmed')
    op.drop_column('orders', 'address')
    # ### end Alembic commands ###
