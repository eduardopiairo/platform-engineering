# Platform Engineering
Internal Developer Platform

## Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                      Internal Developer Platform                     │
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │                  Developer Portal (Backstage)                 │    │
│  │         Service Catalog · Tech Docs · Software Templates     │    │
│  └───────────────────────────┬─────────────────────────────────┘    │
│                              │                                       │
│          ┌───────────────────┼───────────────────┐                  │
│          │                   │                   │                  │
│          ▼                   ▼                   ▼                  │
│  ┌───────────────┐  ┌────────────────┐  ┌────────────────────────┐  │
│  │ GitHub Actions│  │     ArgoCD     │  │ Kubernetes / Crossplane│  │
│  │   Pipelines   │  │   GitOps CD    │  │  Infrastructure as Code│  │
│  │               │  │                │  │                        │  │
│  │ build · test  │  │ sync · deploy  │  │ provision · manage     │  │
│  │ push · notify │  │ rollback       │  │ cloud resources        │  │
│  └───────┬───────┘  └───────┬────────┘  └───────────┬────────────┘  │
│          │                  │                       │               │
│          └──────────────────┴───────────────────────┘               │
│                              │                                       │
│                              ▼                                       │
└─────────────────────────────────────────────────────────────────────┘
```

| Component | Tool | Role |
|---|---|---|
| Developer Portal | [Backstage](https://backstage.io) | Service catalog, TechDocs, and software templates |
| CI Pipeline | GitHub Actions | Build, test, and push container images |
| CD / GitOps | ArgoCD | Syncs manifests from Git to Kubernetes |
| Infrastructure | Kubernetes + Crossplane | Container orchestration and cloud resource provisioning |

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
