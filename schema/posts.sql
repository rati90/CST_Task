BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "posts" (
	"created_at"	DATETIME NOT NULL,
	"updated_at"	DATETIME NOT NULL,
	"id"	INTEGER NOT NULL,
	"description"	TEXT NOT NULL,
	"user_id"	INTEGER NOT NULL,
	PRIMARY KEY("id"),
	FOREIGN KEY("user_id") REFERENCES "users"("id")
);
CREATE INDEX IF NOT EXISTS "ix_posts_id" ON "posts" (
	"id"
);
COMMIT;
