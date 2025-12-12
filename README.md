# DB-Type

This app shows you, which Type of Database in the website. It shows after the ports which use the databases:

db_ports = {
    "MySQL/MariaDB": 3306,
    "PostgreSQL": 5432,
    "SQL Server (MSSQL)": 1433,   # 1434 für Browser Service
    "Oracle DB": 1521,            # auch 2483/2484 für TCPS
    "IBM Db2": 50000,             # weitere Ports 50001-50050
    "SAP MaxDB": 7210,

    "SQLite": None,               # keine Netzwerkverbindung

    "MongoDB": 27017,             # 27018 Shard, 27019 Config
    "Redis": 6379,                # 26379 Sentinel, 16379 Cluster
    "Cassandra": 9042,            # 7000 intern
    "Elasticsearch": 9200,        # 9300 intern
    "CouchDB": 5984,              # 6984 HTTPS
    "Neo4j": 7474,                # 7473 HTTPS
    "ArangoDB": 8529,
    "Riak": 80,
    "HBase": 16000,               # 16020/16030 für RegionServer
    "DynamoDB": None,             # AWS-Service, kein Port
}

Music by SubspaceAudio
