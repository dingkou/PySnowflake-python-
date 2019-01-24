# --dingkou--
# 导入pysnowflake客户端
import snowflake.client

# 连接服务端并初始化一个pysnowflake客户端
host = '127.0.0.1'
port = 8000
def snowflake_():
    snowflake.client.setup(host, port)
    '''
     查看当前状态:snowflake.client.get_stats()
     生成一个全局唯一的ID（在MySQL中可以用BIGINT UNSIGNED对应）:snowflake.client.get_guid()
    '''
    return snowflake.client.get_guid(),snowflake.client.get_stats()

if __name__ == '__main__':
    user_id,status_sf = snowflake_()
    print(user_id)
    print(status_sf)

'''snowflake.client.get_stats()
{
  'dc': 1,
  'worker': 1,
  'timestamp': 1548308065899, # current timestamp for this worker
  'last_timestamp': 1548308065896, # the last timestamp that generated ID on
  'sequence': 1, # the sequence number for last timestamp
  'sequence_overload': 0, # the number of times that the sequence is overflow
  'errors': 0, # the number of times that clock went backward
}
'''