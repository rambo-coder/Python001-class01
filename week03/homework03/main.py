# 作业一：
# 背景： 网络安全工具中有一个常用软件称作端口扫描器，即通过一台主机发起向另一主机的常用端口发起连接，探测目标主机是否开放了指定端口，用于改善目标主机的安全状况。
# 要求：编写一个基于多进程或多线程模型的主机扫描器。
# 使用扫描器可以基于 ping 命令快速检测一个 ip 段是否可以 ping 通，如果可以 ping 通返回主机 ip，如果无法 ping 通忽略连接。
# 使用扫描器可以快速检测一个指定 ip 地址开放了哪些 tcp 端口，并在终端显示该主机全部开放的端口。
# ip 地址、使用 ping 或者使用 tcp 检测功能、以及并发数量，由命令行参数传入。
# 需考虑网络异常、超时等问题，增加必要的异常处理。
# 因网络情况复杂，避免造成网络拥堵，需支持用户指定并发数量。
# 命令行参数举例如下：
# pmap.py -n 4 -f ping -ip 192.168.0.1-192.168.0.100
# pmap.py -n 10 -f tcp -ip 192.168.0.1 -w result.json

# 说明：
# 因大家学习的操作系统版本不同，建立 tcp 连接的工具不限，可以使用 telnet、nc 或 python 自带的 socket 套接字。
# -n 参数 并发数量。
# -f ping 进行 ping 测试， -f tcp 进行 tcp 端口开放、关闭测试。
# ip 连续 ip 地址支持 192.168.0.1-192.168.0.100 写法。
# -w 扫描结果进行保存。
# 选做：
# 通过参数 [-m proc|thread] 指定扫描器使用多进程或多线程模型。
# 增加 -v 参数打印扫描器运行耗时 (用于优化代码)。
# 扫描结果显示在终端，并使用 json 格式保存至文件。
# 参考：https://docs.python.org/zh-cn/3/library/subprocess.html
#
# 测试命令1：python pmap.py -n 2 -f ping -ip 38.99.188.1-38.99.188.10
# 测试命令2：python pmap.py -n 2 -f tcp -ip 38.98.133.111
import sys,argparse
from multiprocessing.dummy import Pool as ThreadPool
from ping3 import ping
from ipToList import ipToList

parser = argparse.ArgumentParser()
parser.add_argument("-n",type=int,help="set the number of concurrent thread.")
parser.add_argument("-f",help="set task type, 'ping' or 'tcp' .")
parser.add_argument("-ip",help="set ip address")
parser.add_argument("-w",help="set the name of saved file")
args=parser.parse_args()

cfg = {
    "numberOfConcurrent":args.n or 1,
    "taskType":args.f or 'ping',
    "ipStart":'',
    "ipEnd":'',
    "saveFileName":args.w
}

if args.f == "ping":
    tempList = args.ip.split('-')
    cfg['ipStart'] = tempList[0]
    cfg['ipEnd'] = tempList[1]
elif args.f =='tcp':
    cfg['ipStart'] = args.ip
    cfg['ipEnd'] = ''

def testPing(address):
    print('ping address: ',address)
    pingResult = ping(address)
    if pingResult:
        return address
    else:
        return None


def testTCP(address):
    print('contact:',address)
    return 2

pool = ThreadPool(cfg['numberOfConcurrent'])
if cfg['taskType'] == 'ping':
    taskResults = pool.map(testPing,ipToList(cfg['ipStart'],cfg['ipEnd']))
elif cfg['taskType'] == 'TCP':
    print('tcp')


pool.close()
pool.join()

result = []
if cfg['taskType'] == 'ping':
    for ip in taskResults:
        if ip:
            result.append(ip)

print('===============')
print('有效ip列表：', result)
