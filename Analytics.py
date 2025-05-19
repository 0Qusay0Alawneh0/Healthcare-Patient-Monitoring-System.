from cassandra.cluster import Cluster
from config import CASSANDRA_HOSTS

cluster = Cluster(CASSANDRA_HOSTS)
session = cluster.connect()

def setup_keyspace_and_table():
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS analytics WITH replication = {
            'class':'SimpleStrategy', 'replication_factor' : 1
        }
    """)
    session.execute("""
        CREATE TABLE IF NOT EXISTS analytics.patient_stats (
            region text,
            date date,
            patient_id text,
            avg_heartbeat double,
            PRIMARY KEY ((region), date, patient_id)
        )
    """)

def add_patient_stat(region, date, patient_id, avg_heartbeat):
    session.execute(
        "INSERT INTO analytics.patient_stats (region, date, patient_id, avg_heartbeat) VALUES (%s, %s, %s, %s)",
        (region, date, patient_id, avg_heartbeat)
    )

def get_patient_stats(region, date):
    rows = session.execute(
        "SELECT * FROM analytics.patient_stats WHERE region=%s AND date=%s", (region, date)
    )
    return list(rows)

if __name__ == "__main__":
    setup_keyspace_and_table()
    add_patient_stat("North", "2025-05-19", "patient_001", 78.5)
    print(get_patient_stats("North", "2025-05-19"))
