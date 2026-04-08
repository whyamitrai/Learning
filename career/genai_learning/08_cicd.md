# CI/CD — Zero Se Samajh

> Pehle Docker (File 07) aur Terraform (File 08) padh. Ye file assume karti hai wo concepts clear hain.

---

## Pehle Ye Samajh — Problem Kya Hai

Tu code likha. Test kiya locally. Sab chal raha hai. Ab production mein daalna hai (deploy karna hai).

**Bina CI/CD ke tu ye karta hai:**
1. Code push kar git pe
2. Server pe SSH kar
3. `git pull` kar
4. Dependencies install kar
5. App restart kar
6. Pray kar ki kuch na toote 🙏

**Problems:**
- Manual hai — har baar same steps, boring, galti hone ka chance
- Agar test nahi kiya aur toota code push kar diya → production down
- Team mein 5 log hain, sab alag tarike se deploy kar rahe hain
- Koi record nahi ki kab kya deploy hua

---

## CI/CD Ka Solution

**CI = Continuous Integration**
Jab bhi tu code push kare → AUTOMATICALLY:
- Code build ho
- Tests run ho
- Agar kuch toota → turant pata chale (push ke 2 min mein)

**CD = Continuous Delivery / Deployment**
Tests pass hone ke baad → AUTOMATICALLY:
- Docker image bane
- Image push ho registry mein
- App deploy ho server pe

**Analogy — Restaurant Kitchen:**

Bina CI/CD: Chef khana banata hai, seedha table pe rakh deta hai. Koi taste check nahi. Customer ko kharab khana mil sakta hai.

CI: Har dish ka taste check hota hai kitchen mein (tests). Kharab hai toh wapas — customer tak nahi pahunchta.

CD: Taste pass → waiter automatically table pe le jaata hai. Chef ko waiter dhundhne ki zaroorat nahi.

CI/CD = **Automated quality check + automated delivery.**

---

## Pipeline Kya Hai

Pipeline = steps ka sequence jo automatically run hota hai.

```
Code Push → Build → Test → Docker Image Bana → Push to Registry → Deploy
```

Har step ko "stage" ya "job" bolte hain. Ek fail hua → aage nahi jaata. Ye safety net hai.

**Analogy — Assembly Line:**
Factory mein car banti hai: frame → engine → paint → quality check → showroom. Ek step fail → car aage nahi jaati. Same concept.

---

## GitHub Actions — Ye Seekh

Bahut saare CI/CD tools hain (Jenkins, GitLab CI, AWS CodePipeline). Tu **GitHub Actions** seekh kyunki:
- Free hai
- Tere GitHub repos mein directly kaam karta hai
- Simple hai
- Most startups isi pe hain

### Kaise Kaam Karta Hai

1. Apne repo mein `.github/workflows/` folder bana
2. Usme ek YAML file daal (pipeline definition)
3. Code push kar
4. GitHub AUTOMATICALLY pipeline run karega
5. Results repo ke "Actions" tab mein dikhenge (green ✅ ya red ❌)

---

## YAML File — Step by Step Samajh

```yaml
# .github/workflows/ci.yml

name: CI Pipeline              # Pipeline ka naam (Actions tab mein dikhega)

on:                            # TRIGGER — kab run hoga?
  push:
    branches: [main]           # Main branch pe push hone pe
  pull_request:
    branches: [main]           # Ya PR aane pe

jobs:                          # JOBS — kya kya karega
  build-and-test:              # Job ka naam (kuch bhi rakh sakta hai)
    runs-on: ubuntu-latest     # Kis machine pe run hoga (GitHub ki free machine)
    
    steps:                     # STEPS — ek ek kaam, order mein
      - name: Checkout code
        uses: actions/checkout@v4    # Step 1: Code clone kar
      
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'     # Step 2: Python install kar
      
      - name: Install dependencies
        run: pip install -r requirements.txt   # Step 3: Dependencies install
      
      - name: Run tests
        run: pytest tests/           # Step 4: Tests run kar
      
      - name: Run linter
        run: flake8 src/             # Step 5: Code quality check
```

### Har Line Ka Matlab

| Keyword | Kya karta hai | Analogy |
|---------|--------------|---------|
| `name` | Pipeline/step ka naam | Label |
| `on` | Kab trigger hoga (push, PR, schedule) | Alarm set karna |
| `jobs` | Kya kya kaam karna hai | To-do list |
| `runs-on` | Kaunsi machine pe chalega | Kaunsa computer use karna hai |
| `steps` | Job ke andar ordered steps | Recipe ke steps |
| `uses` | Pre-built action use karo (marketplace se) | Library import karna |
| `run` | Shell command run karo | Terminal mein type karna |
| `with` | Action ko parameters do | Function ko arguments dena |

### `uses` vs `run` — Important Farak

- `uses` = kisi ne pehle se action bana ke rakha hai, tu use kar. Jaise library import.
  - `actions/checkout@v4` → code clone karta hai
  - `actions/setup-python@v5` → Python install karta hai
  
- `run` = tu apna command likh. Terminal mein jo type karta hai wahi.
  - `run: pip install -r requirements.txt`
  - `run: pytest tests/`

---

## Triggers — Pipeline Kab Chalega

```yaml
on:
  push:                    # Code push hone pe
    branches: [main]       # Sirf main branch pe

  pull_request:            # PR create/update hone pe
    branches: [main]

  schedule:                # Cron job — fixed time pe
    - cron: '0 6 * * *'   # Roz subah 6 baje

  workflow_dispatch:       # Manual — button click se
```

**Most common:** `push` + `pull_request` on main branch.

---

## Secrets — Passwords Kaise Dein

API keys, AWS credentials — ye code mein KABHI nahi daalne. GitHub Secrets mein store karo.

**Kaise set kare:**
1. GitHub repo → Settings → Secrets and variables → Actions
2. "New repository secret" click kar
3. Name: `AWS_ACCESS_KEY_ID`, Value: tera actual key
4. Save

**Pipeline mein use kare:**
```yaml
      - name: Configure AWS
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ap-south-1
```

`${{ secrets.NAME }}` — ye runtime pe actual value se replace ho jaata hai. Code mein ya logs mein kabhi nahi dikhta.

---

## Real Pipeline — Docker Build + Deploy

Ye tera actual project ka pipeline hoga:

```yaml
name: Build and Deploy

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: pytest tests/

  build-and-push:
    needs: test                    # Test pass hone ke BAAD hi chale
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Configure AWS
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ap-south-1
      
      - name: Login to ECR
        id: ecr-login
        uses: aws-actions/amazon-ecr-login@v2
      
      - name: Build and Push Docker Image
        run: |
          docker build -t my-app .
          docker tag my-app:latest ${{ steps.ecr-login.outputs.registry }}/my-app:${{ github.sha }}
          docker push ${{ steps.ecr-login.outputs.registry }}/my-app:${{ github.sha }}
```

### Kya ho raha hai step by step:

```
1. Code push hua main pe
2. Job 1 (test): Python setup → dependencies install → tests run
3. Tests PASS ✅
4. Job 2 (build-and-push): AWS credentials set → ECR login → Docker image build → ECR pe push
5. Image ECR mein safe hai, deploy ke liye ready
```

`needs: test` — ye bolta hai "test job pehle complete ho, tab hi build job chale." Agar test fail → build nahi hoga → broken code deploy nahi hoga.

`github.sha` — har git commit ka unique ID. Image tag mein use karte hain taaki pata rahe kaunsa code kaunsi image mein hai. Rollback easy.

---

## Deployment Strategies — Interview Mein Puchte Hain

### 1. Rolling Deployment
- Purane servers ek ek karke naye version se replace hote hain
- 5 servers hain → pehla update, phir dusra, phir teesra...
- Zero downtime but rollback slow (sab wapas karna padega)

### 2. Blue-Green Deployment
```
Blue (Current - v1) ← Users yahan hain
Green (New - v2)    ← Yahan deploy karo, test karo

Sab theek? Traffic switch karo:
Blue (Old - v1)
Green (Current - v2) ← Ab users yahan hain

Problem aaya? INSTANT rollback:
Blue (Current - v1) ← Users wapas yahan
Green (Broken - v2)
```

- Do identical environments
- Naye pe deploy + test karo
- Traffic ek baar mein switch karo
- Rollback = wapas switch. INSTANT.

### 3. Canary Deployment
```
v1 ← 95% traffic (purana, stable)
v2 ← 5% traffic (naya, testing)

Sab theek? Gradually badhao:
v1 ← 75% traffic
v2 ← 25% traffic

Still theek? Full switch:
v2 ← 100% traffic
```

- Naya version sirf 5% users ko milta hai pehle
- Monitor karo — errors toh nahi aa rahe?
- Gradually 100% pe le jao
- Safest but complex

**Interview answer:** "Hum blue-green use karte hain. Naya version deploy hota hai green environment pe, health check pass hone ke baad traffic switch hoti hai. Problem aaye toh instant rollback blue pe."

---

## Environments — Staging vs Production

```
Code Push → Build → Test → Deploy STAGING → Manual Approval → Deploy PRODUCTION
```

**Staging:** Production jaisa environment but real users NAHI. Yahan test karo. Toot bhi gaya toh koi problem nahi.

**Production:** Real users. Yahan directly push = risk. Hamesha staging se hoke jaana chahiye.

```yaml
  deploy-staging:
    needs: build-and-push
    runs-on: ubuntu-latest
    environment: staging          # GitHub environment (approval set kar sakta hai)
    steps:
      - run: echo "Deploying to staging..."

  deploy-production:
    needs: deploy-staging
    runs-on: ubuntu-latest
    environment: production       # Manual approval required
    steps:
      - run: echo "Deploying to production..."
```

---

## Terraform + CI/CD

Terraform bhi CI/CD mein automate hota hai:

```yaml
  terraform:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: hashicorp/setup-terraform@v3
      
      - name: Terraform Init
        run: terraform init
        working-directory: ./infra
      
      - name: Terraform Plan (PR pe)
        if: github.event_name == 'pull_request'
        run: terraform plan
        working-directory: ./infra
      
      - name: Terraform Apply (merge pe)
        if: github.ref == 'refs/heads/main' && github.event_name == 'push'
        run: terraform apply -auto-approve
        working-directory: ./infra
```

**Pattern:** PR pe sirf `plan` (review karo kya change hoga). Merge pe `apply` (actually change karo). Ye safe hai.

---

## Health Checks — Deploy Ke Baad

Deploy ho gaya. Kaise pata chalega sab theek hai?

```python
# app.py mein ek simple endpoint
@app.get("/health")
def health():
    return {"status": "healthy"}
```

Pipeline mein:
```yaml
      - name: Health Check
        run: |
          sleep 30
          curl -f https://staging.myapp.com/health || exit 1
```

Agar `/health` respond nahi karta → pipeline FAIL → alert aata hai → tu fix karta hai.

---

## Interview Quick-Fire

**"CI/CD kya hai?"**
→ Automated build + test + deploy. Code push karo → automatically test ho, build ho, deploy ho. Manual steps eliminate.

**"Tumhara pipeline kya karta hai?"**
→ Push pe trigger hota hai. Pehle lint + tests. Pass hone pe Docker image build hoti hai, ECR pe push hoti hai with git SHA tag. Phir staging pe deploy, health check, phir production.

**"Secrets kaise manage karte ho?"**
→ GitHub Secrets mein store. Pipeline mein `${{ secrets.KEY }}` se access. Code mein kabhi hardcode nahi. Local ke liye .env + .gitignore.

**"Deployment fail ho jaaye toh?"**
→ Health check fail → automatic rollback purani version pe. Plus alerts set hain. Manual rollback = purani image tag se redeploy.

**"Blue-green vs Canary?"**
→ Blue-green = do environments, traffic ek baar switch, instant rollback. Canary = gradually traffic shift (5% → 25% → 100%), safer but complex.
