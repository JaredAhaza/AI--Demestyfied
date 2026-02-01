# 🎓 New Team Member Onboarding Guide

Welcome to the team! This guide will help you get started quickly.

## 📋 First Week Checklist

### Day 1: Setup & Access
- [ ] Get your laptop configured
- [ ] Set up email and Slack
- [ ] Request access to GitHub organization
- [ ] Set up development environment (see below)
- [ ] Meet with your buddy/mentor

### Day 2-3: Learn the Basics
- [ ] Read the Product Overview document
- [ ] Complete security training
- [ ] Set up local development environment
- [ ] Run the project locally
- [ ] Review coding standards

### Day 4-5: Start Contributing
- [ ] Pick up a "good first issue" from the backlog
- [ ] Attend team standup meetings
- [ ] Submit your first pull request
- [ ] Schedule 1:1s with key team members

## 🛠️ Development Environment Setup

### Prerequisites
- Node.js 18+ (we use nvm for version management)
- Python 3.10+
- Docker Desktop
- VS Code with recommended extensions

### Steps
1. Clone the main repository: `git clone https://github.com/company/main-app`
2. Install dependencies: `npm install`
3. Copy `.env.example` to `.env` and fill in values
4. Start the dev server: `npm run dev`
5. Run tests: `npm test`

## 📞 Key Contacts

| Role | Name | Slack |
|------|------|-------|
| Engineering Manager | Sarah Chen | @sarah |
| Tech Lead | Marcus Johnson | @marcus |
| Product Manager | Emily Rodriguez | @emily |
| DevOps Lead | James Kim | @james |
| Your Buddy | Assigned Day 1 | TBD |

## 🔧 Tools We Use

| Category | Tool | Purpose |
|----------|------|---------|
| Version Control | GitHub | Code hosting & PRs |
| Project Management | Jira | Tickets & sprints |
| Communication | Slack | Daily chat |
| Documentation | Confluence | Team wiki |
| CI/CD | GitHub Actions | Automated builds |
| Monitoring | Datadog | Production monitoring |
| Design | Figma | UI/UX designs |

## ❓ Common Questions

**Q: Where do I find API documentation?**
A: Check the `/docs/api` folder in the main repo, or visit our internal API portal at api-docs.internal.company.com

**Q: How do I get access to production?**
A: You'll need to complete security training first, then request access through the IT portal. Your manager will approve.

**Q: What's the code review process?**
A: All PRs require at least one approval. Tag the `@team-reviewers` group in your PR. Reviews usually happen within 24 hours.

**Q: How do I deploy to staging?**
A: Push to the `staging` branch, and GitHub Actions will auto-deploy. Takes about 10 minutes.

**Q: Who do I ask about [topic]?**
A: Check the Team Directory in Confluence, or ask in the #help-engineering Slack channel.
