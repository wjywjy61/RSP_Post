"""empty message

Revision ID: 47d3222502d1
Revises: 32adf143c932
Create Date: 2020-03-18 19:41:34.884808

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47d3222502d1'
down_revision = '32adf143c932'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('likes', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'likes')
    # ### end Alembic commands ###