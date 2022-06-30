BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "comments" (
	"created_at"	DATETIME NOT NULL,
	"updated_at"	DATETIME NOT NULL,
	"id"	INTEGER NOT NULL,
	"comment_text"	VARCHAR(200) NOT NULL,
	"post_id"	INTEGER NOT NULL,
	"user_id"	INTEGER NOT NULL,
	PRIMARY KEY("id"),
	FOREIGN KEY("post_id") REFERENCES "posts"("id"),
	FOREIGN KEY("user_id") REFERENCES "users"("id")
);
CREATE INDEX IF NOT EXISTS "ix_comments_id" ON "comments" (
	"id"
);
COMMIT;
