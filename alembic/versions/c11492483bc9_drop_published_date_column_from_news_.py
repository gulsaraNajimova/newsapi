"""drop published_date column from news table

Revision ID: c11492483bc9
Revises: afa58b7a4d12
Create Date: 2023-11-03 14:21:16.035832

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c11492483bc9'
down_revision: Union[str, None] = 'afa58b7a4d12'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column("news", "published_date")


def downgrade() -> None:
    op.add_column("news", sa.Column("published_date", sa.Date(), nullable=True))
