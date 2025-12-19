# Class Notes RAG Chatbot

A **lightweight, local-first RAG chatbot** for querying personal class notes with high accuracy and transparency. The system prioritizes teacher-authoritative content, preserves original notes, and avoids model training in favor of retrieval-based grounding.

---

## ✨ Highlights

* Retrieval-Augmented Generation (RAG)
* Teacher-first accuracy (source-aware retrieval)
* Automated typo & grammar cleanup (non-destructive)
* Deterministic decoding of encoded Bible references
* Local-first & privacy-friendly

---

## 🧠 How It Works

1. **Preprocess notes**

   * Decode encoded Bible links → `Hebrews 2:12`
   * Fix typos & formatting (originals preserved)
   * Tag content as `TEACHER` or `STUDENT`

2. **Index notes**

   * Chunk text (~300–500 words)
   * Embed with metadata (source, lecture, course)
   * Store in a local vector database (Chroma / FAISS)

3. **Answer questions**

   * Retrieve relevant chunks
   * Prefer teacher content
   * Fall back to student notes with explicit uncertainty

---

## 📁 Minimal Structure

```
notes/
  raw/        # original notes
  cleaned/    # typo/grammar fixes
  normalized/ # source tags + decoded refs

scripts/      # preprocessing & indexing
app/          # chatbot entry point
```

---

## 🚀 Quick Start (Conceptual)

```bash
python scripts/decode_bible_refs.py
python scripts/clean_notes.py
python scripts/tag_sources.py
python scripts/build_index.py
python app/chatbot.py
```

---

## 🎯 Philosophy

* Retrieval > fine-tuning for factual recall
* Metadata matters (source reliability)
* Deterministic preprocessing beats LLM guessing
* Transparency over “AI magic”

---

## 📜 License

Personal / educational use. Adapt freely for your own study workflows.
