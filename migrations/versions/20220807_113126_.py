"""empty message

Revision ID: 99687f23bfec
Revises: 9e36073db387
Create Date: 2022-08-07 11:31:26.214931

"""
from alembic import op
import sqlalchemy as sa

import os

environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")


# revision identifiers, used by Alembic.
revision = "99687f23bfec"
down_revision = "9e36073db387"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users", "street", existing_type=sa.VARCHAR(length=200), nullable=True
    )
    op.alter_column("users", "city", existing_type=sa.VARCHAR(length=50), nullable=True)
    op.alter_column(
        "users", "state", existing_type=sa.VARCHAR(length=50), nullable=True
    )
    op.alter_column("users", "zip_code", existing_type=sa.INTEGER(), nullable=True)
    op.alter_column(
        "users", "country", existing_type=sa.VARCHAR(length=50), nullable=True
    )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users", "country", existing_type=sa.VARCHAR(length=50), nullable=False
    )
    op.alter_column("users", "zip_code", existing_type=sa.INTEGER(), nullable=False)
    op.alter_column(
        "users", "state", existing_type=sa.VARCHAR(length=50), nullable=False
    )
    op.alter_column(
        "users", "city", existing_type=sa.VARCHAR(length=50), nullable=False
    )
    op.alter_column(
        "users", "street", existing_type=sa.VARCHAR(length=200), nullable=False
    )
    # ### end Alembic commands ###
