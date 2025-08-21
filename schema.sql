DROP TABLE IF EXISTS creditos;

CREATE TABLE creditos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente TEXT,
    monto REAL,
    tasa_interes REAL,
    plazo INTEGER,
    fecha_otorgamiento TEXT
);