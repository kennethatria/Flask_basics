"""empty message

Revision ID: 5169d29e9b70
Revises: 40600e641cea
Create Date: 2019-03-18 22:41:23.359472

"""

# revision identifiers, used by Alembic.
revision = '5169d29e9b70'
down_revision = '40600e641cea'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('incident', sa.Column('user_id', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('incident', 'user_id')
    # ### end Alembic commands ###