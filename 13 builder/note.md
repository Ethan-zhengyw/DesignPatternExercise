# 13 建造者模式

## 定义

### 将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示

## 概念

### Builder

#### 为创建一个Product对象的各个部件指定的抽象接口

### ConcreteBuilder

#### 具体建造者，实现Builder接口，构造和装配各个部件

##### 提供get方法获取最终产品

### Product

#### 具体产品

### Director

#### 指挥者

##### 根据用户的需求构建产品

## 好处

### 用于创建一些复杂的对象，这些对象内部构建的顺序通常是稳定的（稳定的工作流程），但对象内部的构建通常面临着复杂的变化

### 隐藏了产品是如何组装出来的，使得建造代码与表示代码分离

## 建造者模式 vs 简单工厂模式 vs 模板方法模式

### 建造者模式

#### 隐藏了产品是如何组装出来的，隐藏了具体的组装流程，确定了组装流程能够减少出错

### 简单工厂模式

#### 强调的是通过指定产品的方式获得产品对象

### 模板方法模式

#### 相对与建造者模式更为简化，建造者模式多了一个Director角色的construct方法来控制组合流程，即模板
