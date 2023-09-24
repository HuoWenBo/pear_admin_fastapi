from typing import List

from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from pear_admin_fastapi.db.base import Base
from pear_admin_fastapi.db.base import CUDTimeMixin
from pear_admin_fastapi.db.base import CreateTimeMixin, UpdateTimeMixin, EnabledColumnMixin
from pear_admin_fastapi.db.base import IntegerIDMixin

role_permission = Table(
    'role_permission',
    Base.metadata,
    Column('role_id', ForeignKey('role.id'), primary_key=True),
    Column('permission_id', ForeignKey('permission.id'), primary_key=True),
)
user_role = Table(
    'user_role',
    Base.metadata,
    Column('user_id', ForeignKey('user.id'), primary_key=True),
    Column('role_id', ForeignKey('role.id'), primary_key=True),
)


class Permission(IntegerIDMixin, CreateTimeMixin, UpdateTimeMixin, EnabledColumnMixin):
    __tablename__ = 'permission'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name: Mapped[str] = mapped_column(String(32), unique=True, index=True, nullable=False)
    type: Mapped[str] = mapped_column(String(32), nullable=False)
    url: Mapped[str] = mapped_column(String(255), nullable=False)
    icon: Mapped[str] = mapped_column(String(128))

    roles: Mapped[List['Role']] = relationship(
        'Role',
        secondary=role_permission,
        back_populates='permissions'
    )


class Role(IntegerIDMixin, CreateTimeMixin, UpdateTimeMixin, EnabledColumnMixin):
    __tablename__ = 'role'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name: Mapped[str] = mapped_column(String(32), unique=True, index=True, nullable=False)
    icon: Mapped[str] = mapped_column(String(255))

    permissions: Mapped[List[Permission]] = relationship(
        Permission,
        secondary=role_permission,
        back_populates='roles'
    )
    users: Mapped[List['User']] = relationship('User', secondary=user_role, back_populates='roles')


class User(CUDTimeMixin, EnabledColumnMixin):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(32), unique=True, index=True, nullable=False)
    password: Mapped[str] = mapped_column(String(128))
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=True)
    avatar: Mapped[str] = mapped_column(String(320), default="/static/system/admin/images/avatar.jpg")

    roles: Mapped[List[Role]] = relationship(Role, secondary=user_role, back_populates='users')
