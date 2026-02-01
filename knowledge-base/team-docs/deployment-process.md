# 🚀 Deployment Process

## Environments

| Environment | URL | Purpose | Deploy Branch |
|-------------|-----|---------|---------------|
| Development | dev.app.company.com | Developer testing | `develop` |
| Staging | staging.app.company.com | QA & UAT | `staging` |
| Production | app.company.com | Live users | `main` |

## Deployment Pipeline

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Commit    │───▶│   Build     │───▶│   Test      │───▶│   Deploy    │
│   Code      │    │   (CI)      │    │   (Auto)    │    │   (CD)      │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

## How to Deploy

### To Development
Automatic on merge to `develop` branch.

### To Staging
1. Create PR from `develop` to `staging`
2. Get approval from Tech Lead
3. Merge PR
4. Deployment starts automatically (10-15 min)
5. Verify in Slack #deployments channel

### To Production
1. Create PR from `staging` to `main`
2. Get approvals from:
   - Tech Lead
   - QA Lead
   - Product Manager
3. Schedule deployment during deployment window (Tue/Thu 2-4 PM)
4. Merge PR
5. Monitor deployment in #deployments channel
6. Verify production health in Datadog

## Rollback Procedure

If something goes wrong in production:

### Quick Rollback (< 5 min)
1. Go to GitHub Actions
2. Find the last successful deployment
3. Click "Re-run deployment"
4. Monitor rollback in Datadog

### Manual Rollback
```bash
# SSH into deployment server (requires VPN)
ssh deploy@prod-server

# Rollback to previous version
./rollback.sh --version=<previous-version>
```

## Deployment Checklist

Before deploying to production:
- [ ] All tests passing in CI
- [ ] QA sign-off received
- [ ] Database migrations reviewed (if any)
- [ ] Feature flags configured
- [ ] Monitoring alerts set up
- [ ] Rollback plan documented
- [ ] Team notified in Slack

## Emergency Contacts

| Role | Name | Phone |
|------|------|-------|
| On-Call Engineer | Rotating | Check PagerDuty |
| DevOps Lead | James Kim | +1-555-0123 |
| Engineering Manager | Sarah Chen | +1-555-0456 |

## Hotfix Process

For critical production issues:
1. Create branch from `main`: `hotfix/ABC-xxx-description`
2. Make minimal fix
3. Get expedited review (ping in #engineering-urgent)
4. Deploy directly to production
5. Backport to `staging` and `develop`
