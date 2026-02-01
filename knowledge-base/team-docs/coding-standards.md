# 📝 Coding Standards & Best Practices

## General Principles

1. **Write clean, readable code** - Code is read more often than written
2. **Follow the DRY principle** - Don't Repeat Yourself
3. **Keep functions small** - Single responsibility principle
4. **Write tests** - Aim for 80%+ coverage on critical paths
5. **Document complex logic** - Future you will thank present you

## JavaScript/TypeScript Standards

### Naming Conventions
```javascript
// Variables: camelCase
const userName = 'John';
const isActive = true;

// Constants: UPPER_SNAKE_CASE
const MAX_RETRIES = 3;
const API_BASE_URL = 'https://api.example.com';

// Functions: camelCase, verb prefix
function getUserById(id) { }
function calculateTotal(items) { }
async function fetchUserData() { }

// Classes: PascalCase
class UserService { }
class PaymentProcessor { }

// Interfaces/Types: PascalCase with 'I' prefix for interfaces
interface IUserRepository { }
type UserResponse = { };
```

### File Structure
```
src/
├── components/     # React components
├── hooks/          # Custom React hooks
├── services/       # API & business logic
├── utils/          # Helper functions
├── types/          # TypeScript types
└── constants/      # App constants
```

### Code Style
- Use TypeScript for all new code
- Prefer `const` over `let`, never use `var`
- Use arrow functions for callbacks
- Use async/await over .then() chains
- Maximum line length: 100 characters
- Use Prettier for formatting (config in repo)

## Python Standards

### Naming Conventions
```python
# Variables: snake_case
user_name = 'John'
is_active = True

# Constants: UPPER_SNAKE_CASE
MAX_RETRIES = 3
API_BASE_URL = 'https://api.example.com'

# Functions: snake_case
def get_user_by_id(user_id):
    pass

# Classes: PascalCase
class UserService:
    pass
```

### Style Guide
- Follow PEP 8
- Use type hints for function signatures
- Maximum line length: 88 characters (Black default)
- Use Black for formatting
- Use isort for import sorting

## Git Workflow

### Branch Naming
```
feature/ABC-123-add-user-authentication
bugfix/ABC-456-fix-login-redirect
hotfix/ABC-789-security-patch
chore/update-dependencies
```

### Commit Messages
Follow conventional commits:
```
feat: add user authentication flow
fix: resolve login redirect issue
docs: update API documentation
chore: upgrade dependencies
refactor: simplify payment processing
test: add unit tests for user service
```

### Pull Request Guidelines
1. Keep PRs small (< 400 lines ideally)
2. Write a clear description of changes
3. Link to relevant Jira ticket
4. Add screenshots for UI changes
5. Ensure all tests pass
6. Request review from relevant team members

## Code Review Checklist

When reviewing code, check for:
- [ ] Code follows our naming conventions
- [ ] No hardcoded values (use constants/config)
- [ ] Error handling is appropriate
- [ ] Tests cover the changes
- [ ] No security vulnerabilities
- [ ] Performance considerations addressed
- [ ] Documentation updated if needed
