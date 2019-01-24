版本：

python = 3.7

pip = 19

**前言**

由于考虑到以后要动态切分数据，防止将不同表切分数据到同一个表中时出现主键相等的冲突情况，这里我们使用一个全局ID生存器。重要的是他是自增的。
这边我使用`Snowflake`的python实现版（pysnowflake）。当然你也可以使用java实现版.
百度如何使用uid：https://github.com/baidu/uid-generator/blob/master/README.zh_cn.md

### Snowflake的使用

- **安装 requests**

```
pip install requests
```

- **安装 pysnowflake**

```
pip install pysnowflake
```

- **启动pysnowflake服务**

```
snowflake_start_server \
  --address=192.168.10.145 \
  --port=30001 \
  --dc=1 \
  --worker=1 \
  --log_file_prefix=/tmp/pysnowflask.log
```

~~~
# --address：本机的IP地址默认localhost这里解释一下参数意思（可以通过--help来获取）：
# --dc：数据中心唯一标识符默认为0
# --worker：工作者唯一标识符默认为0
# --log_file_prefix：日志文件所在位置
~~~

​																				---dingkou write；
