@echo off
REM PyPi 模块 发布脚本

echo "正在打包..."
python -m build
echo "打包完成"
echo "正在上传PyPi.org..."
twine upload dist/*
echo "上传完成"
rmdir /S /Q dist
rmdir /S /Q build
rmdir /S /Q quant1x_xtquant.egg-info
rmdir /S /Q .eggs
@echo on