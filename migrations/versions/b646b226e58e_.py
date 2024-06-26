"""empty message

Revision ID: b646b226e58e
Revises: 0926f31c3cf0
Create Date: 2024-04-22 19:28:08.566598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b646b226e58e'
down_revision = '0926f31c3cf0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favourites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.Column('pokemon_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['person_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['pokemon_id'], ['pokemon.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('region', schema=None) as batch_op:
        batch_op.add_column(sa.Column('initials_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'pokemon', ['initials_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('region', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('initials_id')

    op.drop_table('favourites')
    # ### end Alembic commands ###
