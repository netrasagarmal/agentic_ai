Evaluation is one of the most important and misunderstood areas in GenAI systems.

A common mistake is trying to evaluate everything using a single metric. In reality:

* **LLMs** → evaluate generation quality.
* **RAG systems** → evaluate retrieval + generation.
* **Agents** → evaluate reasoning + tool usage + task completion.

Think of it like this:

```
Traditional ML
Input → Model → Prediction

LLM Application
Input → Prompt → LLM → Response

RAG Application
Input → Retrieval → Context → LLM → Response

Agentic System
Input → Planning → Tool Calls → Reasoning → Actions → Final Answer
```

Each layer introduces new failure modes and therefore new evaluation methods.

---

# 1. Why Evaluation Matters

Without evaluation, you cannot answer:

* Is model version B better than A?
* Did prompt changes improve results?
* Is retrieval working correctly?
* Is the agent using tools properly?
* Is production quality degrading?

Evaluation helps with:

* Model selection
* Prompt optimization
* Regression testing
* Production monitoring
* Continuous improvement

---

# 2. Types of Evaluation

Broadly there are two categories:

## A. Offline Evaluation

Performed on pre-collected datasets.

Example:

```
Question:
"What is the leave policy?"

Expected:
"Employees get 20 annual leaves."

Generated:
"Employees receive 20 paid annual leaves."
```

Compare generated answer against ground truth.

Used during:

* Development
* Benchmarking
* Experimentation

---

## B. Online Evaluation

Performed with real users.

Examples:

* User ratings
* Thumbs up/down
* Success rate
* Click-through rate
* Human review

Used in production.

---
# LLM Evaluation
<details>
<summary>LLM Evaluation</summary>

# LLM Evaluation

When evaluating a pure LLM, we focus on output quality.

---

# Dimension 1: Correctness

Is answer factually correct?

Example

Question:

```
Capital of France?
```

Output:

```
Paris
```

Correct.

---

Metrics:

### Exact Match (EM)

```
Prediction = Paris
Ground Truth = Paris
```

Score = 1

---

### Accuracy

```
Correct Predictions
-------------------
Total Predictions
```

Example:

```
90 correct
100 questions
```

Accuracy = 90%

---

### F1 Score

Useful when answers partially overlap.

Example:

Ground Truth:

```
Paris is the capital of France
```

Prediction:

```
Capital of France is Paris
```

F1 considers token overlap.

---

# Dimension 2: Similarity

Used for open-ended generation.

Example:

Ground Truth:

```
Machine learning enables systems to learn from data.
```

Generated:

```
ML allows computers to learn patterns from data.
```

Meaning same.

Words different.

Need semantic metrics.

---

## BLEU

Measures n-gram overlap.

Widely used in translation.

Formula idea:

```
Generated words
vs
Reference words
```

Higher overlap → higher BLEU.

Range:

```
0 - 1
```

Limitation:

Fails when wording changes.

---

## ROUGE

Measures recall.

Popular in summarization.

Example:

Reference:

```
Cat sat on mat
```

Generated:

```
Cat sat
```

ROUGE checks how much reference content was captured.

---

## METEOR

Improved BLEU.

Considers:

* Synonyms
* Stemming
* Word variations

---

## BERTScore

Uses embeddings.

Instead of word matching:

```
Dog ≈ Puppy
Car ≈ Vehicle
```

Semantic similarity.

Much stronger than BLEU.

---

# Dimension 3: LLM-as-a-Judge

Very common today.

Another LLM evaluates outputs.

Example:

Prompt:

```
Question:
...

Expected:
...

Generated:
...

Rate from 1-5:
Correctness
Completeness
Clarity
```

Judge LLM returns:

```
Correctness: 5
Clarity: 4
```

Advantages:

* Captures meaning
* Scalable
* Works well for long answers

Used heavily in:

* OpenAI Evals
* LangSmith
* DeepEval
* Ragas

---

# Dimension 4: Hallucination

Critical metric.

Question:

```
Who won FIFA 2026?
```

If event hasn't happened:

Good:

```
I don't know.
```

Bad:

```
Brazil won.
```

Hallucination rate:

```
Hallucinated Responses
----------------------
Total Responses
```

Lower is better.

---

# Dimension 5: Toxicity & Safety

Check:

* Harmful content
* Bias
* Hate speech
* PII leakage

Metrics:

* Toxicity score
* Bias score
* Safety score

Tools:

* OpenAI moderation
* Perspective API

</details>
---
# RAG Evaluation
<details>
<summary>RAG Evaluation . . . </summary>

# 4. RAG Evaluation

RAG has TWO parts.

```
User Query
    ↓
Retriever
    ↓
Relevant Chunks
    ↓
LLM
    ↓
Answer
```

Therefore evaluate:

1. Retrieval
2. Generation

Separately.

---

# Retrieval Evaluation

Question:

```
What is maternity leave policy?
```

Relevant chunk:

```
Employees receive 6 months maternity leave.
```

Did retriever fetch it?

---

## Precision@K

Out of K retrieved chunks:

How many are relevant?

Formula:

```
Relevant Retrieved
------------------
K
```

Example:

```
Top 5 chunks
4 relevant
```

Precision@5 = 0.8

---

## Recall@K

Did we retrieve all relevant chunks?

Formula:

```
Relevant Retrieved
------------------
Total Relevant Chunks
```

Example:

```
Retrieved 4
Actually relevant 5
```

Recall = 0.8

---

## Hit Rate

Simpler metric.

```
Was at least one relevant chunk retrieved?
```

Yes → 1

No → 0

---

## MRR (Mean Reciprocal Rank)

Measures ranking quality.

Example:

```
Relevant chunk appears at rank 1
```

Score:

```
1/1 = 1
```

Rank 3:

```
1/3 = 0.33
```

Higher is better.

---

## NDCG

Measures ranking usefulness.

Rewards:

* Relevant documents
* Higher ranking positions

Widely used in search engines.

---

# Generation Evaluation in RAG

Now evaluate answer quality.

---

## Faithfulness

Most important RAG metric.

Question:

```
Leave policy?
```

Context:

```
20 annual leaves.
```

Answer:

```
20 annual leaves.
```

Faithful.

---

Hallucinated answer:

```
25 annual leaves.
```

Not faithful.

---

Faithfulness asks:

```
Does answer come from retrieved context?
```

---

## Answer Relevancy

Does answer actually answer question?

Question:

```
Leave policy?
```

Answer:

```
Company founded in 2001.
```

Irrelevant.

Low score.

---

## Context Precision

Retrieved chunks should be relevant.

Example:

```
Query: Leave policy
```

Retrieved:

```
Leave policy
Office location
CEO biography
```

Only first chunk useful.

Low precision.

---

## Context Recall

Were all necessary chunks retrieved?

Missing important chunk?

Recall decreases.

---

# RAGAS Metrics

Popular framework.

Main metrics:

### Faithfulness

Answer supported by context.

---

### Answer Relevancy

Answer addresses question.

---

### Context Precision

Retrieved chunks relevant.

---

### Context Recall

Retriever found necessary information.

---

### Context Relevancy

Quality of retrieved context.

---

# Example RAG Evaluation

Question:

```
What is annual leave policy?
```

Retrieved:

```
20 annual leaves.
```

Generated:

```
Employees get 20 annual leaves.
```

Scores:

```
Faithfulness = 1.0
Answer Relevancy = 0.95
Context Precision = 1.0
Context Recall = 1.0
```

Excellent retrieval pipeline.

</details>
---
# Agent Evaluation

<details>
<summary>Agent Evaluation ...</summary>


Most difficult.

Why?

Because agents:

* Reason
* Plan
* Call tools
* Loop
* Take actions

Not just generate text.

---

Agent Flow:

```
User
 ↓
Planner
 ↓
Tool Selection
 ↓
Tool Calls
 ↓
Reasoning
 ↓
Final Answer
```

Every stage must be evaluated.

---

# Agent Metric 1: Task Success

Most important.

Example:

Task:

```
Book meeting tomorrow at 10 AM.
```

Agent successfully books.

Score:

```
Success = 1
```

Otherwise:

```
Success = 0
```

---

# Agent Metric 2: Tool Selection Accuracy

Did agent choose correct tool?

Example:

Question:

```
Weather in Mumbai?
```

Correct:

```
Weather API
```

Wrong:

```
SQL Database
```

Tool accuracy decreases.

---

# Agent Metric 3: Tool Call Success Rate

Formula:

```
Successful Calls
----------------
Total Calls
```

Example:

```
95 successful
100 calls
```

95%

---

# Agent Metric 4: Reasoning Quality

Evaluate chain of thought internally (without exposing it).

Judge:

* Logical consistency
* Correct decomposition
* Proper planning

Usually LLM-as-judge.

---

# Agent Metric 5: Efficiency

How expensive is agent?

Metrics:

### Number of tool calls

```
3 calls
vs
20 calls
```

Lower may be better.

---

### Token Usage

```
Input Tokens
Output Tokens
```

---

### Cost

```
$ per task
```

---

### Latency

```
Total execution time
```

---

# Agent Metric 6: Trajectory Evaluation

Trajectory = complete execution path.

Example:

```
Thought
→ Search
→ Retrieve
→ SQL Query
→ Summarize
→ Final Answer
```

Evaluate entire path.

Questions:

* Were steps necessary?
* Were tools used correctly?
* Was plan optimal?

---

# Agent Metric 7: Multi-Step Success

Example:

```
Find cheapest flight
Book hotel
Create itinerary
Email summary
```

Each step scored.

Final score:

```
Completed Steps
---------------
Total Steps
```

---

# 6. Human Evaluation

Gold standard.

Humans rate:

| Metric       | Score |
| ------------ | ----- |
| Correctness  | 1-5   |
| Relevance    | 1-5   |
| Completeness | 1-5   |
| Fluency      | 1-5   |
| Helpfulness  | 1-5   |

Still widely used for production-grade systems.

---

# 7. Production Evaluation Dashboard

For a real-world AI system, monitor:

### LLM Metrics

* Accuracy
* Hallucination Rate
* Toxicity
* Latency
* Cost

### RAG Metrics

* Recall@K
* Precision@K
* Faithfulness
* Context Precision
* Context Recall

### Agent Metrics

* Task Success Rate
* Tool Accuracy
* Tool Failure Rate
* Average Tool Calls
* Latency
* Cost Per Task

</details>
---

# Popular Evaluation Frameworks

* [LangSmith](https://www.langchain.com/langsmith?utm_source=chatgpt.com)
* [RAGAS](https://ragas.io?utm_source=chatgpt.com)
* [DeepEval](https://deepeval.com?utm_source=chatgpt.com)
* [OpenAI Evals](https://github.com/openai/evals?utm_source=chatgpt.com)
* [TruLens](https://www.trulens.org?utm_source=chatgpt.com)
* [Arize Phoenix](https://phoenix.arize.com?utm_source=chatgpt.com)

# Interview-Level Summary

If asked:

**"How do you evaluate LLMs, RAG systems, and AI Agents?"**

A strong answer is:

> LLM evaluation focuses on generation quality using metrics such as accuracy, F1, BLEU, ROUGE, BERTScore, hallucination rate, and LLM-as-a-judge. RAG evaluation separately measures retrieval quality (Precision@K, Recall@K, MRR, NDCG, Hit Rate) and generation quality (faithfulness, answer relevancy, context precision, context recall). Agent evaluation goes beyond text generation and measures task completion, tool selection accuracy, tool success rate, trajectory quality, latency, cost, and multi-step execution success. In production, automated evaluations are typically combined with human evaluation and continuous monitoring to ensure reliability.
