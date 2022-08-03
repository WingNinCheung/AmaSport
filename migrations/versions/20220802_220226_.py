"""empty message

Revision ID: 5733640e2861
Revises: 7d40cc6be97f
Create Date: 2022-08-02 22:02:26.687362

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5733640e2861"
down_revision = "7d40cc6be97f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "products",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=500), nullable=False),
        sa.Column("price", sa.Float(), nullable=False),
        sa.Column("category", sa.String(length=50), nullable=False),
        sa.Column("brand", sa.String(length=50), nullable=False),
        sa.Column("about", sa.String(length=1000), nullable=False),
        sa.Column("description", sa.String(length=1000), nullable=False),
        sa.Column("dimensions", sa.String(length=100), nullable=False),
        sa.Column("date_available", sa.String(length=100), nullable=False),
        sa.Column("manufacturer", sa.String(length=1000), nullable=False),
        sa.Column("asin", sa.String(length=100), nullable=False),
        sa.Column("image", sa.String(length=1000), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("products")
    # ### end Alembic commands ###
