"""add column description

Revision ID: cd4d2372890d
Revises: 48233f779313
Create Date: 2020-11-25 08:27:24.502137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd4d2372890d'
down_revision = '48233f779313'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'description')
    # ### end Alembic commands ###
