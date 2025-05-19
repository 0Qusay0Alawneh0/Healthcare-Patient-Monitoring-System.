from neo4j import GraphDatabase
from config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def add_doctor_patient(patient_id, patient_name, doctor_id, doctor_name):
    with driver.session() as session:
        session.run(
            "MERGE (p:Patient {id: $pid, name: $pname}) "
            "MERGE (d:Doctor {id: $did, name: $dname}) "
            "MERGE (p)-[:ATTENDED_BY]->(d)",
            pid=patient_id, pname=patient_name, did=doctor_id, dname=doctor_name
        )

def get_doctors_of_patient(patient_id):
    with driver.session() as session:
        result = session.run(
            "MATCH (p:Patient {id: $pid})-[:ATTENDED_BY]->(d:Doctor) RETURN d.name", pid=patient_id
        )
        return [record["d.name"] for record in result]

if __name__ == "__main__":
    add_doctor_patient("patient_001", "Ahmad Alali", "doctor_001", "Dr. Sara")
    print(get_doctors_of_patient("patient_001"))
