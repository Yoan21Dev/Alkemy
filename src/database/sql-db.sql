
-- Creacion de las tablas 

CREATE TABLE "Date" (
        id INTEGER NOT NULL,
        id_provincia INTEGER NOT NULL,
        id_departamento INTEGER,
        category VARCHAR NOT NULL,
        provincia VARCHAR NOT NULL,
        localidad VARCHAR NOT NULL,
        nombre VARCHAR NOT NULL,
        domicilio VARCHAR NOT NULL,
        codigo_postal INTEGER NOT NULL,
        numero_de_telefono INTEGER NOT NULL,
        web VARCHAR NOT NULL,
        update_at TIMESTAMP WITHOUT TIME ZONE,
        create_at TIMESTAMP WITHOUT TIME ZONE,
        PRIMARY KEY (id, id_provincia),
        UNIQUE (id_departamento)
)