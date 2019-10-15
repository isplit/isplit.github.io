# Blog source file

[![Travis](https://www.travis-ci.org/isplit/isplit.github.io.svg?branch=dev)](https://isplit.github.io)

## 开发步骤

### 克隆项目

- https:
    ```shell
    git clone https://github.com/isplit/isplit.github.io.git
    ```

- ssh:
    ```shell
    git clone git@github.com:isplit/isplit.github.io.git
    ```

### 关联 dev 分支

- 查看所有分支
    ```
    git branch -a
    ```

- 创建并切换到 `dev` 分支，并与远程 `dev` 分支关联
    ```
    git checkout -b dev origin/dev
    ```

### 安装 npm 包

根据 `package.json` 安装

```
npm install --save
```
