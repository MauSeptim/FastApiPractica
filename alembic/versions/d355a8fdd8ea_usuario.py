"""usuario

Revision ID: d355a8fdd8ea
Revises: 0bb62eddcbfe
Create Date: 2025-02-08 23:57:24.248754

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd355a8fdd8ea'
down_revision: Union[str, None] = '0bb62eddcbfe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('algo',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('password', sa.String(length=14), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_algo_id'), 'algo', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_algo_id'), table_name='algo')
    op.drop_table('algo')
    # ### end Alembic commands ###
