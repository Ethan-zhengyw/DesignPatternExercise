# 09 原型模式

## 用原型实例指定创建对象的种类，并通过拷贝这些原型创建新的对象

### 即C++中的拷贝构造函数

### 编程实现过程——在原型基类中定义Cloneable接口，接口中定义抽象拷贝方法，具体原型类实现该接口，视情况实现深浅复制

## 避免重新初始化对象，而是动态地获取已有对象的运行时状态

### 隐藏对象创建的细节，创建完成后再进行定制修改

## 浅复制与深复制

### 浅复制

#### 被复制对象的所有变量都含有与原对象相同的值

#### 对其他对象的引用仍然指向原来的对象

### 深复制

#### 引用的对象的变量指向新复制出来的对象，而非原有被引用的对象
