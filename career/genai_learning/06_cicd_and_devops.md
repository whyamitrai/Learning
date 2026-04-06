# CI/CD & DevOps Basics — Ye Seekhna Hai 2 Mahine Mein

> Dekh bhai, tera resume mein CI/CD likha hai Skills mein. But agar interview mein pucha "explain your CI/CD pipeline" aur tu blank gaya toh impression kharab. Ye file tujhe concept + hands-on dono degi. Goal: confidently bol sake "maine ye setup kiya hai" aur GitHub pe proof bhi ho.

---

## CI/CD Kya Hai — Seedhi Baat

**CI = Continuous Integration**
Jab bhi tu code push kare (git push), automatically:
- Code build ho
- Tests run ho
- Agar kuch toota toh turant pata chale

**CD = Continuous Delivery / Deployment**
Build + test pass hone ke baad automatically:
- Code deploy ho staging/production pe
- Bina manual intervention ke

**Analogy**: Soch tu restaurant mein hai. CI = har dish ka taste check hota hai kitchen mein before serving. CD = taste pass hone ke baad waiter automatically table pe le jaata hai. Bina CI/CD ke = chef bana ke seedha table pe rakh deta hai, koi check nahi.

---

## Kyun Chahiye Tujhe?

1. **Resume pe hai** — back it up with real knowledge
2. **Har company mein use hota hai** — code manually deploy karna 2015 ki baat hai
3. **Tera cloud background** — Docker, Terraform, AWS tu jaanta hai. CI/CD inka natural extension hai
4. **Interview mein puchte hain** — "How do you deploy your code?" ka answer "git push aur pray" nahi hona chahiye

---

## Core Concepts

### 1. Pipeline

Pipeline = steps ka sequence jo automatically run hota hai jab trigger hota hai (usually git push).

```
Code Push → Build → Test → Deploy (Staging) → Deploy (Production)
```

Har step ko "stage" ya "job" bolte hain. Ek fail hua toh aage nahi jaata.

### 2. Trigger

Pipeline kab run hoga?
- `push` — jab code push ho
- `pull_request` — jab PR create/update ho
- `schedule` — cron job, daily/weekly
- `manual` — button click se (workflow_dispatch)

### 3. Runner / Agent

Wo machine jis pe pipeline run hota hai.
- GitHub Actions: `ubuntu-latest`, `windows-latest` (GitHub ki machines)
- Jenkins: Tera apna server
- AWS: CodeBuild (managed service)

### 4. Artifacts

Pipeline ke output — build files, test reports, Docker images. Ye save hote hain taaki next stage use kar sake.

### 5. Secrets / Environment Variables

API keys, AWS credentials — ye code mein nahi daalne. Pipeline ke secrets mein store karo, runtime pe inject hote hain.

---

## Tools Landscape — Kya Use Karna Hai

| Tool | Kya Hai | Tere Liye |
|------|---------|-----------|
| **GitHub Actions** | GitHub ka built-in CI/CD | ✅ Ye seekh — free, simple, tere repos mein directly kaam karega |
| Jenkins | Self-hosted CI/CD server | ❌ Abhi nahi — complex setup, companies mein milega toh wahan seekh lena |
| AWS CodePipeline | AWS ka CI/CD | Optional — agar AWS-heavy role hai toh useful |
| GitLab CI | GitLab ka built-in | ❌ Skip — tu GitHub pe hai |
| ArgoCD | Kubernetes GitOps | ❌ Phase 2 — Kubernetes ke baad |

**Decision: GitHub Actions pe focus kar.** Free hai, tere repos mein directly use hoga, aur most startups isi pe hain.

---

## GitHub Actions — Deep Dive

### Kaise Kaam Karta Hai

1. Tu apne repo mein `.github/workflows/` folder banata hai
2. Usme YAML file daalta hai (pipeline definition)
3. Jab trigger condition match hoti hai → GitHub automatically pipeline run karta hai
4. Results "Actions" tab mein dikhte hain

### YAML Structure

```yaml
name: CI Pipeline              # Pipeline ka naam

on:                            # Trigger — kab run hoga
  push:
    branches: [main]           # Sirf main branch pe push hone pe
  pull_request:
    branches: [main]           # Ya PR aane pe

jobs:                          # Jobs — kya kya karega
  build-and-test:              # Job ka naam
    runs-on: ubuntu-latest     # Kis machine pe run hoga
    
    steps:                     # Steps — ek ek kaam
      - name: Checkout code
        uses: actions/checkout@v4    # Pehle code clone kar
      
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Run tests
        run: pytest tests/
      
      - name: Run linter
        run: flake8 src/
```

### Key Terms

- **`on`**: Trigger define karta hai
- **`jobs`**: Parallel ya sequential tasks
- **`runs-on`**: Machine type (runner)
- **`steps`**: Job ke andar ordered steps
- **`uses`**: Pre-built action use karo (marketplace se)
- **`run`**: Shell command run karo
- **`with`**: Action ko parameters do
- **`secrets`**: `${{ secrets.AWS_ACCESS_KEY }}` — encrypted variables

---

## Docker + CI/CD — Ye Combo Important Hai

Tu Docker jaanta hai. CI/CD mein Docker ka role:

1. **Build**: Code se Docker image banao
2. **Push**: Image ko registry mein push karo (ECR, Docker Hub)
3. **Deploy**: Registry se image pull karke run karo (ECS, EC2, etc.)

### Docker Build + Push Pipeline

```yaml
name: Build and Push Docker Image

on:
  push:
    branches: [main]

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      
      - name: Configure AWS Credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ap-south-1
      
      - name: Login to ECR
        id: ecr-login
        uses: aws-actions/amazon-ecr-login@v2
      
      - name: Build and Push
        run: |
          docker build -t my-app .
          docker tag my-app:latest ${{ steps.ecr-login.outputs.registry }}/my-app:latest
          docker tag my-app:latest ${{ steps.ecr-login.outputs.registry }}/my-app:${{ github.sha }}
          docker push ${{ steps.ecr-login.outputs.registry }}/my-app:latest
          docker push ${{ steps.ecr-login.outputs.registry }}/my-app:${{ github.sha }}
```

**Important**: `github.sha` se tag karna — ye har build ka unique identifier hai. Rollback easy hota hai.

---

## Terraform + CI/CD — Infrastructure as Code Pipeline

Tera IaC background hai. CI/CD mein Terraform:

```yaml
name: Terraform Plan and Apply

on:
  pull_request:        # PR pe sirf plan
    branches: [main]
  push:
    branches: [main]   # Merge pe apply

jobs:
  terraform:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      
      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
      
      - name: Terraform Init
        run: terraform init
        working-directory: ./infra
      
      - name: Terraform Plan
        if: github.event_name == 'pull_request'
        run: terraform plan -no-color
        working-directory: ./infra
      
      - name: Terraform Apply
        if: github.ref == 'refs/heads/main' && github.event_name == 'push'
        run: terraform apply -auto-approve
        working-directory: ./infra
```

**Pattern**: PR pe `plan` (review karo kya change hoga), merge pe `apply` (actually change karo). Ye production standard hai.

---

## Environments & Deployment Strategy

### Staging vs Production

```
Code Push → Build → Test → Deploy to Staging → Manual Approval → Deploy to Production
```

- **Staging**: Production jaisa environment but real users nahi. Yahan test karo.
- **Production**: Real users. Yahan directly push = risk.

### Deployment Strategies (Interview mein puchte hain)

**1. Rolling Deployment**
- Purane servers ek ek karke replace hote hain naye version se
- Zero downtime but rollback slow

**2. Blue-Green Deployment**
- Do identical environments: Blue (current) aur Green (new)
- Green pe deploy karo, test karo, traffic switch karo
- Problem aaye toh Blue pe wapas switch — instant rollback
- AWS mein: ECS service update ya ALB target group switch

**3. Canary Deployment**
- Naya version sirf 5-10% traffic ko milta hai pehle
- Monitor karo — sab theek toh gradually 100% pe le jao
- Problem aaye toh sirf 5% users affected

**Interview answer**: "Hum blue-green use karte hain ECS pe. Naya task definition deploy hota hai, health check pass hone ke baad traffic shift hoti hai. Rollback = purani task definition pe wapas."

---

## Monitoring & Logging (CI/CD Ke Baad)

Deploy ke baad kaise pata chalega sab theek hai?

**Health Checks**: Application endpoint jo "I'm alive" bole
```python
@app.get("/health")
def health():
    return {"status": "healthy"}
```

**CloudWatch** (tu already jaanta hai):
- Logs: Application logs
- Metrics: CPU, memory, request count, error rate
- Alarms: Error rate > 5% → alert

**Basic monitoring pipeline mein**:
```yaml
      - name: Health Check
        run: |
          sleep 30  # deployment settle hone do
          curl -f https://staging.myapp.com/health || exit 1
```

---

## Practice Plan — 1 Week

### Day 1-2: Concepts (ye file padh)
- CI/CD kya hai, pipeline, triggers, runners
- GitHub Actions YAML structure samajh
- Docker + CI/CD flow samajh

### Day 3-4: Hands-on Practice 1
**Apne `rag-chatbot-bedrock` repo mein basic CI pipeline add kar:**

```
.github/workflows/ci.yml
```

Kya kare pipeline:
1. Checkout code
2. Setup Python
3. Install dependencies
4. Run linter (flake8)
5. Run tests (pytest) — 2-3 basic tests likh

Ye push kar, Actions tab mein dekh green tick aaye.

### Day 5-6: Hands-on Practice 2
**Docker build + push pipeline add kar:**

1. Dockerfile bana (agar nahi hai)
2. GitHub Actions mein Docker build step add kar
3. ECR pe push karo (ya Docker Hub — free hai)
4. Tagging strategy: `latest` + `github.sha`

### Day 7: Review + Interview Prep
- Apna pipeline explain kar bina dekhe
- Ye questions answer kar:
  - "CI/CD kya hai?"
  - "Tumhara pipeline kya karta hai?"
  - "Blue-green deployment kya hai?"
  - "Secrets kaise manage karte ho pipeline mein?"
  - "Agar deployment fail ho jaaye toh?"

---

## Interview Questions — CI/CD Edition

**"Explain your CI/CD pipeline"**
→ "Jab code push hota hai main branch pe, GitHub Actions trigger hota hai. Pehle code lint hota hai, tests run hote hain. Pass hone pe Docker image build hoti hai, ECR pe push hoti hai with git SHA tag. Phir ECS service update hota hai naye image se. Health check pass hone pe traffic shift hoti hai."

**"How do you handle secrets?"**
→ "GitHub Secrets mein store karte hain — AWS credentials, API keys. Pipeline mein `${{ secrets.KEY_NAME }}` se access hote hain. Code mein kabhi hardcode nahi karte. Local development ke liye .env file with .gitignore."

**"What happens if deployment fails?"**
→ "ECS mein health check fail hone pe automatic rollback hota hai purani task definition pe. Plus pipeline mein health check step hai — fail hone pe alert aata hai aur hum manually previous image tag se redeploy kar sakte hain."

**"Blue-green vs canary?"**
→ "Blue-green mein do full environments hain, traffic ek baar mein switch hoti hai. Canary mein gradually traffic shift hoti hai — 5%, 25%, 100%. Canary safer hai but complex. Hum blue-green use karte hain simplicity ke liye."

---

## Key Takeaways

1. CI/CD = automated build + test + deploy on every code push
2. GitHub Actions = free, simple, directly tere repos mein kaam karega
3. Docker + CI/CD = build image → push to registry → deploy container
4. Terraform + CI/CD = plan on PR, apply on merge
5. Secrets KABHI code mein nahi — pipeline secrets mein store karo
6. Blue-green deployment = safest rollback strategy
7. Health checks + monitoring = deploy ke baad confidence

> Ye file padh, practice kar, aur apne GitHub project mein pipeline add kar. Interview mein "I've set up CI/CD for my projects" confidently bol payega.
