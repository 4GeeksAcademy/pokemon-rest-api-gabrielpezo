"""empty message

Revision ID: e7665ceb5d55
Revises: 4cb9457b4b75
Create Date: 2024-04-19 04:31:42.087459

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7665ceb5d55'
down_revision = '4cb9457b4b75'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pokemon', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('type',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('second_type',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=100),
               existing_nullable=True)
        batch_op.alter_column('height',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('weight',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('primary_ability',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.alter_column('secondary_ability',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=100),
               existing_nullable=True)
        batch_op.alter_column('hidden_ability',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(length=100),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pokemon', schema=None) as batch_op:
        batch_op.alter_column('hidden_ability',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=10),
               existing_nullable=True)
        batch_op.alter_column('secondary_ability',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=10),
               existing_nullable=True)
        batch_op.alter_column('primary_ability',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=10),
               existing_nullable=False)
        batch_op.alter_column('weight',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=10),
               existing_nullable=False)
        batch_op.alter_column('height',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=10),
               existing_nullable=False)
        batch_op.alter_column('second_type',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=10),
               existing_nullable=True)
        batch_op.alter_column('type',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=10),
               existing_nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=20),
               existing_nullable=False)

    # ### end Alembic commands ###
