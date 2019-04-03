# 外观模式

## 定义

### Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.

### Wrap a complicated subsystem with a simpler interface.

### 为子系统中的一组接口提供一个一致的界面，此模式定义了一个高层接口，这个接口使得这一子系统更加容易使用

#### 即常见的分层设计思维

## 作用

### 即封装，屏蔽细节 + 内部合理抽象，避免耦合

### Facade is more like a simple gateway to a complicated set of functionality. You make a black-box for your clients to worry less i.e. make interfaces simpler.

## 何时使用

### 在设计初期阶段，应该要有意识地将不同的两个层分离，在层与层之间建立外观（Facade）

### 在开发阶段，子系统往往因为不断的重构演化而变得越来越复杂，在必要时增加外观Facade提供一个简单的接口，减少它们之间的依赖

### 在维护一个遗留的大型系统时，可能这个系统已经非常难以维护和扩展了，可以为新系统开发一个外观Facade类，来提供设计粗糙或高度复杂的遗留代码的比较简单的接口，让新系统与Facade对象交互，Facade与遗留代码交互所有复杂的工作

## 经典场景

### 电脑开机/关机

### 统一客户服务入口

#### 订单

#### 计费

#### 物流

### 生活实例

#### 基金 vs 股票

##### 把股票卖了，改去买基金吧（基金经理是Facade）
