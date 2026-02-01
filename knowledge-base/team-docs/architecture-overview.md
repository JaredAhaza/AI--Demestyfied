# 🏗️ System Architecture Overview

## High-Level Architecture

```
                                    ┌─────────────────┐
                                    │   CDN (CloudFront)   │
                                    └────────┬────────┘
                                             │
                    ┌────────────────────────┼────────────────────────┐
                    │                        │                        │
                    ▼                        ▼                        ▼
           ┌───────────────┐       ┌───────────────┐       ┌───────────────┐
           │   Web App     │       │  Mobile App   │       │   Admin       │
           │   (Next.js)   │       │   (React Native)      │   (React)     │
           └───────┬───────┘       └───────┬───────┘       └───────┬───────┘
                   │                       │                       │
                   └───────────────────────┼───────────────────────┘
                                           │
                                    ┌──────▼──────┐
                                    │ API Gateway │
                                    │   (Kong)    │
                                    └──────┬──────┘
                                           │
              ┌────────────────────────────┼────────────────────────────┐
              │                            │                            │
              ▼                            ▼                            ▼
     ┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐
     │ User Service    │         │ Order Service   │         │ Payment Service │
     │ (Node.js)       │         │ (Python)        │         │ (Node.js)       │
     └────────┬────────┘         └────────┬────────┘         └────────┬────────┘
              │                            │                            │
              ▼                            ▼                            ▼
     ┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐
     │   PostgreSQL    │         │   PostgreSQL    │         │   PostgreSQL    │
     │   (Users DB)    │         │   (Orders DB)   │         │   (Payments DB) │
     └─────────────────┘         └─────────────────┘         └─────────────────┘
```

## Core Services

### User Service
- **Tech Stack**: Node.js, Express, TypeScript
- **Database**: PostgreSQL
- **Responsibilities**:
  - User registration and authentication
  - Profile management
  - Session management
  - Role-based access control

### Order Service
- **Tech Stack**: Python, FastAPI
- **Database**: PostgreSQL
- **Responsibilities**:
  - Order creation and management
  - Order status tracking
  - Inventory integration
  - Order history

### Payment Service
- **Tech Stack**: Node.js, Express, TypeScript
- **Database**: PostgreSQL
- **Responsibilities**:
  - Payment processing (Stripe integration)
  - Refund handling
  - Invoice generation
  - Payment history

## Data Flow

### User Registration Flow
1. User submits registration form (Web/Mobile)
2. Request goes through API Gateway
3. User Service validates and creates account
4. Welcome email sent via Email Service
5. User redirected to onboarding

### Order Placement Flow
1. User adds items to cart
2. User initiates checkout
3. Order Service creates pending order
4. Payment Service processes payment
5. On success: Order confirmed, notifications sent
6. On failure: Order cancelled, user notified

## External Integrations

| Service | Purpose | Integration Type |
|---------|---------|------------------|
| Stripe | Payment processing | REST API |
| SendGrid | Email notifications | REST API |
| Twilio | SMS notifications | REST API |
| AWS S3 | File storage | SDK |
| Datadog | Monitoring | Agent |
| Sentry | Error tracking | SDK |

## Security Architecture

- **Authentication**: JWT tokens with refresh rotation
- **Authorization**: Role-based access control (RBAC)
- **Encryption**: TLS 1.3 in transit, AES-256 at rest
- **Secrets**: AWS Secrets Manager
- **WAF**: AWS WAF in front of API Gateway

## Scalability

- **Horizontal scaling**: All services run in Kubernetes
- **Database**: Read replicas for heavy read operations
- **Caching**: Redis for session and frequently accessed data
- **Queue**: RabbitMQ for async processing
