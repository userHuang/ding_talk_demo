**customer_manage**
# 钉钉企业会话消息推送demo

# ant design mobile
# python react

# FAQ

安装 python Django

### 如何准备NodeJS环境？ ###

如果没有安装cnpm，安装cnpm：
```
npm install -g cnpm --registry=https://registry.npm.taobao.org 
```

安装必要的包：
```
cnpm install supervisor -g
cnpm install -g bunyan
cnpm install
```

### 如何在本地开发调试？ ###

答：初次搭建环境，按如下步骤：
1. 在mysql中创建`ding_talk`数据库: `create database ding_talk default character set utf8 `;
1. 将`ding_talk`数据库授权给`ding_talk`用户：`grant all on ding_talk.* to 'ding_talk'@localhost identified by 'huangjian'`
1. 初始化数据库
1. 启动 `start_bundle_server.bat`
1. 启动 `start_service.bat | bunyan`
1. 访问 `http://127.0.0.1:9000/account/login/`
1. 登陆系统
