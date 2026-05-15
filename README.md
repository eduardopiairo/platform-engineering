# Platform Engineering
Internal Developer Platform

## Architecture

This platform follows the five-plane reference architecture defined by the [Platform Engineering community](https://platformengineering.org/blog/create-your-own-platform-engineering-reference-architectures) (based on hundreds of real-world IDP implementations) and the capability model from the [CNCF Platforms Whitepaper](https://tag-app-delivery.cncf.io/whitepapers/platforms/).

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                         Internal Developer Platform                           │
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────────┐  │
│  │                     1. Developer Control Plane                          │  │
│  │                                                                        │  │
│  │   Backstage Developer Portal                                           │  │
│  │   Service Catalog · Software Templates · TechDocs · Scorecards        │  │
│  └──────────────────────────────────┬─────────────────────────────────────┘  │
│                                     │                                        │
│  ┌──────────────────────────────────▼─────────────────────────────────────┐  │
│  │                   2. Integration & Delivery Plane                       │  │
│  │                                                                        │  │
│  │   GitHub Actions (CI)              ArgoCD (CD / GitOps)               │  │
│  │   build · test · push image        sync · deploy · rollback           │  │
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

Sourced from the [Platform Engineering community reference architecture](https://platformengineering.org/blog/create-your-own-platform-engineering-reference-architectures), modelled on McKinsey's framework and expanded with community tooling patterns.

### 1. Developer Control Plane
The primary interaction layer — where platform users configure, discover, and consume platform capabilities without needing to understand the underlying infrastructure.

| Capability | Tool | Status |
|---|---|---|
| Developer Portal | [Backstage](https://backstage.io) | Planned |
| Service Catalog | Backstage Catalog | Planned |
| Software Templates | Backstage Scaffolder | In progress |
| TechDocs | Backstage TechDocs | Planned |

### 2. Integration & Delivery Plane
Handles the full lifecycle of building artifacts and deploying them: CI pipelines produce container images, GitOps tooling reconciles the desired state into the cluster.

| Capability | Tool | Status |
|---|---|---|
| CI Pipelines | GitHub Actions | In progress |
| Container Registry | GitHub Container Registry | Planned |
| GitOps CD | ArgoCD | Planned |

### 3. Resource Plane
The actual infrastructure — compute, networking, storage, and cloud resources that workloads run on. Provisioned declaratively via GitOps.

| Capability | Tool | Status |
|---|---|---|
| Container Orchestration | Kubernetes | Planned |
| Cloud Resource Provisioning | Crossplane | Planned |

### 4. Monitoring & Logging Plane
Cross-cutting observability across applications and infrastructure: real-time metrics, structured logs, distributed traces, and alerting.

| Capability | Tool | Status |
|---|---|---|
| Metrics | TBD | Not started |
| Logging | TBD | Not started |
| Tracing | TBD | Not started |
| Alerting | TBD | Not started |

### 5. Security Plane
Manages secrets, identity, and policy enforcement to protect sensitive information across all other planes.

| Capability | Tool | Status |
|---|---|---|
| Secrets Management | TBD | Not started |
| Identity & Access | TBD | Not started |
| Policy Enforcement | TBD | Not started |

## CNCF Capability Coverage

The [CNCF Platforms Whitepaper](https://tag-app-delivery.cncf.io/whitepapers/platforms/) defines the following capability domains for an IDP. Coverage status against this platform:

| CNCF Capability | Plane | Tool | Status |
|---|---|---|---|
| Web Portals | Developer Control | Backstage | Planned |
| Golden Path Templates | Developer Control | Backstage Scaffolder | In progress |
| Build & Test Automation | Integration & Delivery | GitHub Actions | In progress |
| Delivery Automation | Integration & Delivery | ArgoCD | Planned |
| Artifact Storage | Integration & Delivery | GitHub Container Registry | Planned |
| Infrastructure Services | Resource | Kubernetes | Planned |
| Data Services | Resource | Crossplane | Planned |
| Observability | Monitoring & Logging | TBD | Not started |
| Identity & Secrets | Security | TBD | Not started |
| Security Services | Security | TBD | Not started |

## Repository Structure

```
platform-engineering/
└── backstage/
    └── templates/
        └── register-service/        # Register Existing Service template
            ├── template.yaml        # Backstage Software Template
            └── skeleton/
                └── catalog-info.yaml
```

## References

- [Platform Engineering community — IDP Reference Architecture](https://platformengineering.org/blog/create-your-own-platform-engineering-reference-architectures)
- [CNCF TAG App Delivery — Platforms Whitepaper](https://tag-app-delivery.cncf.io/whitepapers/platforms/)
- [CNCF Platform Engineering Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/)
- [Backstage](https://backstage.io)
- [ArgoCD](https://argoproj.github.io/cd/)
- [Crossplane](https://www.crossplane.io)
