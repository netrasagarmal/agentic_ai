This is exactly the type of question you can expect in a Staff AI Engineer / Senior AI Architect / FAANG AI System Design interview.

The interviewer usually does **not** give you complete requirements. They intentionally leave gaps because they want to evaluate:

* Requirement gathering
* Tradeoff analysis
* Scale thinking
* Enterprise architecture
* RAG expertise
* Production readiness
* Security and compliance awareness
* Evaluation strategy

---

# How to Approach Any RAG System Design Interview

Before jumping into architecture, follow this framework:

## Step 1: Clarify Requirements

Always start with questions.

Never start drawing architecture immediately.

Typical questions:

### Business Questions

* What problem are we solving?
* Who are the users?
* Internal employees or external customers?
* Expected business outcome?

### Scale Questions

* DAU?
* Peak QPS?
* Number of documents?
* Document growth per day?
* Average document size?

### Latency Questions

* Real-time or asynchronous?
* SLA requirements?
* Response time target?

### Data Questions

* Structured?
* Unstructured?
* PDFs?
* Images?
* Tables?
* Videos?
* Emails?

### Security Questions

* Multi-tenant?
* RBAC?
* PII?
* HIPAA?
* GDPR?
* SOC2?

### Accuracy Questions

* Hallucination tolerance?
* Human review required?
* Explainability requirements?

---

# Generic Thinking Framework

For any RAG system think in layers:

```text
Data Sources
    ↓
Ingestion
    ↓
Parsing
    ↓
Chunking
    ↓
Embedding
    ↓
Vector DB
    ↓
Retrieval
    ↓
Reranking
    ↓
LLM
    ↓
Evaluation
    ↓
Monitoring
```

---

# Scenario 1: Global Banking Knowledge Assistant

## Problem Statement

You are asked to design an AI-powered assistant for a multinational bank.

The assistant should help users find information from banking policies, regulatory documents, compliance manuals, investment products, customer agreements, and internal knowledge bases.

The system should answer user questions accurately and cite sources.

Design the solution.

---

# What Information Should You Ask?

Candidate should ask:

### Users

Who are the users?

Possible answer:

* 100,000 employees
* Compliance officers
* Wealth managers
* Customer support teams

---

### Documents

What document types?

Possible answer:

* PDFs
* Regulatory filings
* Emails
* Word documents
* Scanned documents

---

### Scale

Possible answer:

```text
500 Million documents

50 TB content

100K daily updates

10K concurrent users
```

---

### Compliance

Possible answer:

```text
GDPR
SOX
PCI-DSS
Regional Regulations
```

---

# High-Level Design

## Data Ingestion Layer

Sources:

```text
SharePoint
Confluence
S3
Document Repositories
Email Archives
```

Use:

```text
Kafka
Airflow
Spark
```

for ingestion pipelines.

---

## Parsing Layer

Need support for:

```text
Text
Tables
Forms
Images
Scanned PDFs
```

Use:

* OCR
* Layout-aware extraction
* Document Intelligence

Store:

```text
Raw Document
Parsed Text
Metadata
```

---

## Chunking Strategy

For regulations:

Avoid naive chunking.

Use:

```text
Hierarchical Chunking

Regulation
  Section
      Subsection
           Clause
```

Reason:

Compliance questions require context preservation.

---

## Embedding Strategy

Use:

```text
Title Embedding
Section Embedding
Clause Embedding
```

Store metadata:

```json
{
 "country":"US",
 "department":"Compliance",
 "version":"2026"
}
```

---

## Retrieval

Use Hybrid Search

```text
BM25
+
Dense Retrieval
```

because compliance terms often require exact keyword matching.

Example:

```text
Basel III
IFRS 9
AML
KYC
```

---

## Reranking

Cross Encoder

Top 100

↓

Top 10

---

## Generation

Use:

```text
Context Window Assembly
Citation Generation
Grounded Answering
```

Prompt:

```text
Answer ONLY from context.
If unavailable say:
"I couldn't find supporting evidence."
```

---

## Evaluation

Retrieval:

* Recall@K
* MRR
* NDCG

Generation:

* Faithfulness
* Groundedness
* Hallucination Rate

---

# What FAANG Interviewers Look For

Mention:

```text
Document Versioning
Regulatory Change Tracking
Source Citations
Audit Logs
```

Huge plus points.

---

# Scenario 2: Telecom Customer Support RAG Platform

## Problem Statement

Design an AI assistant for a telecom operator.

The assistant should help resolve customer issues related to:

* Billing
* Network problems
* Device configuration
* Broadband issues
* Roaming services

The organization serves tens of millions of customers.

---

# Clarification Questions

Ask:

### Who uses system?

Possible answer:

```text
Customers
Call Center Agents
Field Engineers
```

---

### Data Sources?

Possible answer:

```text
Knowledge Base
Support Tickets
Network Logs
Product Catalogs
Runbooks
```

---

### Real-time requirements?

Possible answer:

```text
Under 2 seconds
```

---

# Important Observation

This is NOT purely document RAG.

This is:

```text
Knowledge RAG
+
Operational Data RAG
```

---

# Architecture

## Static Knowledge

Store:

```text
FAQs
Product Documents
Support Articles
```

inside Vector DB.

---

## Dynamic Data

Retrieve:

```text
Current Bill
Current Outage
Current Plan
Current Ticket
```

via APIs.

Do NOT vectorize.

---

# Retrieval Flow

User:

```text
Why is my internet slow?
```

Agent first determines:

```text
Need customer-specific data?
```

YES

Call:

```text
Network API
Usage API
Outage API
```

Then combine with RAG.

---

## Architecture

```text
User Query
      ↓
Intent Detection
      ↓
Agent Router
      ↓
Tool Calls
      ↓
Knowledge Retrieval
      ↓
Reranking
      ↓
LLM
```

---

## Security

Need:

```text
Tenant Isolation
PII Redaction
Role-Based Access
```

---

## Evaluation

Additional Metrics:

### Resolution Accuracy

```text
Issue Resolved?
```

---

### Ticket Deflection Rate

```text
How many tickets avoided?
```

---

### First Contact Resolution

Very important telecom KPI.

---

# What Interviewers Want

They want you to realize:

```text
Not everything belongs in Vector DB.
```

Current bill should come from API.

Not embeddings.

This is a common trap.

---

# Scenario 3: Global Manufacturing Copilot

## Problem Statement

Design an AI assistant for a manufacturing company operating 500+ factories worldwide.

The assistant should help engineers troubleshoot machine failures, understand maintenance procedures, and access technical manuals.

---

# Clarification Questions

Ask:

### What data?

Possible answer:

```text
Maintenance Logs
Machine Manuals
Sensor Data
Incident Reports
Images
Videos
CAD Drawings
```

---

### Users?

```text
Plant Engineers
Operators
Maintenance Teams
```

---

### Availability?

```text
24/7
Mission Critical
```

---

# Key Insight

This is a Multimodal RAG system.

---

# Architecture

## Ingestion

Sources:

```text
PDF Manuals
CAD Files
Machine Images
Sensor Streams
Maintenance Reports
```

---

## Storage

### Text

Vector DB

---

### Images

Multimodal Embeddings

---

### Sensor Data

Time-Series Database

```text
InfluxDB
TimescaleDB
```

---

# Query Example

User:

```text
Why is Pump A overheating?
```

System retrieves:

### Manual

```text
Pump overheating section
```

### Historical Incidents

```text
Past failures
```

### Sensor Data

```text
Current temperature
Pressure trend
```

### Images

```text
Similar visual failures
```

---

# Agentic Layer

This becomes:

```text
RAG + Agent
```

Agent may call:

```text
Sensor Service
Maintenance Service
ERP System
Inventory Service
```

---

# Retrieval

Multi-stage retrieval:

```text
Dense Retrieval
      ↓
Metadata Filtering
      ↓
Cross Encoder Rerank
      ↓
Context Compression
```

---

# Evaluation

### Retrieval

* Recall@K
* Precision@K

### Generation

* Faithfulness
* Hallucination Rate

### Business Metrics

* Mean Time To Resolution
* Downtime Reduction
* Maintenance Cost Savings

---

# What Makes a FAANG-Level Answer?

A FAANG-level candidate goes beyond:

```text
PDF
→ Embedding
→ Vector DB
→ GPT
```

and discusses:

### Data Layer

* Incremental indexing
* CDC
* Versioning
* Deduplication

### Retrieval Layer

* Hybrid Search
* Query Rewriting
* Multi-query Retrieval
* Metadata Filtering
* Reranking

### Generation Layer

* Context Compression
* Citation Generation
* Structured Outputs

### Enterprise Layer

* RBAC
* Multi-tenancy
* Audit Logs
* Encryption

### Reliability Layer

* Caching
* Fallback Models
* Circuit Breakers
* Retry Logic

### Evaluation Layer

* Offline Evaluation
* Online Evaluation
* Human Feedback
* Drift Detection

### Monitoring Layer

* Latency
* Cost
* Hallucinations
* Retrieval Quality
* User Satisfaction

If you can systematically walk through **Requirements → Scale → Data → Ingestion → Retrieval → Generation → Security → Evaluation → Monitoring → Tradeoffs**, you'll perform at the level expected for Senior/Staff AI System Design interviews at large technology companies.
