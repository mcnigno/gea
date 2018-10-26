"""comment on all others

Revision ID: 60b8954ac861
Revises: 1290ca6da86a
Create Date: 2018-09-30 14:00:08.612258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60b8954ac861'
down_revision = '1290ca6da86a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('cdrlitem_id', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('discipline_id', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('doctype_id', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('documentclass_id', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('domain_id', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('matrix_id', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('mr_id', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('partner_id', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('sheet', sa.String(length=3), nullable=True))
    op.add_column('comments', sa.Column('vendor_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'vendor', ['vendor_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'partner', ['partner_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'domain', ['domain_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'matrix', ['matrix_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'doctype', ['doctype_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'documentclass', ['documentclass_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'discipline', ['discipline_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'cdrlitem', ['cdrlitem_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'mr', ['mr_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'vendor_id')
    op.drop_column('comments', 'sheet')
    op.drop_column('comments', 'partner_id')
    op.drop_column('comments', 'mr_id')
    op.drop_column('comments', 'matrix_id')
    op.drop_column('comments', 'domain_id')
    op.drop_column('comments', 'documentclass_id')
    op.drop_column('comments', 'doctype_id')
    op.drop_column('comments', 'discipline_id')
    op.drop_column('comments', 'cdrlitem_id')
    # ### end Alembic commands ###