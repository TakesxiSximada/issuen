"""first

Revision ID: 376c06ffb4e
Revises:
Create Date: 2015-12-09 23:37:16.620550

"""

# revision identifiers, used by Alembic.
revision = '376c06ffb4e'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op  # noqa
import sqlalchemy as sa  # noqa
from sqlalchemy.sql.expression import text  # noqa
from sqlalchemy.sql import functions as sqlf  # noqa
Identifier = sa.BigInteger


def upgrade():
    op.create_table(
        'User',
        sa.Column('id', Identifier(), primary_key=True),
        sa.Column('email', sa.String(254), unique=True, server_default=''),
        sa.Column('password', sa.String(100), server_default=''),
    )


def downgrade():
    op.drop_table('User')
