"""comment on job

Revision ID: ff7188c160ad
Revises: 47c8c94b3c65
Create Date: 2018-09-30 13:55:53.584836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff7188c160ad'
down_revision = '47c8c94b3c65'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('job_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'job', ['job_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'job_id')
    # ### end Alembic commands ###