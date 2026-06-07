#coding: utf-8

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("quant1x-xtquant")
except PackageNotFoundError:
    __version__ = "0.0.0"


def check_for_update(package_name):
    try:
        import requests
        current_version = __version__
        # 查询PyPI的API获取最新版本信息
        response = requests.get(f"https://pypi.org/pypi/{package_name}/json", timeout=10)
        if response.status_code == 200:
            latest_version = response.json()['info']['version']
            if current_version != latest_version:
                print(f"xtquant{latest_version}已经发布,前往 http://dict.thinktrader.net/nativeApi/download_xtquant.html 查看更新说明\n")
            else:
                print("xtquant文档地址：http://dict.thinktrader.net/nativeApi/start_now.html")
    except Exception:
        pass


try:
    check_for_update("xtquant")
except Exception:
    pass

