"""add search_query column to news table

Revision ID: afa58b7a4d12
Revises: 
Create Date: 2023-11-03 14:16:55.046489

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'afa58b7a4d12'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("news", sa.Column("search_query", sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column("news", "search_query")
