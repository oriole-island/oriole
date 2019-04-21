# oriole

## 安装

  pip install oriole-service

# 编译

  oriole因为涉及C语言的编程环境，不推荐自己编译，作者不提供C语言使用方面的帮助。
  正确的做法是：pip install oriole-service

### 编译方法：

1. 安装libpython3.6
2. 用自己的虚拟环境替代/home/xx/p3
3. 将所有.c编译成.so

例如：编译cf.c
<code>

gcc -pthread -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D\_FORTIFY\_SOURCE=2 -fPIC -I/home/xx/p3/include -I/usr/include/python3.6m -c cf.c -o cf.o

gcc -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D\_FORTIFY\_SOURCE=2 cf.o -o cf.cpython-36m-x86\_64-linux-gnu.so
</code>
