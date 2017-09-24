"""empty message

Revision ID: 14c5d087aba4
Revises: 3bd8376bee61
Create Date: 2015-08-23 17:22:15.787130

"""

# revision identifiers, used by Alembic.
revision = '14c5d087aba4'
down_revision = '3bd8376bee61'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('entry'):
        op.add_column('entry', sa.Column('author_id', sa.Integer(), nullable=True))
        op.create_foreign_key(None, 'entry', 'user', ['author_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'entry', type_='foreignkey')
    op.drop_column('entry', 'author_id')
    ### end Alembic commands ###