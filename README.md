# Platform Engineering
Internal Developer Platform

## Architecture

This platform follows the five-plane reference architecture defined by the [Platform Engineering community](https://platformengineering.org/blog/create-your-own-platform-engineering-reference-architectures) and the capability model from the [CNCF Platforms Whitepaper](https://tag-app-delivery.cncf.io/whitepapers/platforms/).

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                         Internal Developer Platform                           │
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────────┐  │
│  │                     1. Developer Control Plane                          │  │
│  │                                                                        │  │
│  │   ┌──────────────────────────┐  ┌──────────────────────────────────┐  │  │
│  │   │  Path 1 · Port           │  │  Path 2 · Backstage               │  │  │
│  │   │  (managed SaaS portal)   │  │  (self-hosted OSS portal)         │  │  │
│  │   │                          │  │                                  │  │  │
│  │   │  Software Catalog        │  │  Software Catalog                │  │  │
│  │   │  Self-service Actions    │  │  Software Templates              │  │  │
│  │   │  Scorecards              │  │  TechDocs                        │  │  │
│  │   │  Automations             │  │  Scorecards (plugins)            │  │  │
│  │   └──────────────────────────┘  └──────────────────────────────────┘  │  │
│  └──────────────────────────────────┬─────────────────────────────────────┘  │
│                                     │                                        │
│  ┌──────────────────────────────────▼─────────────────────────────────────┐  │
│  │                   2. Integration & Delivery Plane                       │  │
│  │                                                                        │  │
│  │   GitHub Actions (CI)                  ArgoCD (CD / GitOps)           │  │
│  │   build · test · push image            sync · deploy · rollback       │  │
│  └────────────────┬─────────────────────────────────┬───────────────────┘  │
│                   │                                 │                        │
│  ┌────────────────▼─────────────────────────────────▼───────────────────┐  │
│  │                       3. Resource Plane                                │  │
│  │                                                                        │  │
│  │   Kubernetes (compute)         Crossplane (cloud resource provisioning)│  │
│  │   clusters · networking · storage · databases                         │  │
│  └────────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│  ┌──────────────────────────────┐   ┌────────────────────────────────────┐  │
│  │  4. Monitoring & Logging     │   │   5. Security Plane                 │  │
│  │                              │   │                                    │  │
│  │  metrics · logs · traces     │   │   secrets · identity · policies    │  │
│  │  alerts · dashboards         │   │   RBAC · audit                     │  │
│  └──────────────────────────────┘   └────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────────────────┘
```

## The Five Planes

### 1. Developer Control Plane

The primary interaction layer where platform users configure, discover, and consume platform capabilities. This platform explores **two portal options in parallel**:

#### Path 1 — Port (managed SaaS)

[Port](https://www.port.io) is a fully managed developer portal with a flexible data model built on blueprints and relations. Teams define their own entity types and self-service actions without managing infrastructure.

| Capability | Port Feature | Notes |
|---|---|---|
| Software Catalog | Blueprints + Entities | Schema-driven, fully customizable |
| Self-service | Actions (GitHub / webhook) | Triggers CI workflows, runbooks |
| Scorecards | Built-in | Service quality and compliance gates |
| Automations | Automation rules | Event-driven, no-code workflows |

#### Path 2 — Backstage (self-hosted OSS)

[Backstage](https://backstage.io) is an open-source developer portal from Spotify, self-hosted and fully extensible via plugins.

| Capability | Backstage Feature | Notes |
|---|---|---|
| Software Catalog | Catalog + `catalog-info.yaml` | Git-backed entity registration |
| Golden Path Templates | Scaffolder | Cookiecutter-style project generation |
| Documentation | TechDocs | Docs-as-code, MkDocs-powered |
| Plugins | Plugin marketplace | Kubernetes, ArgoCD, cost, etc. |

#### Path Comparison

| Dimension | Path 1 · Port | Path 2 · Backstage |
|---|---|---|
| Hosting | SaaS (managed) | Self-hosted |
| Setup time | Minutes | Days to weeks |
| Customization | Blueprint-driven (no-code/low-code) | Plugin-driven (React/TypeScript) |
| Maintenance | Vendor-managed | Platform team owns |
| Cost | Paid subscription | Open source (infra cost only) |
| Best for | Fast time-to-value, smaller platform teams | Full control, large engineering orgs |

### 2. Integration & Delivery Plane

Handles the full lifecycle of building artifacts and deploying them.

| Capability | Tool | Status |
|---|---|---|
| CI Pipelines | GitHub Actions | In progress |
| Container Registry | GitHub Container Registry | Planned |
| GitOps CD | ArgoCD | Planned |

### 3. Resource Plane

Actual infrastructure — compute, networking, storage, and cloud resources. Provisioned declaratively via GitOps.

| Capability | Tool | Status |
|---|---|---|
| Container Orchestration | Kubernetes | Planned |
| Cloud Resource Provisioning | Crossplane | Planned |

### 4. Monitoring & Logging Plane

Cross-cutting observability across applications and infrastructure.

| Capability | Tool | Status |
|---|---|---|
| Metrics | TBD | Not started |
| Logging | TBD | Not started |
| Tracing | TBD | Not started |
| Alerting | TBD | Not started |

### 5. Security Plane

Manages secrets, identity, and policy enforcement across all planes.

| Capability | Tool | Status |
|---|---|---|
| Secrets Management | TBD | Not started |
| Identity & Access | TBD | Not started |
| Policy Enforcement | TBD | Not started |

## Repository Structure

```
platform-engineering/
├── path1-port/                      # Path 1: Port as developer portal
│   └── ...                          # Port blueprints, actions, automations
│
└── path2-backstage/                 # Path 2: Backstage as developer portal
    └── templates/
        └── register-service/        # Register Existing Service template
            ├── template.yaml        # Backstage Software Template
            └── skeleton/
                └── catalog-info.yaml
```

> The current `backstage/` directory maps to Path 2 and will be renamed to `path2-backstage/`.

## References

- [Platform Engineering community — IDP Reference Architecture](https://platformengineering.org/blog/create-your-own-platform-engineering-reference-architectures)
- [CNCF TAG App Delivery — Platforms Whitepaper](https://tag-app-delivery.cncf.io/whitepapers/platforms/)
- [CNCF Platform Engineering Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/)
- [Port — Developer Portal](https://www.port.io)
- [Backstage — Open Source Developer Portal](https://backstage.io)
- [ArgoCD](https://argoproj.github.io/cd/)
- [Crossplane](https://www.crossplane.io)
