#  基础环境搭建

> 基于Anaconda的，如果把python比作Linux的话，那么Anaconda就类似于centos，Ubuntu这种，意会一下

**下载地址：** https://www.anaconda.com/distribution/

## 安装使用

#### 安装

没什么好介绍的，可视化丰富，下载对应版本，一路click。

**window下环境变量：**
```
C:\Users\ataola\Anaconda3;
C:\Users\ataola\Anaconda3\Library\mingw-w64\bin;
C:\Users\ataola\Anaconda3\Library\usr\bin;
C:\Users\ataola\Anaconda3\Library\bin;
C:\Users\ataola\Anaconda3\Scripts;
```

#### 使用

##### 基本命令

* 查看帮助: `conda -h`

* 查看版本: `conda -V`


##### 换源

如果你在国内的话，由于墙的原因你需要换个源，国外就算了。

* 查看配置命令：`conda list --show`

* 配置源

```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge 
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/menpo/

conda config --set show_channel_urls yes
```

**参考：** https://mirror.tuna.tsinghua.edu.cn/help/anaconda/


##### 创建一个Python3.7的虚拟环境

命令如下：`conda create --name py37 python=3.7`

日志记录

```
C:\Users\ataola>conda create --name py37 python=3.7
Solving environment: done


==> WARNING: A newer version of conda exists. <==
  current version: 4.5.11
  latest version: 4.8.2

Please update conda by running

    $ conda update -n base -c defaults conda



## Package Plan ##

  environment location: C:\Users\ataola\Anaconda3\envs\py37

  added / updated specs:
    - python=3.7


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    sqlite-3.31.1              |       he774522_0         961 KB
    certifi-2019.11.28         |           py37_0         157 KB
    python-3.7.6               |       h60c2a47_2        18.3 MB
    wheel-0.34.2               |           py37_0          67 KB
    openssl-1.1.1d             |       he774522_4         5.7 MB
    vs2015_runtime-14.16.27012 |       hf0eaf9b_1         2.4 MB
    setuptools-46.0.0          |           py37_0         665 KB
    pip-20.0.2                 |           py37_1         1.9 MB
    ca-certificates-2020.1.1   |                0         165 KB
    ------------------------------------------------------------
                                           Total:        30.3 MB

The following NEW packages will be INSTALLED:

    ca-certificates: 2020.1.1-0
    certifi:         2019.11.28-py37_0
    openssl:         1.1.1d-he774522_4
    pip:             20.0.2-py37_1
    python:          3.7.6-h60c2a47_2
    setuptools:      46.0.0-py37_0
    sqlite:          3.31.1-he774522_0
    vc:              14.1-h0510ff6_4
    vs2015_runtime:  14.16.27012-hf0eaf9b_1
    wheel:           0.34.2-py37_0
    wincertstore:    0.2-py37_0

Proceed ([y]/n)? y


Downloading and Extracting Packages
sqlite-3.31.1        | 961 KB    | ############################################################################ | 100%
certifi-2019.11.28   | 157 KB    | ############################################################################ | 100%
python-3.7.6         | 18.3 MB   | ############################################################################ | 100%
wheel-0.34.2         | 67 KB     | ############################################################################################################################ | 100%
openssl-1.1.1d       | 5.7 MB    | ############################################################################################################################ | 100%
vs2015_runtime-14.16 | 2.4 MB    | ############################################################################################################################ | 100%
setuptools-46.0.0    | 665 KB    | ############################################################################################################################ | 100%
pip-20.0.2           | 1.9 MB    | ############################################################################################################################ | 100%
ca-certificates-2020 | 165 KB    | ############################################################################################################################ | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use:
# > activate py37
#
# To deactivate an active environment, use:
# > deactivate
#
# * for power-users using bash, you must source
#


C:\Users\ataola>
```

激活py37环境: `activate py37`

```

C:\Users\ataola>activate py37

(py37) C:\Users\ataola>python -V
Python 3.7.6

(py37) C:\Users\ataola>
```

退出py37环境: `deactivate`

*注意是直接deactivate*

移除虚拟环境：`conda remove --name py37 --all`

查看安装虚拟环境列表：`conda env list`

```
C:\Users\ataola>conda env list
# conda environments:
#
base                  *  C:\Users\ataola\Anaconda3
py37                     C:\Users\ataola\Anaconda3\envs\py37


C:\Users\ataola>activate py37
```

查看环境包: `conda list`


与之类似的可以搜下`virtualenv`这个包，这里不作介绍了。

##### jupyter notebook

在命令行输入`jupyter notebook`，会打开浏览器然后进到楼下编程界面

![](img/01-anaconda.png)

