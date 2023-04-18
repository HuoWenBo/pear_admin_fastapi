Alembic使用SQLAlchemy作为底层引擎，为关系数据库提供了变更管理脚本的创建、管理和调用。

### 迁移环境

Alembic的使用始于迁移环境的创建。这是特定于特定应用程序的脚本目录。迁移环境只创建一次，然后与应用程序的源代码本身沿着维护。环境是使用Alembic的
init 命令创建的，然后可以根据应用程序的特定需求进行定制。
此环境的结构（包括一些生成的迁移脚本）如下所示：

```
yourproject/    -这是应用程序源代码的根目录，或其中的某个目录。
    alembic/    -此目录位于应用程序的源代码树中，是迁移环境的主目录。它可以被命名为任何名称，并且使用多个数据库的项目甚至可能具有多个数据库。
        env.py  -这是一个Python脚本，每当调用alembic迁移工具时都会运行。至少，它包含配置和生成SQLAlchemy引擎的指令，从该引擎获取连接和事务，然后调用迁移引擎，使用连接作为数据库连接的源。
                脚本是生成的环境的一部分，因此迁移的运行方式完全可以自定义。如何连接的具体细节以及如何调用迁移环境的具体细节都在这里。可以修改脚本，以便可以操作多个引擎，可以将自定义参数传递到迁移环境中，可以加载特定于应用程序的库和模型并使其可用。
           
        README  -包含在各种环境模板中，应该有一些信息。
        script.py.mako -这是一个Mako模板文件，用于生成新的迁移脚本。这里的任何内容都用于在 versions/
                        中生成新文件。这是可编写脚本的，因此可以控制每个迁移文件的结构，包括每个文件中的标准导入，以及对 upgrade() 和 downgrade()
                        函数结构的更改。例如， multidb 环境允许使用命名方案 upgrade_engine1() 、 upgrade_engine2() 生成多个函数。

        versions/  -此目录包含各个版本的脚本。其他迁移工具的用户可能会注意到，这里的文件不使用升序整数，而是使用部分GUID方法。在Alembic中，版本脚本的顺序是相对于脚本本身中的指令的，并且理论上可以在其他版本文件之间“拼接”版本文件，允许合并来自不同分支的迁移序列，尽管需要小心手动。
            3512b954651e_add_account.py
            2b1ae634e5cd_add_order_id.py
            3adcc9a56557_rename_username_field.py
```
创建alembic环境：使用alembic命令创建alembic环境：

```
alembic init alembic
```

生成初始版本：使用alembic命令生成初始版本：

```
alembic revision -m "init"
```
编写迁移脚本：在alembic/versions目录下创建一个迁移脚本，例如：

```python
# alembic/versions/xxxxxx_create_user_table.py
from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=50), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('user')
```
执行迁移命令：使用alembic命令执行迁移：
```
alembic upgrade head
```