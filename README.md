# my-site

# 注意

1. 华为的ecs贼贵
2. docker
3. git
4. 防火墙，安全组，内部的ip

```
docker build -t my-site -f docker/Dockerfile .
docker run -d -p 80:8080 my-site
```

#### 安装git
https://www.jianshu.com/p/1608889b7d2d
https://www.linuxidc.com/Linux/2019-10/161215.htm

#### centos安装docker
https://www.cnblogs.com/qgc1995/p/9553572.html

#### 其他
https://www.cnblogs.com/hailun1987/p/7518306.html

https://support.huaweicloud.com/usermanual-ecs/zh-cn_topic_0030878383.html
https://bbs.huaweicloud.com/ask/1551085535933786

不用git 可以用 winscp