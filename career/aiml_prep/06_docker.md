# Docker — Zero Se Samajh

> Travel mein padhne ke liye. Assume: tujhe pata hai Docker kya hai (containers), but deep understanding nahi hai.
> Part of career/aiml_prep/ system. See MASTER_PLAN.md for full context.

---

## Pehle Ye Samajh — Problem Kya Hai

Tu Python script likha. Tere laptop pe chal raha hai. Ab colleague ko bheja — uske pe nahi chala. Kyun?

- Tere pe Python 3.11 hai, uske pe 3.9
- Tere pe `pandas` installed hai, uske pe nahi
- Tere pe Windows hai, uske pe Mac
- Tere pe kuch environment variable set hai, uske pe nahi

**Ye "It works on my machine" problem hai.** Har developer ki life mein aata hai.

---

## Docker Ka Solution

Docker bolta hai: "Apna code + sab dependencies + sab settings ek DABBA (container) mein pack kar do. Ye dabba kahi bhi chalega — tere laptop pe, colleague ke laptop pe, server pe, cloud pe. Exactly same."

**Analogy — Tiffin Box:**

Bina Docker: Tu recipe bhej raha hai. "Ye ingredients lao, ye temperature pe pakao, ye bartan use karo." Har kitchen mein result alag aayega.

Docker ke saath: Tu PACKED TIFFIN bhej raha hai. Khana ready hai, garam hai, bartan ke saath hai. Kahi bhi kholo — same taste.

---

## Key Concepts — Ek Ek Karke

### Image

**Image = Recipe/Blueprint.** Ye ek file hai jisme likha hai:
- Kaunsa OS use karna hai (Ubuntu, Alpine)
- Kaunsa software install karna hai (Python, Node)
- Kaunsi files copy karni hain (tera code)
- Kaunsa command run karna hai (python app.py)

Image se tu CONTAINER banata hai. Ek image se 100 containers bana sakta hai — sab identical.

**Analogy:** Image = Cookie cutter. Container = Cookie. Ek cutter se bahut cookies ban sakti hain.

### Container

**Container = Running instance of an image.** Ye ek isolated environment hai jisme tera app chal raha hai.

- Apna khud ka filesystem hai
- Apne khud ke processes hain
- Baaki system se ISOLATED hai
- Lightweight hai (VM se bahut chhota aur fast)

### Container vs VM (Virtual Machine)

```
VM:        [App] [OS] [Hypervisor] [Hardware]
           Poora OS install hota hai. Heavy. Slow to start. GBs of space.

Container: [App] [Docker Engine] [Host OS] [Hardware]
           Sirf app + dependencies. Light. Seconds mein start. MBs of space.
```

**Simple mein:** VM = poora ghar rent karna (kitchen, bedroom, bathroom — sab tera). Container = co-working desk lena (sirf desk tera, baaki shared). Container fast aur cheap hai.

### Registry

**Registry = Image ka storage.** Jaise GitHub code store karta hai, Registry images store karta hai.

- **Docker Hub:** Public registry. Free. `python:3.11`, `node:18`, `ubuntu:22.04` — ye sab yahan se aate hain.
- **AWS ECR (Elastic Container Registry):** Private registry. Teri company ki images yahan store hoti hain. Secure.

### Docker Hub Pe Already Kya Hai

Tu har cheez scratch se nahi banata. Docker Hub pe ready-made images hain:

```
python:3.11      → Python installed hai, seedha use kar
node:18          → Node.js installed hai
ubuntu:22.04     → Ubuntu OS
postgres:15      → PostgreSQL database ready to run
redis:7          → Redis cache ready to run
nginx:latest     → Web server ready to run
```

Tu in images ke UPAR apna code add karta hai. Ye "base image" hai.

---

## Dockerfile — Image Kaise Banti Hai

Dockerfile = ek text file jisme step-by-step instructions hain image banane ke liye.

### Simple Example — Python App

Tere paas ye files hain:
```
my-app/
├── app.py              ← tera Python code
├── requirements.txt    ← dependencies (flask, requests, etc.)
└── Dockerfile          ← ye banayenge
```

```dockerfile
# Step 1: Base image — Python 3.11 wala dabba lo
FROM python:3.11-slim

# Step 2: Container ke andar working directory set karo
WORKDIR /app

# Step 3: Dependencies pehle copy karo (caching ke liye — baad mein samjhayega)
COPY requirements.txt .

# Step 4: Dependencies install karo
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Apna code copy karo
COPY . .

# Step 6: Bata do ki app kaunse port pe chalega
EXPOSE 5000

# Step 7: Container start hone pe ye command run hoga
CMD ["python", "app.py"]
```

### Har Line Ka Matlab

| Command | Kya karta hai | Analogy |
|---------|--------------|---------|
| `FROM` | Base image choose karo | Foundation of building |
| `WORKDIR` | Container mein kaunse folder mein kaam karna hai | `cd /app` jaisa |
| `COPY` | Tere laptop se file container mein copy karo | Pen drive se file copy |
| `RUN` | Container mein command run karo (build time pe) | Terminal mein command type karna |
| `EXPOSE` | Bata do kaunsa port use hoga (documentation) | "Ye darwaza khula hai" |
| `CMD` | Container START hone pe kya run karna hai | "Jab dabba kholo toh ye karo" |

### RUN vs CMD — Important Farak

- `RUN` = IMAGE BANATE WAQT run hota hai. Ek baar. Install karna, setup karna.
- `CMD` = CONTAINER START hone pe run hota hai. Har baar. App chalana.

```dockerfile
RUN pip install flask        ← Image banate waqt Flask install ho gaya (ek baar)
CMD ["python", "app.py"]     ← Har baar container start hone pe app chalega
```

---

## Docker Commands — Ye Yaad Rakh

### Image Banana (Build)

```bash
docker build -t my-app .
```
- `-t my-app` = image ka naam "my-app" rakh
- `.` = current directory mein Dockerfile dhundh

### Container Chalana (Run)

```bash
docker run -p 5000:5000 my-app
```
- `-p 5000:5000` = tere laptop ka port 5000 → container ka port 5000 connect kar
- Ab browser mein `localhost:5000` pe app chalega

### Background Mein Chalana

```bash
docker run -d -p 5000:5000 my-app
```
- `-d` = detached mode (background mein chale, terminal free rahe)

### Chalte Containers Dekhna

```bash
docker ps
```
- Sab running containers dikhata hai (ID, name, port, status)

### Container Rokna

```bash
docker stop <container_id>
```

### Images Dekhna

```bash
docker images
```
- Sab downloaded/built images dikhata hai

### Container Ke Andar Jaana

```bash
docker exec -it <container_id> bash
```
- Container ke andar terminal khul jayega. Debug karne ke liye useful.

### Sab Kuch Clean Karna

```bash
docker system prune -a
```
- Sab stopped containers, unused images hata do. Disk space free karo.

---

## Port Mapping — Ye Samajhna Zaroori Hai

Container ISOLATED hai. Uska apna network hai. Tere laptop se directly access nahi ho sakta.

`-p 5000:5000` ka matlab:

```
Tera Laptop (Host)          Container
Port 5000        ←——→       Port 5000
```

Browser mein `localhost:5000` → Docker forward karta hai container ke port 5000 pe → App ka response wapas aata hai.

Agar `-p 8080:5000` likhe:
```
Tera Laptop                 Container
Port 8080        ←——→       Port 5000
```
Browser mein `localhost:8080` pe access hoga, but container ke andar app 5000 pe chal raha hai.

**Left = tera laptop ka port. Right = container ka port.**

---

## Volumes — Data Persist Karna

**Problem:** Container stop kiya → sab data GAYAB. Container ke andar jo bhi tha — gone. Kyunki container temporary hai.

**Solution:** Volume = tere laptop ka folder container se connect karo. Data laptop pe save hoga, container band ho toh bhi rehega.

```bash
docker run -p 5000:5000 -v /my/data:/app/data my-app
```

```
Tera Laptop                 Container
/my/data         ←——→       /app/data
```

Container ke andar `/app/data` mein jo bhi likhe — tere laptop ke `/my/data` mein save hoga. Container delete karo — data safe hai.

**Kab use hota hai:** Database data, uploaded files, logs — kuch bhi jo persist karna hai.

---

## Docker Compose — Multiple Containers Ek Saath

Real apps mein ek container nahi hota. Typically:
- App container (Python/Node)
- Database container (PostgreSQL/MongoDB)
- Cache container (Redis)
- Reverse proxy (Nginx)

Sab alag alag `docker run` karna painful hai. Docker Compose ek file mein sab define karta hai.

### docker-compose.yml Example

```yaml
version: '3.8'

services:
  app:
    build: .                    # Current directory ka Dockerfile use kar
    ports:
      - "5000:5000"            # Port mapping
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
    depends_on:
      - db                      # Pehle db start ho, phir app

  db:
    image: postgres:15          # Docker Hub se ready-made image
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=mydb
    volumes:
      - db_data:/var/lib/postgresql/data   # Data persist karo

volumes:
  db_data:                      # Named volume define karo
```

### Compose Commands

```bash
docker-compose up              # Sab containers start karo
docker-compose up -d           # Background mein start karo
docker-compose down            # Sab band karo
docker-compose logs app        # App container ke logs dekho
docker-compose build           # Images rebuild karo
```

**Ek command se poora environment up:** `docker-compose up`. App + Database + Cache — sab ready. Ye development mein bahut useful hai.

---

## Environment Variables — Secrets Kaise Dein

Code mein kabhi passwords/API keys hardcode mat kar. Environment variables use kar.

### Dockerfile mein (default values)
```dockerfile
ENV PORT=5000
ENV DEBUG=false
```

### Run time pe override
```bash
docker run -e PORT=8080 -e API_KEY=abc123 my-app
```

### Docker Compose mein
```yaml
services:
  app:
    environment:
      - API_KEY=abc123
      - DATABASE_URL=postgresql://...
```

### .env file se (best practice)
```bash
# .env file (GITIGNORE mein daalna!)
API_KEY=abc123
DATABASE_URL=postgresql://user:pass@db:5432/mydb
```

```yaml
# docker-compose.yml
services:
  app:
    env_file:
      - .env
```

---

## Dockerfile Best Practices

### 1. Layer Caching — Build Fast Karo

Docker har line ko ek "layer" mein cache karta hai. Agar line nahi badli toh cache use hota hai (fast). Badli toh us line se neeche sab rebuild hota hai.

```dockerfile
# ❌ BAD — code change kiya toh dependencies bhi reinstall
COPY . .
RUN pip install -r requirements.txt

# ✅ GOOD — dependencies tab hi reinstall jab requirements.txt badle
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
```

Pehle dependencies copy + install (ye rarely change hoti hain → cached rehta hai). Phir code copy (ye frequently change hota hai). Result: code change pe sirf last step rebuild hota hai. FAST.

### 2. Slim Images Use Karo

```dockerfile
# ❌ python:3.11       → 900MB+ (full OS, unnecessary tools)
# ✅ python:3.11-slim  → 150MB (sirf zaroori cheezein)
# ✅ python:3.11-alpine → 50MB (minimal, but compatibility issues ho sakte hain)
```

Chhoti image = fast download, fast deploy, kam disk use.

### 3. .dockerignore File

Jaise `.gitignore` git ke liye, `.dockerignore` Docker ke liye. Ye files container mein COPY nahi hongi.

```
# .dockerignore
.git
__pycache__
*.pyc
.env
node_modules
.vscode
```

---

## Real World Flow — Tere Project Ke Liye

Tera RAG chatbot project ka Docker flow:

```
1. Dockerfile likh (Python base, dependencies install, code copy)
2. docker build -t rag-chatbot .
3. docker run -p 8000:8000 rag-chatbot
4. Browser: localhost:8000 → App chal raha hai
5. Sab theek → Image push karo ECR pe
6. ECR se ECS/EC2 pe deploy karo (production)
```

```
Development:  Dockerfile → docker build → docker run → test locally
Production:   docker push → ECR → ECS/EC2 → users access karte hain
```

---

## Interview Quick-Fire

**"Docker kya hai?"**
→ Application ko uski sab dependencies ke saath ek isolated container mein pack karna. "It works on my machine" problem solve karta hai. Lightweight, fast, portable.

**"Container vs VM?"**
→ VM mein poora OS install hota hai (heavy, slow, GBs). Container sirf app + dependencies (light, fast, MBs). Container host OS share karta hai.

**"Dockerfile kya hai?"**
→ Step-by-step instructions image banane ke liye. FROM (base), COPY (files), RUN (install), CMD (start command).

**"Docker Compose kya hai?"**
→ Multiple containers ek file mein define karo aur ek command se start karo. App + DB + Cache sab ek saath.

**"Volume kya hai?"**
→ Container ka data persist karna. Host folder ko container folder se connect karo. Container delete ho toh bhi data safe.

**"Image optimize kaise karte ho?"**
→ Slim base images, layer caching (dependencies pehle copy), .dockerignore, multi-stage builds.

---

## Docker → Kubernetes Connection

Docker = ek container run karna. But production mein 100 containers manage karne hain — scaling, healing, networking. That's where Kubernetes comes in.

**Full details:** See `09_aws_cloud_services.md` → Kubernetes section.

**Quick version for Docker interviews:**
- Docker builds and runs containers
- Kubernetes ORCHESTRATES containers at scale
- AWS ECS = AWS-native orchestration (simpler)
- AWS EKS = Kubernetes on AWS (industry standard)
- Tera voice bot: Docker + ECS Fargate (serverless containers)
