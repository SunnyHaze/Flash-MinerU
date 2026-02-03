# 编写教程：

## 安装
克隆本仓库后, :
```shell
cd Flash-MinerU
pip install -e .
```
如果安装正确则以下指令应该能正确执行：
```shell
pip show flash-mineru
```

## 仓库结构
1. 全局入口调用方式参考`/test/test_main.py`
2. 请务必随时添加必要依赖到`requirements.txt`
3. 实际pipeline组织逻辑放在中`/flash_mineru/main.py`
4. 实际mineru逻辑函数放在`/flash_mineru/mineru_core`


