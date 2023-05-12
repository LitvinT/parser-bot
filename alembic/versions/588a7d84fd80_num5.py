"""num5

Revision ID: 588a7d84fd80
Revises: 4321647eae0f
Create Date: 2023-05-12 12:53:15.997008

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '588a7d84fd80'
down_revision = '4321647eae0f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admin', sa.Column('name', sa.VARCHAR(length=32), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('admin', 'name')
    # ### end Alembic commands ###
