CREATE TABLE "unidad" (
    "id"  SERIAL  NOT NULL,
    "nombre" varchar(100)   NOT NULL,
    CONSTRAINT "pk_unidad" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "direcccion" (
    "id"  SERIAL  NOT NULL,
    "id_pais" int   NOT NULL,
    "id_region" int   NOT NULL,
    "calle" varchar(100)   NOT NULL,
    "numero" varchar(10)   NOT NULL,
    "depto_casa" varchar(10)   NOT NULL,
    "id_unidad" int   NOT NULL,
    CONSTRAINT "pk_direcccion" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "persona" (
    "id"  SERIAL  NOT NULL,
    "rut" int   NOT NULL,
    "id_unidad" int   NOT NULL,
    "estado" boolean   NOT NULL,
    "email" varchar(100)   NOT NULL,
    "nombre" varchar(100)   NOT NULL,
    "id_perfil" int   NOT NULL,
    "contrasena" varchar(100)   NOT NULL,
    CONSTRAINT "pk_persona" PRIMARY KEY (
        "id"
     ),
    CONSTRAINT "uc_persona_rut" UNIQUE (
        "rut"
    )
);

CREATE TABLE "tarea" (
    "id"  SERIAL  NOT NULL,
    "id_unidad" int   NOT NULL,
    "nombre" varchar(100)   NOT NULL,
    CONSTRAINT "pk_tarea" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "tarea_persona" (
    "id"  SERIAL  NOT NULL,
    "id_persona" int   NOT NULL,
    "id_unidad" int   NOT NULL,
    "id_tarea" int   NOT NULL,
    "fecha_inicio" date   NOT NULL,
    "fecha_termino" date   NOT NULL,
    CONSTRAINT "pk_tarea_persona" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "gasto" (
    "id"  SERIAL  NOT NULL,
    "factura" varchar(100)   NOT NULL,
    "id_unidad" int   NOT NULL,
    "monto_orginal" int   NOT NULL,
    "descripcion" varchar(100)   NOT NULL,
    CONSTRAINT "pk_gasto" PRIMARY KEY (
        "id"
     ),
    CONSTRAINT "uc_gasto_factura" UNIQUE (
        "factura"
    )
);

CREATE TABLE "gasto_persona" (
    "id"  SERIAL  NOT NULL,
    "id_persona" int   NOT NULL,
    "factura" varchar(100)   NOT NULL,
    "monto_prorrateado" int   NOT NULL,
    CONSTRAINT "pk_gasto_persona" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "perfil" (
    "id"  SERIAL  NOT NULL,
    "nombre" varchar(50)   NOT NULL,
    CONSTRAINT "pk_perfil" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "pais" (
    "id"  SERIAL  NOT NULL,
    "codigo_iso" varchar(3)   NOT NULL,
    "nombre" varchar(250)   NOT NULL,
    CONSTRAINT "pk_pais" PRIMARY KEY (
        "id"
     ),
    CONSTRAINT "uc_pais_codigo_iso" UNIQUE (
        "codigo_iso"
    )
);

CREATE TABLE "region" (
    "id"  SERIAL  NOT NULL,
    "id_pais" int   NOT NULL,
    "nombre" varchar(250)   NOT NULL,
    CONSTRAINT "pk_region" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "comuna" (
"id" SERIAL NOT NULL,
"id_region" int NOT NULL,
"nombre" varchar(250),
CONSTRAINT "pk_comuna" PRIMARY KEY("id")
)

-- Free plan table limit reached. SUBSCRIBE for more.



ALTER TABLE "direcccion" ADD CONSTRAINT "fk_direcccion_id_pais" FOREIGN KEY("id_pais")
REFERENCES "pais" ("id");

ALTER TABLE "direcccion" ADD CONSTRAINT "fk_direcccion_id_unidad" FOREIGN KEY("id_unidad")
REFERENCES "unidad" ("id");

ALTER TABLE "persona" ADD CONSTRAINT "fk_persona_id_unidad" FOREIGN KEY("id_unidad")
REFERENCES "unidad" ("id");

ALTER TABLE "persona" ADD CONSTRAINT "fk_persona_id_perfil" FOREIGN KEY("id_perfil")
REFERENCES "perfil" ("id");

ALTER TABLE "tarea" ADD CONSTRAINT "fk_tarea_id_unidad" FOREIGN KEY("id_unidad")
REFERENCES "unidad" ("id");

ALTER TABLE "tarea_persona" ADD CONSTRAINT "fk_tarea_persona_id_persona" FOREIGN KEY("id_persona")
REFERENCES "persona" ("id");

ALTER TABLE "tarea_persona" ADD CONSTRAINT "fk_tarea_persona_id_unidad" FOREIGN KEY("id_unidad")
REFERENCES "unidad" ("id");

ALTER TABLE "tarea_persona" ADD CONSTRAINT "fk_tarea_persona_id_tarea" FOREIGN KEY("id_tarea")
REFERENCES "tarea" ("id");

ALTER TABLE "gasto" ADD CONSTRAINT "fk_gasto_id_unidad" FOREIGN KEY("id_unidad")
REFERENCES "unidad" ("id");

ALTER TABLE "gasto_persona" ADD CONSTRAINT "fk_gasto_persona_id_persona" FOREIGN KEY("id_persona")
REFERENCES "persona" ("id");

ALTER TABLE "gasto_persona" ADD CONSTRAINT "fk_gasto_persona_factura" FOREIGN KEY("factura")
REFERENCES "gasto" ("factura");

ALTER TABLE "region" ADD CONSTRAINT "fk_region_id_pais" FOREIGN KEY("id_pais")
REFERENCES "pais" ("id");

ALTER TABLE gasto_persona
ADD CONSTRAINT unique_factura_id_persona
UNIQUE (factura, id_persona);