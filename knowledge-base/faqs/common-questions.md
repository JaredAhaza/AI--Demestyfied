# ❓ Frequently Asked Questions

## Getting Started

### How do I set up my development environment?
See the [Onboarding Guide](../team-docs/onboarding-guide.md) for step-by-step instructions. Key steps:
1. Install Node.js 18+ and Python 3.10+
2. Clone the repository
3. Run `npm install`
4. Copy `.env.example` to `.env`
5. Run `npm run dev`

### Where do I find the project documentation?
- **Technical docs**: In the `/docs` folder of each repository
- **API docs**: api-docs.internal.company.com
- **Team wiki**: Confluence space "Engineering Team"
- **Architecture**: See [Architecture Overview](../team-docs/architecture-overview.md)

### How do I get access to internal tools?
Submit a request through the IT Portal. Your manager will need to approve. Common tools:
- GitHub: Request @engineering-team access
- Jira: Auto-provisioned with your account
- AWS: Request through IT, requires security training

## Development

### What's our branching strategy?
We use GitFlow:
- `main` - Production code
- `staging` - Pre-production testing
- `develop` - Integration branch
- `feature/*` - New features
- `bugfix/*` - Bug fixes
- `hotfix/*` - Production emergency fixes

### How do I run tests locally?
```bash
# Run all tests
npm test

# Run with coverage
npm run test:coverage

# Run specific test file
npm test -- --grep "UserService"
```

### How do I create a database migration?
```bash
# Create a new migration
npm run migration:create -- --name=add-user-preferences

# Run pending migrations
npm run migration:up

# Rollback last migration
npm run migration:down
```

### What's the code review process?
1. Push your branch and create a PR
2. Add description, link Jira ticket, add screenshots if UI
3. Request review from `@team-reviewers`
4. Address feedback
5. Get at least 1 approval
6. Squash and merge

## Deployment

### How do I deploy to staging?
Merge your PR to the `staging` branch. Deployment is automatic and takes about 10-15 minutes. Monitor in #deployments Slack channel.

### Who can deploy to production?
Production deployments require approval from:
- Tech Lead
- QA Lead  
- Product Manager

Deployments happen during windows: Tuesday and Thursday, 2-4 PM.

### How do I rollback a deployment?
1. Go to GitHub Actions
2. Find the last successful deployment workflow
3. Click "Re-run" on that workflow
4. Notify the team in #engineering

## Troubleshooting

### My local environment won't start
Common fixes:
1. Delete `node_modules` and run `npm install` again
2. Check if Docker is running (required for local DBs)
3. Verify `.env` file has all required variables
4. Check if ports 3000, 5432 are available

### Tests are failing in CI but pass locally
- Check Node version matches CI (18.x)
- Ensure all dependencies are in package.json (not just local)
- Look for timing-dependent tests
- Check for missing environment variables

### I can't connect to the database
1. Ensure Docker is running: `docker ps`
2. Check database container: `docker-compose logs db`
3. Verify connection string in `.env`
4. Try restarting: `docker-compose down && docker-compose up -d`

## Team & Communication

### What meetings do we have?
| Meeting | Frequency | Time | Purpose |
|---------|-----------|------|---------|
| Daily Standup | Daily | 9:30 AM | Quick sync |
| Sprint Planning | Bi-weekly | Monday 10 AM | Plan sprint |
| Retro | Bi-weekly | Friday 3 PM | Improve process |
| Tech Sync | Weekly | Wednesday 2 PM | Technical discussions |

### How do I escalate an issue?
1. **Low urgency**: Post in #engineering Slack
2. **Medium urgency**: DM relevant team lead
3. **High urgency**: Post in #engineering-urgent
4. **Critical (production down)**: Page on-call via PagerDuty

### Where do I report a bug?
1. Check if it's already reported in Jira
2. If not, create a bug ticket with:
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots/logs
   - Environment info
