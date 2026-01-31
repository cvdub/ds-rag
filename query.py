import psycopg
from openai import OpenAI

DB_CONN = "dbname=draw_steel user=postgres password=postgres host=localhost"
client = OpenAI()


def query_db(query: str, k: int = 10):
    """Perform semantic search on the documents database."""
    # Generate query embedding
    response = client.embeddings.create(
        input=[query],
        model="text-embedding-3-small"
    )
    query_embedding = response.data[0].embedding

    # Search database using vector similarity
    with psycopg.connect(DB_CONN) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT content, embedding <=> %s::vector AS distance
                FROM documents
                ORDER BY embedding <=> %s::vector
                LIMIT %s
                """,
                (query_embedding, query_embedding, k)
            )

            results = []
            for row in cur.fetchall():
                results.append({
                    "content": row[0],
                    "distance": float(row[1])
                })

            return results
