# 18 备忘录模式

## 定义

### 在不破坏封装性的前提下，捕获一个对象的内部状态，并在该对象之外保存这个状态。将来可以将该对象恢复到原先保存的状态

## 概念

### originator/发起人

#### 负责创建一个备忘录Memento，记录需要保存的信息

### memento/备忘录

#### 负责存储originator的内部信息

### caretaker/备忘录管理者

#### 负责保存好备忘录，不能对备忘录的内容进行操作

## 为什么需要caretaker？

### It also simplifies originator code such that the originator does not need to 【keep track of its previous state】 since this is the responsibility of the CareTaker.

### caretaker维护的是一个memento列表，原始对象可能有多个备份

## 应用场景

### 文本编辑器历史操作恢复

#### 撤销/重做（undo/redo）

### 数据库事务执行失败回滚

### 游戏临时存档

## 备忘录模式 vs 原型模式

### 复制的数据（应用场景）

#### 备忘录模式只备份部分需要的数据

#### 原型模式一般复制了整个对象的数据

### 实现方式

#### 原型模式是通过定义clone接口、实现clone接口完成目的

#### 备忘录模式定义了新的备忘录类型和负责保管备忘录的管理者类型
