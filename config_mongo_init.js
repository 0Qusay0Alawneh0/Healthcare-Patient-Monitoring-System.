db = db.getSiblingDB('healthcare');
db.createCollection('patients');
db.patients.createIndex({region: 1});
