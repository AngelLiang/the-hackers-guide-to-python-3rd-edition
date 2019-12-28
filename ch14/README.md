
## nofify_on_insert 的触发函数

通过 psql 中的 LISTEN 操作来检查是否工作正常：

```
Server [localhost]:
Database [postgres]: mydatabase
Port [5432]:
Username [postgres]:
用户 postgres 的口令：
psql (12.1)
输入 "help" 来获取帮助信息.

mydatabase=# LISTEN channel_1;
LISTEN
mydatabase=# INSERT INTO message(channel, source, content)
mydatabase-# VALUES(1, 'jd', 'hello world');
INSERT 0 1
从PID为5656的服务器进程接收到带有字节流量"{"id":1,"channel":1,"source":"jd","content":"hello world"}"的异步通知消息"channel_1".
mydatabase=#
```
