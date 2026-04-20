# AWS Cloud Services — Interview-Ready Guide

> Tu cloud engineer hai. Recruiters WILL ask about AWS services.
> Ye file covers: services you use, services you should know, and how to explain your architecture.
> 🟢 = Easy, 🟡 = Medium, 🔴 = Advanced

---

## 🟢 Tera Production Architecture — Explain Kaise Kare

Tu ye architecture use karta hai (demo solution):
```
CloudFront (CDN) → Web App (frontend)
                → VM (backend) → DynamoDB (database)
                                → S3 (file storage)
```

**Is this production-grade?** Mostly yes. Here's why:

| Component | Service | Production-grade? | Why |
|-----------|---------|-------------------|-----|
| Frontend hosting | CloudFront + S3 | ✅ Yes | CDN = fast globally, S3 = highly available |
| Backend | EC2 (VM) | 🟡 Acceptable | Works, but Lambda or ECS would be more scalable |
| Database | DynamoDB | ✅ Yes | Serverless, auto-scaling, managed by AWS |
| File storage | S3 | ✅ Yes | 99.999999999% durability, industry standard |

**What would make it MORE production-grade:**
- Backend on Lambda (serverless, auto-scales to zero) or ECS (containerized, auto-scales)
- API Gateway in front of backend (rate limiting, auth, monitoring)
- CloudWatch for monitoring + alerts
- WAF (Web Application Firewall) on CloudFront

**Interview mein kaise bolo:**
"I deployed a production application using CloudFront for CDN and static hosting, EC2 for the backend API, DynamoDB for the database, and S3 for file storage. For future improvements, I'd move the backend to Lambda or ECS for better scalability and add API Gateway for rate limiting and monitoring."

---

## 🟢 AWS Services You Use Daily — Quick Reference

### Compute

**Lambda** — Serverless functions. Code upload karo, AWS manage kare. Pay per execution.
- Max timeout: 15 minutes
- Max memory: 10 GB
- Use case: API backends, event processing, chatbot logic
- Tera chatbot isi pe hai

**EC2** — Virtual machines. Full control. Tu manage kare.
- Use case: Long-running processes, custom software, GPU workloads
- Tera demo backend isi pe hai

**ECS (Elastic Container Service)** — Docker containers run karo on AWS.
- Fargate mode: Serverless containers (no EC2 management)
- EC2 mode: Containers on your EC2 instances
- Tera voice bot isi pe hai (Docker + ECS)

**When to use what:**
| Need | Use | Why |
|------|-----|-----|
| Short tasks (<15 min), event-driven | Lambda | Cheapest, auto-scales to zero |
| Containerized apps, long-running | ECS Fargate | No server management, Docker support |
| Full control, GPU, custom OS | EC2 | Maximum flexibility |

### API & Networking

**API Gateway** — Managed API layer. Routes requests, handles auth, rate limiting.
- REST API or WebSocket API
- Integrates with Lambda, EC2, any HTTP endpoint
- Tera chatbot: API Gateway → Lambda → Bedrock

**CloudFront** — CDN (Content Delivery Network). Cache content at edge locations worldwide.
- Static files (HTML, CSS, JS) serve fast globally
- Tera frontend isi pe hai

**VPC (Virtual Private Cloud)** — Tera private network in AWS.
- Public subnets: Internet accessible (web servers)
- Private subnets: No internet access (databases, internal services)
- NAT Gateway: Private subnet se internet access (for updates)

### Storage

**S3 (Simple Storage Service)** — Object storage. Files store karo.
- 99.999999999% durability (11 nines)
- Storage classes: Standard (frequent access), IA (infrequent), Glacier (archive)
- Tera file storage isi pe hai

**DynamoDB** — NoSQL database. Serverless, auto-scaling.
- Key-value + document store
- Single-digit millisecond latency
- Pay per read/write
- Tera chatbot ka data isi mein hai

### AI/ML

**Bedrock** — Serverless AI model access. Multiple models (Claude, Titan, Llama).
- Tera primary AI platform
- Covered in detail in 01_genai_core.md and 02_langchain_rag.md

### Security & Monitoring

**IAM (Identity and Access Management)** — Who can do what.
- Users, Roles, Policies
- Least privilege: Give minimum permissions needed
- Tera kaam: IAM roles for Lambda, ECS tasks

**CloudWatch** — Monitoring + logging + alerts.
- Logs: Lambda logs, API Gateway logs
- Metrics: CPU, memory, request count
- Alarms: "If error rate > 5%, send alert"
- Tera kaam: Lambda monitoring, Bedrock cost tracking

**Secrets Manager** — Store API keys, passwords securely.
- Rotate secrets automatically
- Access from Lambda/ECS via IAM role
- Better than environment variables for production

---

## 🟡 Kubernetes — Basics You Should Know

**Kubernetes (K8s)** = Container orchestration platform. Docker containers ko manage karta hai at scale.

**Docker vs Kubernetes:**
- Docker = ek container run karna
- Kubernetes = 100 containers manage karna (scaling, healing, networking, deployment)

**Analogy:** Docker = ek truck chalana. Kubernetes = poora fleet manage karna (kaunsa truck kahan jaye, koi kharab ho toh replace karo, traffic ke hisaab se trucks badhao).

### Key Concepts

**Pod** — Smallest unit. Ek ya zyada containers ka group.
```
Pod = [Container 1] + [Container 2 (optional)]
```
Usually ek pod mein ek container hota hai.

**Node** — Machine (EC2 instance) jis pe pods run hote hain.

**Cluster** — Multiple nodes ka group. Kubernetes ek cluster manage karta hai.

**Deployment** — "Mujhe 3 copies chahiye is app ki." Kubernetes ensure karta hai hamesha 3 pods running hain. Ek crash ho → automatically naya bana deta hai.

**Service** — Pods ko network pe expose karna. Stable IP/DNS deta hai even if pods change.

**Namespace** — Logical separation. Dev, staging, production alag namespaces mein.

### AWS EKS (Elastic Kubernetes Service)

AWS ka managed Kubernetes. Control plane AWS manage karta hai, tu sirf pods deploy kar.

```
ECS = AWS ka apna container orchestration (simpler, AWS-specific)
EKS = Kubernetes on AWS (industry standard, portable, complex)
```

**Kab ECS, kab EKS:**
| Scenario | Use |
|----------|-----|
| Simple apps, AWS-only, small team | ECS Fargate |
| Complex microservices, multi-cloud, large team | EKS |
| Already using Kubernetes elsewhere | EKS |

**Interview mein:** "I've used ECS with Fargate for my containerized deployments. For larger-scale microservices architectures, I'd use EKS for Kubernetes orchestration. The choice depends on team expertise and whether multi-cloud portability is needed."

### Basic kubectl Commands (Know These)

```bash
kubectl get pods                    # Running pods dekho
kubectl get services                # Services dekho
kubectl get deployments             # Deployments dekho
kubectl describe pod <name>         # Pod ki details
kubectl logs <pod-name>             # Pod ke logs
kubectl apply -f deployment.yaml    # Config apply karo
kubectl scale deployment my-app --replicas=5  # 5 copies bana do
```

### Simple Deployment YAML

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3                    # 3 copies chahiye
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app
        image: my-app:latest     # Docker image
        ports:
        - containerPort: 5000
        resources:
          limits:
            memory: "256Mi"
            cpu: "500m"
```

Ye bolta hai: "my-app ki 3 copies chalao, har ek 256MB memory aur 0.5 CPU use kare, port 5000 pe sune."

---

## 🟡 AWS Architecture Patterns — Interview Mein Puchte Hain

### Serverless Pattern (Tera Chatbot)
```
API Gateway → Lambda → Bedrock
                    → DynamoDB
                    → S3
```
- Zero server management
- Auto-scales to zero (no traffic = no cost)
- Pay per request
- Best for: APIs, chatbots, event processing

### Containerized Pattern (Tera Voice Bot)
```
ALB → ECS Fargate → Bedrock
                  → DynamoDB
```
- Docker containers, managed by AWS
- Auto-scaling based on CPU/memory
- Best for: Long-running services, WebSocket apps, microservices

### Static + API Pattern (Tera Demo App)
```
CloudFront → S3 (frontend)
          → API Gateway → Lambda/EC2 (backend)
                                    → DynamoDB
```
- Frontend: Static files on S3, cached by CloudFront
- Backend: API behind API Gateway
- Best for: Web applications

### Event-Driven Pattern
```
S3 upload → Lambda → Process → DynamoDB
SQS message → Lambda → Process → SNS notification
```
- Events trigger processing
- Fully decoupled
- Best for: File processing, notifications, async workflows

---

## 🟡 AWS Services — Interview Quick-Fire

**"Lambda vs EC2?"**
→ Lambda = serverless, auto-scales, pay per execution, max 15 min. EC2 = full VM, you manage, always running, unlimited time. Lambda for short tasks, EC2 for long-running/custom needs.

**"ECS vs EKS?"**
→ ECS = AWS-native container orchestration, simpler. EKS = managed Kubernetes, industry standard, portable. ECS for AWS-only simple apps, EKS for complex microservices or multi-cloud.

**"S3 storage classes?"**
→ Standard (frequent access), IA (infrequent, cheaper), Glacier (archive, cheapest, slow retrieval). Choose based on access pattern.

**"VPC kya hai?"**
→ Private network in AWS. Public subnets for internet-facing resources, private subnets for internal resources. Security groups for firewall rules.

**"IAM best practices?"**
→ Least privilege (minimum permissions). Use roles not users for services. MFA for console access. Regular access review.

**"CloudWatch kaise use karte ho?"**
→ Logs for debugging, metrics for monitoring, alarms for alerts. I track Lambda execution time, error rates, and Bedrock token usage for cost control.

**"DynamoDB vs RDS?"**
→ DynamoDB = NoSQL, serverless, auto-scaling, key-value. RDS = SQL, managed but not serverless, relational data. DynamoDB for simple access patterns, RDS for complex queries/joins.

**"How do you secure your AWS architecture?"**
→ IAM least privilege, VPC with private subnets, security groups, Secrets Manager for credentials, CloudWatch for monitoring, WAF for web protection, encryption at rest and in transit.

---

## 🔴 Production Best Practices

### Monitoring Stack
```
CloudWatch Logs → Log Groups → Metric Filters → Alarms → SNS → Email/Slack
```
Every production service should have:
- Error rate alarm (>5% → alert)
- Latency alarm (p99 > threshold → alert)
- Cost alarm (daily spend > budget → alert)

### Infrastructure as Code
- ALL infrastructure in Terraform (not console clicks)
- State in S3 with DynamoDB locking
- CI/CD pipeline for infra changes (plan on PR, apply on merge)

### Security Checklist
- [ ] IAM roles with least privilege
- [ ] Secrets in Secrets Manager (not env vars)
- [ ] VPC with private subnets for databases
- [ ] Security groups: minimum ports open
- [ ] Encryption: at rest (S3, DynamoDB, RDS) + in transit (HTTPS)
- [ ] CloudTrail enabled (audit log of all API calls)
- [ ] WAF on public endpoints

**Interview mein:** "In production, I follow AWS Well-Architected Framework principles — security through IAM least privilege and VPC isolation, reliability through multi-AZ deployments, performance through CloudFront caching and auto-scaling, and cost optimization through serverless services and monitoring."
