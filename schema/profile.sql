BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "profile" (
	"created_at"	DATETIME NOT NULL,
	"updated_at"	DATETIME NOT NULL,
	"id"	INTEGER NOT NULL,
	"first_name"	VARCHAR(50) NOT NULL,
	"last_name"	VARCHAR(50) NOT NULL,
	"bio"	TEXT,
	"user_id"	INTEGER NOT NULL,
	PRIMARY KEY("id"),
	FOREIGN KEY("user_id") REFERENCES "users"("id")
);
CREATE INDEX IF NOT EXISTS "ix_profile_id" ON "profile" (
	"id"
);
COMMIT;
