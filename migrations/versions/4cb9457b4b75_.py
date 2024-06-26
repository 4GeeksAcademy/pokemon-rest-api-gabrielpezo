"""empty message

Revision ID: 4cb9457b4b75
Revises: 85d75a56432a
Create Date: 2024-04-19 04:09:03.709878

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cb9457b4b75'
down_revision = '85d75a56432a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokemon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('type', sa.String(length=10), nullable=False),
    sa.Column('second_type', sa.String(length=10), nullable=True),
    sa.Column('height', sa.String(length=10), nullable=False),
    sa.Column('weight', sa.String(length=10), nullable=False),
    sa.Column('primary_ability', sa.String(length=10), nullable=False),
    sa.Column('secondary_ability', sa.String(length=10), nullable=True),
    sa.Column('hidden_ability', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pokemon')
    # ### end Alembic commands ###
