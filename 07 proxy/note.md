# 07 代理模式

## 定义

### 为其他对象提供一种代理以控制对这个对象的访问

## 应用场景

### 远程代理

#### 为一个对象在不同的地址空间提供局部代表，这样可以隐藏一个对象存在于不同地址空间的事实

#### 解决远程访问的问题

##### RPC？

### 虚拟代理

#### 根据需要创建开销很大的对象。通过它来存放实例化需要很长时间的真是对象

#### 优化性能

##### 浏览器下载优化，显示过程中图片没下载完就先放张假的提示正在下载

##### 文件/数据库访问缓存

### 安全代理

#### 用来控制真实对象访问时的权限

### 智能指引

#### 调用真实的对象时，代理处理另外一些事

##### 访问一个对象时负载一些内务处理

###### 计算真实对象引用次数

###### 检查对象是否已经锁定

## 代理模式 vs 策略模式

### 策略模式中的环境类类似代理模式中的代理类

#### Context ～ Proxy

### 策略模式重组合、代理模式重控制

#### 策略模式主要是环境类中的策略对象会发生改变

#### 代理模式主要是隐藏真实对象，提供额外的处理逻辑，以达到性能优化、安全性提升等作用

#### 代理模式中代理类与被代理类实现相同的接口

## 练习

### https://web.ti.bfh.ch/~due1/courses/c355/exercises/proxy/index.html
