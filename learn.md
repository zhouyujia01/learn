## 一、获取代码

1.拉取代码

**地址**

```
http://icode.baidu.com/repos/baidu/bce-op/acloud/tree/master
```

**执行命令**

```
git clone https://zhouyujia01@icode.baidu.com/baidu/bce-op/acloud baidu/bce-op/acloud && curl -s http://icode.baidu.com/tools/hooks/commit-msg > baidu/bce-op/acloud/.git/hooks/commit-msg && chmod u+x baidu/bce-op/acloud/.git/hooks/commit-msg && git config -f baidu/bce-op/acloud/.git/config user.name zhouyujia01 && git config -f baidu/bce-op/acloud/.git/config user.email zhouyujia01@baidu.com
```

2.配置公钥 [已经配置，后续不需要再做配置]
```
1】设置本地ssh 密钥

执行：ssh-keygen -t rsa

生成的公钥地址：/Users/zhouyujia01/.ssh/

文件说明：
	id_rsa		私钥
	id_rsa.pub  公钥
	known_hosts	

2】粘贴 （id_rsa.pub  公钥）到 http://icode.baidu.com/account/keys ssh公钥
```


## 二、安装工具

```
1.安装 homebrew

参考地址：https://brew.sh/index_zh-cn.html
	

2.安装 mysql
有两种安装方式：
	a.通过下载安装
	b.通过 brew 命令行安装 [推荐]
参考地址：https://www.jianshu.com/p/fd3aae701db9
https://aaaaaashu.gitbooks.io/mac-dev-setup/content/MySql/index.html [推荐]


3.git的使用

http://rogerdudler.github.io/git-guide/index.zh.html


4.redis

mac 下安装也可以使用 homebrew，homebrew 是 mac 的包管理器。
1、安装redis: 
    brew install redis
2、启动 redis：
    可以使用后台服务启动【推荐】： brew services start redis
    或者直接启动：redis-server /usr/local/etc/redis.conf

```

## 代码解析

1.页面提交

提交按钮
```
<button id="submit" type="submit" class="btn btn-google btn-flat" style="margin-left: 0px">提交
                    </button>
```


表单
```
<form class="form-horizontal" action="/scale/innerforecast" method="post" role="form"></form>
```

说明：点击提交按钮的时候，通过 /scale/innerforecast 路径寻找后端路由。


后端代码
```
@scale.route('/innerforecast', methods=['GET', 'POST'])
@app.uuap.login_required
def innerforecast():
    """

    Returns:

    """
    print url_for('scale.innerforecast')
    data = flask.request.form.to_dict()
    if data:
        data['flavor'] = None
        print data
        data['submit_user'] = session.get('username')
        data['satisfy_time'] = None
        data['create_time'] = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        encapsul.insert_inner_data_to_mysql(data)
        return redirect(url_for('scale.innerforecast'))
    records = encapsul.get_inner_data_from_mysql()
    return flask.render_template('scale/innerforecast.tpl', records=records)

```

说明：接收到前端请求，向数据库发请求获取到数据，最终向页面返回数据




## 优化点

1.分页优化，改为异步获取数据分页



## 数据库操作

```
## 连接数据库
mysql -u root


## 查看所有数据库
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.00 sec)

## 创建数据库test
mysql>  CREATE DATABASE test;
Query OK, 1 row affected (0.01 sec)

## 再次查看数据库，是否创建成功
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| test               |
+--------------------+
5 rows in set (0.00 sec)

## 使用 test 数据库
mysql> use test;
Database changed


## 查看 test 数据库中有哪些表
mysql> show tables;
Empty set (0.00 sec)

## 创建数据库表 runoob_tbl
mysql> CREATE TABLE IF NOT EXISTS `runoob_tbl`(
    ->    `runoob_id` INT UNSIGNED AUTO_INCREMENT,
    ->    `runoob_title` VARCHAR(100) NOT NULL,
    ->    `runoob_author` VARCHAR(40) NOT NULL,
    ->    `submission_date` DATE,
    ->    PRIMARY KEY ( `runoob_id` )
    -> )ENGINE=InnoDB DEFAULT CHARSET=utf8;
Query OK, 0 rows affected (0.03 sec)


## 再次查看数据库 表信息
mysql> show tables;
+----------------+
| Tables_in_test |
+----------------+
| runoob_tbl     |
+----------------+
1 row in set (0.00 sec)

## 查看 runoob_tbl 表的表结构
mysql> desc runoob_tbl;
+-----------------+------------------+------+-----+---------+----------------+
| Field           | Type             | Null | Key | Default | Extra          |
+-----------------+------------------+------+-----+---------+----------------+
| runoob_id       | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| runoob_title    | varchar(100)     | NO   |     | NULL    |                |
| runoob_author   | varchar(40)      | NO   |     | NULL    |                |
| submission_date | date             | YES  |     | NULL    |                |
+-----------------+------------------+------+-----+---------+----------------+
4 rows in set (0.02 sec)


## 给 runoob_tbl 表添加字段,字段名为 id, 并且显示在 submission_date 字段之后
mysql> alter table `runoob_tbl`  Add column id int not null default 0 AFTER `submission_date`;
Query OK, 0 rows affected (0.03 sec)
Records: 0  Duplicates: 0  Warnings: 0

## 再次查看数据库有哪些表
mysql> show tables;
+----------------+
| Tables_in_test |
+----------------+
| runoob_tbl     |
+----------------+
1 row in set (0.00 sec)

## 再次查看表结构
mysql> desc runoob_tbl;
+-----------------+------------------+------+-----+---------+----------------+
| Field           | Type             | Null | Key | Default | Extra          |
+-----------------+------------------+------+-----+---------+----------------+
| runoob_id       | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| runoob_title    | varchar(100)     | NO   |     | NULL    |                |
| runoob_author   | varchar(40)      | NO   |     | NULL    |                |
| submission_date | date             | YES  |     | NULL    |                |
| id              | int(11)          | NO   |     | 0       |                |
+-----------------+------------------+------+-----+---------+----------------+
5 rows in set (0.00 sec)


## 删除字段，字段名为id
mysql> alter table runoob_tbl drop column id;
Query OK, 0 rows affected (0.02 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc runoob_tbl;
+-----------------+------------------+------+-----+---------+----------------+
| Field           | Type             | Null | Key | Default | Extra          |
+-----------------+------------------+------+-----+---------+----------------+
| runoob_id       | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| runoob_title    | varchar(100)     | NO   |     | NULL    |                |
| runoob_author   | varchar(40)      | NO   |     | NULL    |                |
| submission_date | date             | YES  |     | NULL    |                |
+-----------------+------------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)


## 插入数据
mysql> INSERT INTO runoob_tbl (runoob_title, runoob_author, submission_date)  VALUES ("学习 PHP", "菜鸟教程", NOW()); 
Query OK, 1 row affected, 1 warning (0.01 sec)


## 查询
mysql> select * from runoob_tbl;
+-----------+--------------+---------------+-----------------+
| runoob_id | runoob_title | runoob_author | submission_date |
+-----------+--------------+---------------+-----------------+
|         1 | 学习 PHP     | 菜鸟教程      | 2018-01-07      |
+-----------+--------------+---------------+-----------------+
1 row in set (0.00 sec)

## 更新数据
mysql> UPDATE runoob_tbl SET runoob_title='学习 C++' WHERE runoob_id=1;
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from runoob_tbl;
+-----------+--------------+---------------+-----------------+
| runoob_id | runoob_title | runoob_author | submission_date |
+-----------+--------------+---------------+-----------------+
|         1 | 学习 C++     | 菜鸟教程      | 2018-01-07      |
+-----------+--------------+---------------+-----------------+
1 row in set (0.00 sec)


## 再插入一条数据
mysql> INSERT INTO runoob_tbl (runoob_title, runoob_author, submission_date)  VALUES ("学习 PHP2", "菜鸟教程2", NOW());
Query OK, 1 row affected, 1 warning (0.00 sec)

mysql> select * from runoob_tbl;                                                                                     +-----------+--------------+---------------+-----------------+
| runoob_id | runoob_title | runoob_author | submission_date |
+-----------+--------------+---------------+-----------------+
|         1 | 学习 C++     | 菜鸟教程      | 2018-01-07      |
|         2 | 学习 PHP2    | 菜鸟教程2     | 2018-01-07      |
+-----------+--------------+---------------+-----------------+
2 rows in set (0.00 sec)


## 删除 runoob_id=2 的数据 
mysql> DELETE FROM runoob_tbl WHERE runoob_id=2;
Query OK, 1 row affected (0.00 sec)

mysql> select * from runoob_tbl;
+-----------+--------------+---------------+-----------------+
| runoob_id | runoob_title | runoob_author | submission_date |
+-----------+--------------+---------------+-----------------+
|         1 | 学习 C++     | 菜鸟教程      | 2018-01-07      |
+-----------+--------------+---------------+-----------------+
1 row in set (0.00 sec)



```



