"""empty message

Revision ID: 9e36073db387
Revises:
Create Date: 2022-08-03 13:20:55.995633

"""
from alembic import op
import sqlalchemy as sa
import os

environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")


# revision identifiers, used by Alembic.
revision = "9e36073db387"
down_revision = None
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

    if environment == "production":
        op.execute(f"ALTER TABLE products SET SCHEMA {SCHEMA};")
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=40), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("hashed_password", sa.String(length=255), nullable=False),
        sa.Column("street", sa.String(length=200), nullable=False),
        sa.Column("city", sa.String(length=50), nullable=False),
        sa.Column("state", sa.String(length=50), nullable=False),
        sa.Column("zip_code", sa.Integer(), nullable=False),
        sa.Column("country", sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("username"),
    )
    if environment == "production":
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")
    op.create_table(
        "cart_items",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("product_id", sa.Integer(), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["products.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    if environment == "production":
        op.execute(f"ALTER TABLE cart_items SET SCHEMA {SCHEMA};")
    op.create_table(
        "orders",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("product_id", sa.Integer(), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.Column("price", sa.Float(), nullable=False),
        sa.Column("street", sa.String(length=200), nullable=False),
        sa.Column("city", sa.String(length=50), nullable=False),
        sa.Column("state", sa.String(length=50), nullable=False),
        sa.Column("zip_code", sa.Integer(), nullable=False),
        sa.Column("country", sa.String(length=50), nullable=False),
        sa.Column("delivery_time", sa.Integer(), nullable=False),
        sa.Column("delivery_status", sa.String(length=30), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["products.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    if environment == "production":
        op.execute(f"ALTER TABLE orders SET SCHEMA {SCHEMA};")
    op.create_table(
        "reviews",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("product_id", sa.Integer(), nullable=False),
        sa.Column("rating", sa.Integer(), nullable=False),
        sa.Column("review_body", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["products.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    if environment == "production":
        op.execute(f"ALTER TABLE reviews SET SCHEMA {SCHEMA};")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("reviews")
    op.drop_table("orders")
    op.drop_table("cart_items")
    op.drop_table("users")
    op.drop_table("products")
    # ### end Alembic commands ###
