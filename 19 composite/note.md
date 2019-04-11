# 19 组合模式

## 定义

### 将对象组合成树形结构以表示“部分—整体”的层次结构。组合模式使得用户对单个对象和组合对象的使用具有一致性。

## 概念

### 组件

#### 叶子

##### 没有子节点

#### 组合

##### 包含多个从属的组件

#### 叶子与组合的抽象，定义了叶子和组合需要实现的统一的接口

## 透明方式与不透明方式

### 叶子与组合可能存在一些不同的接口，这部分接口是否要放到组合抽象中

#### 是 --> 叶子与组合完全操作完全统一，对客户来讲是透明的，不需要考虑这个组件是叶子还是组合

#### 否 --> 叶子节点不需要实现多余的没有意义的接口，客户端需要感知操作的组件是组合还是叶子

## 应用场景

### Word文档里的文字处理：对一个字处理与对多个字处理

### 文件系统：处理一个文件与处理一个文件夹

### 绘图工具：对一个图形处理与对多个图形处理

### 企业组织结构

### 需求中体现部分与整体层次结构时，希望用户可以忽略组合对象与单个对象的不同，统一地使用组合结构中的所有对象时，考虑使用组合模式