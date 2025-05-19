from influxdb_client import InfluxDBClient, Point, WritePrecision
from config import INFLUXDB_URL, INFLUXDB_TOKEN, INFLUXDB_ORG, INFLUXDB_BUCKET

client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)
write_api = client.write_api()
query_api = client.query_api()

def add_measurement(patient_id, heartbeat, bp_sys, bp_dia, timestamp):
    p = Point("body_measurement") \
        .tag("patient_id", patient_id) \
        .field("heartbeat", heartbeat) \
        .field("bp_sys", bp_sys) \
        .field("bp_dia", bp_dia) \
        .time(timestamp, WritePrecision.NS)
    write_api.write(INFLUXDB_BUCKET, INFLUXDB_ORG, p)

def get_measurements(patient_id, range_start="-1h"):
    query = f'''
        from(bucket: "{INFLUXDB_BUCKET}")
        |> range(start: {range_start})
        |> filter(fn: (r) => r["patient_id"] == "{patient_id}")
    '''
    return query_api.query_org(INFLUXDB_ORG, query)

if __name__ == "__main__":
    add_measurement("patient_001", 78, 120, 80, "2025-05-19T10:00:00Z")
