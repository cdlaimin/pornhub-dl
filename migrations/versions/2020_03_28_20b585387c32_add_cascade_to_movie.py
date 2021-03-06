"""Add cascade to movie

Revision ID: 20b585387c32
Revises: fb1a5a75318a
Create Date: 2020-03-28 11:44:26.859813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20b585387c32"
down_revision = "fb1a5a75318a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("movie_user_key_fkey", "movie", type_="foreignkey")
    op.create_foreign_key(
        "user", "movie", "user", ["user_key"], ["key"], ondelete="cascade"
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("user", "movie", type_="foreignkey")
    op.create_foreign_key("movie_user_key_fkey", "movie", "user", ["user_key"], ["key"])
    # ### end Alembic commands ###
