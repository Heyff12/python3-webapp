import orm
from models import User, Blog, Comment
import asyncio

async def test(loop):
    #创建连接池,里面的host,port,user,password需要替换为自己数据库的信息
    await orm.create_pool(loop=loop, host='127.0.0.1', port=3306, user='root', password='root',db='awesome')
    #没有设置默认值的一个都不能少
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    await u.save()


# loop = asyncio.get_event_loop()
# #把协程丢到EventLoop中执行
# loop.run_until_complete(test(loop))
# loop.close()
# for x in test(loop):
#     pass


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete( asyncio.wait([test( loop )]) )  
    loop.close()
    if loop.is_closed():
        sys.exit(0)