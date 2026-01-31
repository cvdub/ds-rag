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

# Prepare chunks for batching
chunks_to_process = []
for chunk in chunks:
    if "Glossary Index" in getattr(chunk.meta, "headings", []):
        continue
    text_for_embedding = chunker.contextualize(chunk)
    chunks_to_process.append((chunk, text_for_embedding))

BATCH_SIZE = 100
num_chunks = len(chunks_to_process)

with psycopg.connect(DB_CONN) as conn:
    with conn.cursor() as cur:
        # Process in batches
        for batch_start in range(0, num_chunks, BATCH_SIZE):
            batch_end = min(batch_start + BATCH_SIZE, num_chunks)
            batch = chunks_to_process[batch_start:batch_end]

            print(f"Processing chunks {batch_start + 1}-{batch_end}/{num_chunks}")

            # Extract texts for batch embedding
            texts = [text for _, text in batch]

            # Create embeddings in batch
            response = client.embeddings.create(
                input=texts, model="text-embedding-3-small"
            )

            # Insert all chunks from this batch
            for (chunk, text), embedding_data in zip(batch, response.data):
                cur.execute(
                    """
                    INSERT INTO documents (embedding, content, meta)
                    VALUES (%s, %s, %s)
                    """,
                    (embedding_data.embedding, text, chunk.model_dump_json()),
                )

            conn.commit()
