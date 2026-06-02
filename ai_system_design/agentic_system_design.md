For FAANG-level AI System Design interviews, agentic systems are significantly harder than traditional RAG because interviewers expect you to think about:

* Planning
* Reasoning
* Multi-agent coordination
* Tool orchestration
* MCP integrations
* Long-running workflows
* Human-in-the-loop
* Memory
* Context Engineering
* Reliability
* Governance
* Evaluation

The biggest mistake candidates make is designing:

```text
User → LLM → Tool → Answer
```

A Staff-level candidate designs:

```text
User
 ↓
Agent Orchestrator
 ↓
Planner
 ↓
Memory Layer
 ↓
Knowledge Layer
 ↓
Tool Layer
 ↓
Execution Layer
 ↓
Validation Layer
 ↓
Human Review (if needed)
 ↓
Final Action
```

---

# Universal Agent Design Framework

Before every design:

## Step 1 Ask Questions

### Business

* What business problem are we solving?
* Fully autonomous or copilot?
* Human approval required?

### Users

* Internal employees?
* External customers?
* Partners?

### Scale

* Daily active users?
* Concurrent sessions?
* Requests/sec?

### Actions

* Read-only?
* Write operations?
* Financial impact?
* Regulatory impact?

### Knowledge

* Internal documents?
* Structured databases?
* APIs?
* External web?

### Reliability

* Can agent make mistakes?
* Human approval threshold?

---

# Scenario 1: Enterprise Legal Contract Intelligence Agent

## Problem Statement

Design an AI agent platform for a multinational corporation.

The system should help legal teams review contracts, identify risks, suggest modifications, negotiate clauses, and create final contract summaries.

The company processes millions of contracts annually across multiple countries.

Design the solution.

---

# Information Candidate Should Ask

### Users?

Possible answer:

```text
Corporate Lawyers
Procurement Teams
Compliance Teams
```

---

### Contract Types?

```text
Vendor Agreements
NDAs
Employment Contracts
Partnership Agreements
```

---

### Regulations?

```text
GDPR
HIPAA
Country Specific Laws
```

---

# Core Challenge

Not a chatbot.

Agent must:

```text
Read
Analyze
Compare
Reason
Suggest
Negotiate
```

---

# Agent Architecture

```text
Contract Upload
      ↓
Orchestrator
      ↓
Planner
      ↓
Specialized Agents
```

---

## Agents

### Clause Extraction Agent

Extract:

```text
Termination
Liability
Indemnity
IP Rights
Confidentiality
```

---

### Risk Analysis Agent

Compare against:

```text
Legal Policies
Historical Contracts
Compliance Rules
```

---

### Negotiation Agent

Suggest:

```text
Replace clause
Reduce liability
Modify payment terms
```

---

### Compliance Agent

Checks:

```text
GDPR
Industry Regulations
Country Laws
```

---

# Tools

### RAG

Knowledge:

```text
Legal Playbooks
Historical Contracts
Policies
```

---

### MCP Tools

```text
Contract Repository
Document Management
Legal Research APIs
```

---

# Human Approval

Mandatory before:

```text
Final Contract Changes
```

---

# Evaluation

### Contract Risk Detection Accuracy

### Clause Extraction F1

### Hallucination Rate

### Legal Expert Agreement Score

---

# What Interviewers Want

Mention:

```text
Agent should never autonomously sign contracts.
```

---

# Scenario 2: Global Supply Chain Autonomous Operations Agent

## Problem Statement

Design an AI operations agent for a global supply chain company managing:

* Warehouses
* Shipping
* Inventory
* Suppliers

across 100+ countries.

The agent should proactively detect issues and take corrective actions.

---

# Clarifying Questions

### Autonomous?

Can it execute actions?

Possible answer:

```text
Yes
```

with approval thresholds.

---

### Data Sources?

```text
ERP
SAP
Oracle
Inventory Systems
IoT Sensors
```

---

# Agent Architecture

## Planner

Receives objective:

```text
Maintain inventory levels
```

---

## Monitoring Agent

Monitors:

```text
Inventory
Lead Times
Demand
Supplier Risk
```

---

## Forecast Agent

Uses:

```text
Historical Sales
Seasonality
Market Trends
```

---

## Supplier Agent

Evaluates:

```text
Supplier Reliability
Cost
Availability
```

---

## Procurement Agent

Creates:

```text
Purchase Orders
```

---

# Tools

```text
SAP
Oracle ERP
Supplier APIs
Logistics APIs
Email Systems
```

---

# Example Flow

Inventory drops.

Agent:

```text
Detects shortage
     ↓
Forecasts impact
     ↓
Finds alternate supplier
     ↓
Creates PO
     ↓
Requests approval
     ↓
Submits order
```

---

# Evaluation

### Stockout Reduction

### Forecast Accuracy

### Procurement Savings

### Agent Success Rate

---

# FAANG Discussion

Need:

```text
Human approval for purchases > $100K
```

or similar threshold.

---

# Scenario 3: Healthcare Clinical Operations Agent

## Problem Statement

Design an AI agent for a healthcare network serving millions of patients.

The system should assist clinicians with diagnosis support, care coordination, scheduling, and treatment recommendations.

---

# Clarifying Questions

### Is it diagnosing?

Or assisting?

Correct answer:

```text
Assisting
Not replacing doctors
```

---

### Data Sources?

```text
EMR/EHR
Lab Results
Medical Imaging
Clinical Notes
Medical Guidelines
```

---

# Agent Architecture

## Patient Context Agent

Builds:

```text
Patient Timeline
```

---

## Medical Knowledge Agent

RAG over:

```text
Clinical Guidelines
Research Papers
Protocols
```

---

## Scheduling Agent

Coordinates:

```text
Appointments
Labs
Follow-Ups
```

---

## Care Coordination Agent

Finds:

```text
Required Specialists
```

---

# Tools

```text
Epic
Cerner
Lab APIs
Imaging Systems
```

---

# Safety Layer

Critical.

```text
No autonomous treatment decisions.
```

Every recommendation:

```text
Evidence
Confidence
Source Citation
```

---

# Evaluation

### Clinical Agreement Score

### Recommendation Accuracy

### Safety Violation Rate

### Physician Acceptance Rate

---

# What Interviewers Want

Human-in-loop.

Always.

---

# Scenario 4: E-Commerce Autonomous Shopping and Operations Agent

## Problem Statement

Design an AI platform for a marketplace with 100 million users.

The agent should:

* Help customers shop
* Manage returns
* Handle refunds
* Resolve disputes
* Recommend products
* Track orders

---

# Clarifying Questions

### Customers only?

Or internal agents too?

Potential answer:

```text
Both
```

---

# Agent Architecture

## Customer Agent

Handles:

```text
Search
Recommendations
Questions
```

---

## Order Agent

Tracks:

```text
Orders
Shipments
Returns
```

---

## Refund Agent

Determines:

```text
Eligibility
Refund Amount
```

---

## Fraud Agent

Checks:

```text
Abuse Patterns
Return Fraud
```

---

# Tools

```text
Order DB
Inventory APIs
Payment APIs
Shipping APIs
CRM
```

---

# Example

User:

```text
My package never arrived.
```

Agent:

```text
Check shipment
     ↓
Check carrier
     ↓
Check history
     ↓
Approve refund
     ↓
Notify customer
```

---

# Evaluation

### Resolution Rate

### Refund Accuracy

### Fraud Detection Precision

### CSAT

---

# Scenario 5: Telecom Network Operations Agent

## Problem Statement

Design an AI agent platform for a telecom provider serving 50 million subscribers.

The system should detect outages, diagnose root causes, coordinate field engineers, and communicate with customers.

---

# Clarification Questions

### Scope?

Only support?

Or network operations?

Assume:

```text
Full network operations
```

---

# Data Sources

```text
Network Telemetry
Tower Metrics
Logs
Incidents
Runbooks
Customer Complaints
```

---

# Multi-Agent Architecture

## Incident Detection Agent

Detects:

```text
Network anomalies
```

---

## Root Cause Agent

Analyzes:

```text
Logs
Topology
Past incidents
```

---

## Field Operations Agent

Schedules:

```text
Technicians
```

---

## Customer Communication Agent

Generates:

```text
Outage notifications
Status updates
```

---

# Knowledge Layer

RAG over:

```text
Runbooks
Network Docs
Historical Incidents
Vendor Manuals
```

---

# Tools

```text
Network Monitoring
ServiceNow
Jira
CRM
GIS Systems
```

---

# Example Flow

```text
Tower Failure
     ↓
Detection Agent
     ↓
Root Cause Agent
     ↓
Runbook Retrieval
     ↓
Field Engineer Assignment
     ↓
Customer Notification
     ↓
Incident Resolution
```

---

# Evaluation

### MTTR Reduction

(Mean Time To Resolution)

### Incident Detection Precision

### False Alarm Rate

### Successful Auto-Resolution %

---

# FAANG-Level Answer Structure (Always Follow)

For any agent design problem, structure your answer as:

```text
1. Clarify Requirements

2. Functional Requirements

3. Non-Functional Requirements

4. Scale Estimation

5. High-Level Architecture

6. Agent Architecture

7. Context Engineering Strategy

8. Memory Design
   - Short-term
   - Long-term
   - Episodic

9. Knowledge Layer
   - RAG
   - Graph RAG
   - Hybrid Search

10. Tool/MCP Layer

11. Planning & Execution

12. Human Approval Layer

13. Security & Governance

14. Evaluation

15. Monitoring

16. Failure Handling

17. Tradeoffs
```

This structure is very close to what Staff/Principal AI Engineers are expected to demonstrate in interviews because it shows that you can design not just an LLM application, but a production-grade autonomous AI system operating at enterprise scale.
