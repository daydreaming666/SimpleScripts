# checknames.py

这是一个用来帮助班长和学习委员提前下班的脚本。可以用来检查收上来的文件，并按老师的要求重命名。

比如一个同学上交了`李华.zip`而你们老师想要`软件191-191234567-李华.zip`。它可以帮你完成（前提是上交的同学至少要把自己的姓名写对

## usage

```bash
python checknames.py {working-dir}
```



## settings.json

这是这份脚本的配置文件，需要你提前把班级的信息放进去。

就像：

```json
{
    "name_format": "{classname}-{id}-{name}{extname}", // 这里规定重命名的格式
    "classname": "软件191",	// 班级名
    "names": {
        "李华": "190265461",	// 输入姓名和学号，以逗号隔开
        "王小美": "190265462"
    }
}
```

