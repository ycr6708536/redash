"""encyrpted_options

Revision ID: 93e68dcacb09
Revises: 71477dadd6ef
Create Date: 2018-10-16 11:32:38.320962

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '93e68dcacb09'
down_revision = '71477dadd6ef'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('data_sources', 'encrypted_options',
               existing_type=postgresql.BYTEA(),
               nullable=True)
    
    # TODO: implement copying of current options to new encyrpted field


def downgrade():
    op.alter_column('data_sources', 'encrypted_options',
               existing_type=postgresql.BYTEA(),
               nullable=True)
