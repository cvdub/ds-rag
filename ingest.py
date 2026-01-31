import psycopg
import tiktoken
from docling.chunking import HybridChunker
from docling.document_converter import DocumentConverter
from docling_core.transforms.chunker.tokenizer.openai import OpenAITokenizer
from openai import OpenAI

md_path = "data-md/Rules/Draw Steel Heroes - Unlinked.md"

client = OpenAI()
tokenizer = OpenAITokenizer(
    tokenizer=tiktoken.encoding_for_model("gpt-4o"),
    max_tokens=128 * 1024,  # context window length required for OpenAI tokenizers
)

# Parse markdown with docling
doc = DocumentConverter().convert(source=md_path).document
# Chunk according to document sections, combining small sections
chunker = HybridChunker(tokenizer=tokenizer, merge_peers=True)
chunks = list(chunker.chunk(dl_doc=doc))

DB_CONN = "dbname=draw_steel user=postgres password=postgres host=localhost"

with psycopg.connect(DB_CONN) as conn:
    with conn.cursor() as cur:
        num_chunks = len(chunks)
        for i, chunk in enumerate(chunks, start=1):
            print(f"CHUNK {i}/{num_chunks}")
            if "Glossary Index" in getattr(chunk.meta, "headings", []):
                continue

            # Add additional context (usually parent headers) to chunk text
            text_for_embedding = chunker.contextualize(chunk)
            response = client.embeddings.create(
                input=text_for_embedding, model="text-embedding-3-small"
            )
            embedding = response.data[0].embedding

            # Save to DB
            cur.execute(
                """
                INSERT INTO documents (embedding, content, meta)
                VALUES (%s, %s, %s)
                """,
                (embedding, text_for_embedding, chunk.model_dump_json()),
            )

    conn.commit()
