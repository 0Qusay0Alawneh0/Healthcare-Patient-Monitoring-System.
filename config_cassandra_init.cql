CREATE KEYSPACE IF NOT EXISTS analytics WITH replication = {
  'class':'SimpleStrategy', 'replication_factor' : 1
};
CREATE TABLE IF NOT EXISTS analytics.patient_stats (
  region text,
  date date,
  patient_id text,
  avg_heartbeat double,
  PRIMARY KEY ((region), date, patient_id)
);
