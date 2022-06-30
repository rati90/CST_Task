BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "users" (
	"created_at"	DATETIME NOT NULL,
	"updated_at"	DATETIME NOT NULL,
	"id"	INTEGER NOT NULL,
	"username"	VARCHAR(100) NOT NULL,
	"email"	VARCHAR(100) NOT NULL,
	"hashed_password"	VARCHAR(300) NOT NULL,
	"role"	VARCHAR(9),
	"is_public"	BOOLEAN,
	"is_active"	BOOLEAN DEFAULT 'true',
	PRIMARY KEY("id")
);
INSERT INTO "users" VALUES ('2022-06-30 11:53:05.373543','2022-06-30 11:53:05.373543',1,'string','string','$2b$12$QoSMiT8tupp6q6Y12GfgaO.PY48ae8L3SHQmef7jhOTFT21YfzZ9K','user',1,1);
CREATE UNIQUE INDEX IF NOT EXISTS "ix_users_email" ON "users" (
	"email"
);
CREATE UNIQUE INDEX IF NOT EXISTS "ix_users_username" ON "users" (
	"username"
);
CREATE INDEX IF NOT EXISTS "ix_users_id" ON "users" (
	"id"
);
COMMIT;
