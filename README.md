# learn-py3

Learn Pythone 3 (3.6+) with VS Code

## 环境配置

### 配置 Python interpreter

可以通过打开命令面板 （Shift + cmd + p） 然后输出 `Python: Select interpreter` 来选择。
本项目之后。 为了升级到 `python 3.7` 之后不需要修改路径，所以选择了 `/usr/local/bin/python3`
暂时指向 `3.6.5`

### 配置自动格式化

本项目选择 `black` 作为自动格式化工具。
所以我们先安装一下 `pip3 install balck`
然后配置一下.

```json
{
  "python.formatting.provider": "black",
  "editor.formatOnSave": true
}
```

### 配置 lint

VSCode 默认使用的是 Pylint .
我们先安装一下 `pip3 install pylint`
然后再配置开启 Pylint.

```json
{
  "python.linting.enabled": true
}
```

更多说明参考 [Python Linting](https://code.visualstudio.com/docs/python/linting)

### Ctags

项目符号，VS Code Python 插件提示安装 `ctags.

安装 ctags `brew install ctags`

## 运行与调试

1.  直接按 `Ctrl+F5` 即可执行当前文件。 `F5` 高度当前文件。

也可以通过添加如下任务来实现上面的目标:

```json
{
  "name": "Python: Current File",
  "type": "python",
  "request": "launch",
  "program": "${file}"
}
```

更多运行配置，参考 [Python Debugging](https://code.visualstudio.com/docs/python/debugging)

## 单元测试

推荐使用 `pytest` 然后 VS Code 默认配置的也是 `pytest`

```json
{
  "python.unitTest.pyTestEnabled": true
}
```

安装 `pytest` ,`pip3 install --user pytest`

更多单元测试的配置说明，参考：[Unit Testing](https://code.visualstudio.com/docs/python/unit-testing)

写好单元测试之后，在测试文件右键可以选择 `Run Current Unittest File`。
也可以点击下面的状态栏的图标，命令面板，文件浏览器右键选择。

## 开始写代码

推荐的学习路径是通过阅读 Python 文档。以对应的文档的章节标题创建单元测试文件。
比如针对 Python References 中的第 3 部分 `Data Model`.
创建 `test_3_data_model` 的包名。 然后创建具体小节的测试文件。
如 `test_3_3_3_customizing_class_creation.py` 单元测试文件。
