CREATE DATABASE draw_steel;

\c draw_steel;

CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    embedding vector(1536),
    content TEXT NOT NULL,
    meta JSONB,
    fts tsvector GENERATED ALWAYS AS (to_tsvector('english', content)) STORED
);

CREATE INDEX idx_documents_meta ON documents USING GIN (meta);
CREATE INDEX idx_documents_embedding ON documents USING hnsw (embedding vector_cosine_ops);
CREATE INDEX idx_documents_fts ON documents USING GIN (fts);
