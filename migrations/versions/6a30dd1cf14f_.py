"""empty message

Revision ID: 6a30dd1cf14f
Revises: 7239979e940a
Create Date: 2025-02-21 21:25:05.656835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a30dd1cf14f'
down_revision = '7239979e940a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alunos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('aluno_id', sa.Integer(), nullable=False),
    sa.Column('turma_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['aluno_id'], ['usuario.id'], ),
    sa.ForeignKeyConstraint(['turma_id'], ['turma.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('alunos')
    # ### end Alembic commands ###
