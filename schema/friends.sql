BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "friends" (
	"id"	INTEGER NOT NULL,
	"user_id"	INTEGER,
	"friend_id"	INTEGER NOT NULL,
	PRIMARY KEY("id"),
	FOREIGN KEY("user_id") REFERENCES "users"("id")
);
CREATE INDEX IF NOT EXISTS "ix_friends_id" ON "friends" (
	"id"
);
COMMIT;
