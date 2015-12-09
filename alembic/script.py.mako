"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""

# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}

from alembic import op  # noqa
import sqlalchemy as sa  # noqa
from sqlalchemy.sql.expression import text  # noqa
from sqlalchemy.sql import functions as sqlf  # noqa
Identifier = sa.BigInteger

${imports if imports else ""}

def upgrade():
    ${upgrades if upgrades else "pass"}


def downgrade():
    ${downgrades if downgrades else "pass"}
