"""Update tags

Revision ID: 185d87f7f96a
Revises: 9bd767baeae9
Create Date: 2022-11-19 22:56:14.643699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '185d87f7f96a'
down_revision = '9bd767baeae9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('association_table',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('association_table')
    op.drop_table('tags')
    # ### end Alembic commands ###