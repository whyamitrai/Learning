# Terraform — Zero Se Samajh

> Travel mein padhne ke liye. Assume: tujhe pata hai cloud kya hai (AWS), but Terraform practically nahi kiya.

---

## Pehle Ye Samajh — Problem Kya Hai

Tu AWS pe kaam karta hai. EC2 instance chahiye. Kya karta hai?

1. AWS Console khol
2. EC2 pe jaa
3. Launch Instance click kar
4. AMI choose kar, instance type choose kar, security group set kar
5. Launch kar

Ab 10 instances chahiye. 10 baar same steps? Aur agar kal sab delete karke dobara banana ho? Phir se 10 baar?

**Aur sabse bada problem:** Tune kya kya click kiya — koi record nahi. Colleague ko batana ho toh screenshots bhejega? Agar galti se kuch delete ho gaya toh yaad hai kya settings thi?

---

## Terraform Ka Solution

Terraform bolta hai: "Apna infrastructure CODE mein likh do. Ek file mein likh do ki kya chahiye — EC2, S3, RDS, VPC — sab. Phir ek command se sab ban jayega. Delete karna ho? Ek command. Dobara banana ho? Ek command."

**Analogy — Shopping List:**

Bina Terraform: Tu dukaan mein jaa ke yaad se saamaan le raha hai. Kuch bhool jayega. Kal phir jaana ho toh phir se yaad karna padega.

Terraform ke saath: Tu SHOPPING LIST likh ke jaa raha hai. Exact same saamaan har baar. List mein change karo → next trip mein automatically adjust.

**Ye "Infrastructure as Code" (IaC) hai.** Infrastructure ko code mein define karna, version control karna (git), aur automate karna.

---

## Key Concepts — Ek Ek Karke

### Provider

**Provider = Kaunsa cloud platform?** Terraform ko batana padta hai ki tu kahan pe infrastructure banana chahta hai.

```hcl
provider "aws" {
  region = "ap-south-1"    # Mumbai region
}
```

AWS, Azure, GCP, DigitalOcean — sab ke providers hain. Tu mostly AWS use karega.

### Resource

**Resource = Kya banana hai?** Ek EC2 instance, ek S3 bucket, ek RDS database — har cheez ek resource hai.

```hcl
resource "aws_instance" "my_server" {
  ami           = "ami-0abcdef1234567890"
  instance_type = "t2.micro"
}
```

Ye padh: "AWS pe ek instance bana, iska naam 'my_server' rakh, ye AMI use kar, t2.micro type ka ho."

### State

**State = Terraform ki diary.** Terraform ek file (`terraform.tfstate`) mein note karta hai ki usne kya kya banaya hai.

Kyun zaroori hai?
- Terraform ko pata hona chahiye ki kya ALREADY exist karta hai
- Agar tu code mein change kare, Terraform compare karta hai: "code mein kya hai vs actually kya hai" → sirf DIFFERENCE apply karta hai
- Bina state ke Terraform har baar sab kuch naya banayega (duplicate resources)

**Analogy:** Tu ek room decorate kar raha hai. State = photo of current room. Naya plan banaya → purani photo se compare karo → sirf jo change karna hai wo karo (sofa hatao, table add karo). Bina photo ke → poora room khaali karke scratch se decorate karna padega.

### Variables

**Variables = Reusable values.** Hardcode mat kar, variables use kar.

```hcl
variable "instance_type" {
  description = "EC2 instance type"
  default     = "t2.micro"
}

resource "aws_instance" "my_server" {
  ami           = "ami-0abcdef1234567890"
  instance_type = var.instance_type    # Variable use kiya
}
```

Ab same code se `t2.micro` bhi bana sakta hai, `t3.large` bhi — sirf variable change karo.

### Output

**Output = Result dikhana.** Resource ban gaya, uski details chahiye (IP address, URL, etc.).

```hcl
output "server_ip" {
  value = aws_instance.my_server.public_ip
}
```

`terraform apply` ke baad terminal mein dikhega: `server_ip = 13.234.56.78`

---

## Terraform File Structure

```
my-project/
├── main.tf          ← Main resources (EC2, S3, RDS, etc.)
├── variables.tf     ← Variables define karo
├── outputs.tf       ← Outputs define karo
├── provider.tf      ← Provider config (AWS, region)
├── terraform.tfvars ← Variable values (GITIGNORE mein daalna!)
└── .gitignore       ← terraform.tfstate, .terraform/, *.tfvars
```

Sab `.tf` files mein likhte hain. Terraform automatically sab `.tf` files ek folder mein padh leta hai.

---

## Terraform Commands — Ye Yaad Rakh

### 1. Init (Setup)
```bash
terraform init
```
- Pehli baar run karo. Provider plugins download karta hai.
- Jaise `npm install` — dependencies install.

### 2. Plan (Preview)
```bash
terraform plan
```
- Dikhata hai KYA HOGA — kya banayega, kya delete karega, kya change karega.
- Actually kuch KARTA nahi. Sirf preview.
- **HAMESHA plan dekho apply se pehle.** Ye safety net hai.

```
+ aws_instance.my_server    ← ye BANAYEGA (green +)
~ aws_s3_bucket.data        ← ye CHANGE karega (yellow ~)
- aws_instance.old_server   ← ye DELETE karega (red -)
```

### 3. Apply (Execute)
```bash
terraform apply
```
- Actually infrastructure banata/change karta hai.
- Pehle plan dikhata hai, phir puchta hai "yes" type karo.
- `terraform apply -auto-approve` → bina puche apply (CI/CD mein use hota hai).

### 4. Destroy (Delete Everything)
```bash
terraform destroy
```
- SAB KUCH delete kar deta hai jo Terraform ne banaya tha.
- Testing ke baad cleanup ke liye useful. Production mein KABHI accidentally mat run karna.

### Flow:
```
init → plan → apply → (changes?) → plan → apply → ... → destroy (cleanup)
```

---

## HCL Syntax — Basic Samajh

HCL = HashiCorp Configuration Language. Terraform ki language.

### Resource Block
```hcl
resource "RESOURCE_TYPE" "LOCAL_NAME" {
  setting1 = "value1"
  setting2 = "value2"
}
```

- `RESOURCE_TYPE` = AWS ka resource type (`aws_instance`, `aws_s3_bucket`)
- `LOCAL_NAME` = tere code mein iska naam (reference ke liye)

### Real Examples

**EC2 Instance:**
```hcl
resource "aws_instance" "web_server" {
  ami           = "ami-0abcdef1234567890"
  instance_type = "t2.micro"
  
  tags = {
    Name = "My Web Server"
  }
}
```

**S3 Bucket:**
```hcl
resource "aws_s3_bucket" "data_bucket" {
  bucket = "my-unique-bucket-name-12345"
  
  tags = {
    Environment = "dev"
  }
}
```

**Security Group:**
```hcl
resource "aws_security_group" "web_sg" {
  name        = "web-sg"
  description = "Allow HTTP and SSH"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]    # Sab se HTTP allow
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["YOUR_IP/32"]    # Sirf tera IP se SSH allow
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"              # Sab outbound allow
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

### Resources Ko Connect Karna

Ek resource dusre ko reference kar sakta hai:

```hcl
resource "aws_instance" "web_server" {
  ami             = "ami-0abcdef1234567890"
  instance_type   = "t2.micro"
  security_groups = [aws_security_group.web_sg.name]   # ← Reference!
}
```

`aws_security_group.web_sg.name` — ye Terraform ko bolta hai "pehle security group bana, phir uska naam yahan use kar." Terraform automatically ORDER samajh leta hai (dependency graph).

---

## Modules — Reusable Code

**Problem:** Har project mein same VPC, same security groups, same setup likh raha hai. Copy-paste.

**Solution:** Module = reusable Terraform code ka package. Ek baar likh, baar baar use kar.

```hcl
module "vpc" {
  source = "terraform-aws-modules/vpc/aws"   # Community module
  
  name = "my-vpc"
  cidr = "10.0.0.0/16"
  
  azs             = ["ap-south-1a", "ap-south-1b"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24"]
}
```

Ye community module use kar raha hai — kisi ne VPC ka poora setup likh diya, tu sirf values de. 100+ lines ka code ek module call mein.

**Analogy:** Functions in programming. Ek baar function likh, baar baar call kar with different arguments.

---

## State Management — Important Concept

### Local State (Default)
```
terraform.tfstate → tere laptop pe save hota hai
```
**Problem:** Team mein kaam kar raha hai. Tere laptop pe state hai, colleague ke pe nahi. Dono apply karein toh conflict.

### Remote State (Production Standard)
```hcl
terraform {
  backend "s3" {
    bucket = "my-terraform-state"
    key    = "prod/terraform.tfstate"
    region = "ap-south-1"
  }
}
```
State S3 mein save hota hai. Team mein sab same state access karte hain. Conflict nahi hota.

**DynamoDB Lock:** S3 ke saath DynamoDB table use karte hain locking ke liye. Ek time pe ek hi banda apply kar sake.

---

## Terraform vs CloudFormation vs CDK

| | Terraform | CloudFormation | CDK |
|---|-----------|---------------|-----|
| By | HashiCorp | AWS | AWS |
| Language | HCL | YAML/JSON | Python/TypeScript |
| Multi-cloud | ✅ AWS, Azure, GCP | ❌ Sirf AWS | ❌ Sirf AWS |
| Community | Bahut bada | AWS only | Growing |
| Learning | Medium | Medium | Easy (if you know Python) |

**Kyun Terraform?** Multi-cloud support. Industry standard. Zyada jobs mein maanga jaata hai.

---

## Common Patterns

### Data Sources (Existing Resources Read Karna)

Kuch already exist karta hai AWS pe (tune manually banaya tha). Terraform se READ kar sakta hai:

```hcl
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]   # Canonical (Ubuntu)
  
  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id   # Dynamic AMI
  instance_type = "t2.micro"
}
```

Hardcode AMI ID nahi karna padta — Terraform latest Ubuntu AMI khud dhundh leta hai.

### Conditional Resources

```hcl
variable "create_bucket" {
  default = true
}

resource "aws_s3_bucket" "data" {
  count  = var.create_bucket ? 1 : 0    # true = bana, false = mat bana
  bucket = "my-bucket"
}
```

### Loops (Multiple Resources)

```hcl
variable "server_names" {
  default = ["web-1", "web-2", "web-3"]
}

resource "aws_instance" "servers" {
  count         = length(var.server_names)
  ami           = "ami-0abcdef1234567890"
  instance_type = "t2.micro"
  
  tags = {
    Name = var.server_names[count.index]
  }
}
```

3 servers ban jayenge: web-1, web-2, web-3. Ek resource block se.

---

## Interview Quick-Fire

**"Terraform kya hai?"**
→ Infrastructure as Code tool. Infrastructure ko code mein define karo, version control karo, ek command se create/update/delete karo. Multi-cloud support.

**"terraform plan vs apply?"**
→ Plan = preview (kya hoga dikhata hai, kuch karta nahi). Apply = actually execute karta hai. Hamesha plan pehle dekho.

**"State kya hai?"**
→ Terraform ki diary — kya banaya hai uska record. State se compare karke sirf changes apply karta hai. Remote state (S3) team mein use hota hai.

**"Module kya hai?"**
→ Reusable Terraform code. Ek baar likh, baar baar use kar with different values. Functions jaisa.

**"Terraform vs CloudFormation?"**
→ Terraform = multi-cloud (AWS, Azure, GCP), HCL language, bigger community. CloudFormation = AWS only, YAML/JSON. Terraform industry standard hai.

**"State file mein conflict aaye toh?"**
→ Remote state S3 mein + DynamoDB locking. Ek time pe ek hi apply kar sakta hai. State file kabhi manually edit mat karo.
