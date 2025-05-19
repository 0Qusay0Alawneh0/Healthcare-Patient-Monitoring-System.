import redis
from config import REDIS_HOST, REDIS_PORT

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def set_alert(patient_id, timestamp, alert):
    key = f"alert:{patient_id}:{timestamp}"
    r.set(key, alert)

def get_alerts_for_patient(patient_id):
    pattern = f"alert:{patient_id}:*"
    return {k: r.get(k) for k in r.keys(pattern)}

if __name__ == "__main__":
    set_alert("patient_001", "2025-05-19T10:01:00Z", '{"type":"high_bp","value":180,"notified":false}')
    print(get_alerts_for_patient("patient_001"))
