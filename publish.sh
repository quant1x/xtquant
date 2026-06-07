#!/bin/sh
# PyPi 模块 发布脚本

# 获取当前路径, 用于返回
p0=`pwd`
# 获取脚本所在路径, 防止后续操作在非项目路径
p1=$(cd $(dirname $0);pwd)

cd $p1
echo "正在打包..."
python -m build
echo "打包完成"
echo "正在上传PyPi.org..."
twine upload dist/*
echo "上传完成"
rm -rf dist
rm -rf build
rm -rf quant1x_xtquant.egg-info
rm -rf .eggs
cd $p0
