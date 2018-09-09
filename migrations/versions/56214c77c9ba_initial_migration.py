"""Initial Migration

Revision ID: 56214c77c9ba
Revises: 
Create Date: 2018-09-09 15:00:43.436948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56214c77c9ba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_categories_category_name'), 'categories', ['category_name'], unique=False)
    op.add_column('pitches', sa.Column('category_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pitches', 'categories', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.drop_column('pitches', 'category_id')
    op.drop_index(op.f('ix_categories_category_name'), table_name='categories')
    op.drop_table('categories')
    # ### end Alembic commands ###