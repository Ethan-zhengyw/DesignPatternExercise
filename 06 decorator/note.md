# 06 装饰器模式

## 定义

### 动态地给一个对象添加一些额外地职责，不用生成新的子类

## 优点

### 新加入的职责只是在某些场景需要使用时，使用该模式能够避免把类地核心职责与装饰职责混合在一起

## 是否需要抽象组件类？

### 非必须，如果只有一个具体组件，就没有必要进行抽象了

### 类似的，抽象装饰类也不是必须的

### 根据不同场景需求，组件与装饰器是否需要抽象的组合有4种

#### 一、组件不抽象、装饰器不抽象

##### 最简单的场景，一次性

#### 二、组件不抽象、装饰器抽象

##### 针对一个组件有多种不同的装饰

#### 三、组件抽象、装饰器不抽象

##### 针对不同的具体组件有一个相同的装饰方法

#### 四、组件抽象、装饰器抽象

##### 最通用的方法，针对不同的具体组件有多种不同的装饰方法

## 练习

### 《大话设计模式》一书中的例子——按顺序给人穿上衣服，最后再显示这个人的穿着
