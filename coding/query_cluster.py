from cassandra.cluster import Cluster

cluster = Cluster(
    contact_points=[
        ('127.0.0.1',9042),
        ('127.0.0.1',9043),
        ('127.0.0.1',9044)
    ]
)
session = cluster.connect()
session.default_timeout = None

session.set_keyspace('sadeemlake')

# rows = session.execute('select * from sadeemlake.rawdata where colltype=1 and date_time < totimestamp(now()) limit 1')
rows = session.execute('select count(*) from sadeemlake.rawdata')
print(rows[0])
session.shutdown