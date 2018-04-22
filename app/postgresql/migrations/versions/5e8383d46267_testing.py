"""testing

Revision ID: 5e8383d46267
Revises: 7690e35e653b
Create Date: 2018-04-18 13:47:20.463480

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5e8383d46267'
down_revision = '7690e35e653b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('results', sa.Column('result_all', postgresql.JSON(astext_type=sa.Text()), nullable=True))
    op.add_column('results', sa.Column('result_no_stop_words', postgresql.JSON(astext_type=sa.Text()), nullable=True))
    op.drop_column('results', 'info')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('results', sa.Column('info', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('results', 'result_no_stop_words')
    op.drop_column('results', 'result_all')
    # ### end Alembic commands ###