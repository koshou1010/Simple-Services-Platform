"""fixed user_profile add basemodel

Revision ID: 91c022f2ad4f
Revises: 7f5fcfb66ef6
Create Date: 2023-06-09 11:36:27.338719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91c022f2ad4f'
down_revision = '7f5fcfb66ef6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # op.create_table('report_sleep_statistic',
    # sa.Column('valid_flag', sa.Boolean(), nullable=False),
    # sa.Column('create_user', sa.String(length=40), nullable=False),
    # sa.Column('create_datetime', sa.DateTime(), nullable=False),
    # sa.Column('update_user', sa.String(length=40), nullable=False),
    # sa.Column('update_datetime', sa.DateTime(), nullable=False),
    # sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    # sa.Column('report_id', sa.Integer(), nullable=False),
    # sa.Column('total_sleep_hrs', sa.Float(), nullable=False),
    # sa.Column('total_sleep_hrs_without_missing', sa.Float(), nullable=False),
    # sa.Column('missing_times', sa.Integer(), nullable=False),
    # sa.Column('awake_times', sa.Integer(), nullable=False),
    # sa.Column('rem_times', sa.Integer(), nullable=False),
    # sa.Column('light_times', sa.Integer(), nullable=False),
    # sa.Column('deep_times', sa.Integer(), nullable=False),
    # sa.Column('awake_per_with_awake', sa.Float(), nullable=False),
    # sa.Column('rem_per_with_awake', sa.Float(), nullable=False),
    # sa.Column('light_per_with_awake', sa.Float(), nullable=False),
    # sa.Column('deep_per_with_awake', sa.Float(), nullable=False),
    # sa.Column('rem_per_without_awake', sa.Float(), nullable=False),
    # sa.Column('light_per_without_awake', sa.Float(), nullable=False),
    # sa.Column('deep_per_without_awake', sa.Float(), nullable=False),
    # sa.ForeignKeyConstraint(['report_id'], ['report.record_id'], ),
    # sa.PrimaryKeyConstraint('id')
    # )
    
    # create default
    from sqlalchemy.orm import sessionmaker
    from model.user_profile import UserProfile   
    import datetime
    bind = op.get_bind()
    Session = sessionmaker(bind=bind)
    session = Session()

    
    op.add_column('user_profile', sa.Column('valid_flag', sa.Boolean(), nullable=True))
    op.add_column('user_profile', sa.Column('create_user', sa.String(length=40), nullable=True))
    op.add_column('user_profile', sa.Column('create_datetime', sa.DateTime(), nullable=True))
    op.add_column('user_profile', sa.Column('update_user', sa.String(length=40), nullable=True))
    op.add_column('user_profile', sa.Column('update_datetime', sa.DateTime(), nullable=True))
    
    session.query(UserProfile).update({'valid_flag' : True})
    session.query(UserProfile).update({'create_user' : 'server_migrate'})
    session.query(UserProfile).update({'create_datetime' : datetime.datetime.now()})
    session.query(UserProfile).update({'update_user' : 'server_migrate'})
    session.query(UserProfile).update({'update_datetime' : datetime.datetime.now()})

    op.alter_column('user_profile', 'valid_flag',nullable=False, existing_type=sa.Boolean())
    op.alter_column('user_profile', 'create_user',nullable=False, existing_type= sa.String(length=40))
    op.alter_column('user_profile', 'create_datetime',nullable=False, existing_type=sa.DateTime())
    op.alter_column('user_profile', 'update_user',nullable=False, existing_type=sa.String(length=40))
    op.alter_column('user_profile', 'update_datetime',nullable=False, existing_type=sa.DateTime())


    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    
    op.drop_column('user_profile', 'update_datetime')
    op.drop_column('user_profile', 'update_user')
    op.drop_column('user_profile', 'create_datetime')
    op.drop_column('user_profile', 'create_user')
    op.drop_column('user_profile', 'valid_flag')

    # op.drop_table('report_sleep_statistic')
    # ### end Alembic commands ###
