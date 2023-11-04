"""drop published_date column

Revision ID: 581b3da6595d
Revises: 
Create Date: 2023-11-05 01:09:08.597952

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '581b3da6595d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column("news", "published_date")


def downgrade() -> None:
    op.add_column("news", sa.Column("published_date", sa.Date(), nullable=True))
