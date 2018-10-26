"""comment on application

Revision ID: 47c8c94b3c65
Revises: 0712b1c17814
Create Date: 2018-09-30 13:48:38.216474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47c8c94b3c65'
down_revision = '0712b1c17814'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('application_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'application', ['application_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'application_id')
    # ### end Alembic commands ###