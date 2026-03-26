# Next.js Patterns

Detect Next.js-specific patterns: App Router, Server Components, API routes, Server Actions, and data fetching.

## Search Patterns

### File Roles

```
# App Router (Next.js 13+)
app/
app/layout.tsx
app/page.tsx
app/*/page.tsx
app/*/layout.tsx
app/*/loading.tsx
app/*/error.tsx
app/*/not-found.tsx
app/api/*/route.ts
app/api/*/route.js

# Pages Router (legacy)
pages/
pages/index.tsx
pages/api/*.ts
pages/_app.tsx
pages/_document.tsx

# Components
components/**/*.tsx
components/**/*.jsx

# Server Actions
actions/**/*.ts
app/*/actions.ts

# Lib/Utils
lib/**/*.ts
utils/**/*.ts
```

### Structure Markers

```
# Server Components (default)
async function Page() {
export default async function

# Client Components
"use client"
"use client";

# Server Actions
"use server"
"use server";

# Metadata
export const metadata
export const generateMetadata

# Dynamic routes
[slug]/
[id]/
[...slug]/
[[...slug]]/
```

### Data Fetching Patterns

```
# Server-side fetching
async function getData() {
await fetch(
fetch('...', { cache: '...' })
fetch('...', { next: { revalidate: ... } })

# Caching
cache: 'no-store'
cache: 'force-cache'
next: { revalidate: 60 }
next: { tags: ['...'] }

# Parallel fetching
Promise.all([
Promise.allSettled([
```

### API Route Patterns

```
# Route handlers (App Router)
export async function GET(request: Request)
export async function POST(request: Request)
export async function PUT(request: Request)
export async function DELETE(request: Request)
export async function PATCH(request: Request)

# Route config
export const dynamic = 'force-dynamic'
export const dynamic = 'force-static'
export const revalidate = 60

# Response helpers
NextResponse.json()
NextResponse.redirect()
new NextResponse()
```

### Server Actions Patterns

```
# Server action definition
"use server"
async function [action]()

# Form actions
<form action={action}>
useActionState
useFormStatus

# Server action in component
async function handleSubmit(formData: FormData) {
    "use server"
}
```

### Client Patterns

```
# Hooks
useState
useEffect
useCallback
useMemo
useRef

# Next.js hooks
useRouter
usePathname
useSearchParams
useParams

# Data fetching (client)
useSWR
useQuery (React Query)
```

### Layout Patterns

```
# Root layout
export default function RootLayout({
    children,
}: {
    children: React.ReactNode
})

# Nested layouts
export default function Layout({
    children,
    params,
}: {
    children: React.ReactNode
    params: { ... }
})

# Parallel routes
export default function Layout({
    children,
    sidebar,
}: {
    children: React.ReactNode
    sidebar: React.ReactNode
})
```

## Analysis Method

1. **Detect router type**: App Router (`app/`) vs Pages Router (`pages/`)
2. **Enumerate pages/routes**: Group by `page.tsx` files
3. **Detect server/client split**: Check `"use client"` usage
4. **Analyze data fetching**: Check `fetch` patterns and caching
5. **Check server actions**: Look for `"use server"`

## Reporting Threshold

Report only if:
- ≥3 pages with similar structure
- Inconsistent server/client patterns
- Mixed data fetching strategies

## Insight Template

```
INSIGHT:
  id: NEXTJS-[n]
  title: "NEXT.JS PATTERN: [Pattern] follows consistent structure"
  summary: "[N] [Pattern] files share [markers]."
  confidence: [high|medium|low]
  evidence:
    - path[:line-line] — shows [marker]
  template_markers:
    - router_type: [App Router|Pages Router]
    - component_type: [Server|Client|Mixed]
    - data_fetching: [Server fetch|Client SWR|React Query]
    - server_actions: [true|false]
```

## Command Template

When a Next.js pattern is detected, propose a command:

```yaml
name: "create-nextjs-[pattern]"
summary: "Scaffold a new [Pattern] in Next.js"
whenToUse:
  - "Adding a new page"
  - "Creating an API route"
contextValidationCheckpoints:
  - "What is the route path?"
  - "Is this a server or client component?"
steps:
  - name: "Create page"
    description: "Create Next.js page component"
    codeSnippet: |
      // app/[route]/page.tsx
      async function Page() {
        const data = await fetch('...');
        
        return (
          <div>
            {/* content */}
          </div>
        );
      }
      
      export default Page;
  - name: "Create API route (if needed)"
    description: "Create API route handler"
    codeSnippet: |
      // app/api/[route]/route.ts
      import { NextResponse } from 'next/server';
      
      export async function GET() {
        return NextResponse.json({ data: [] });
      }
```

## Common Next.js Patterns

| Pattern | Indicators | Standard/Command |
|---------|------------|------------------|
| **Server Component** | `async function`, no `"use client"` | Standard: "Server component pattern" |
| **Client Component** | `"use client"`, `useState` | Standard: "Client component pattern" |
| **API Route** | `export async function GET/POST` | Command: "create-nextjs-api-route" |
| **Server Action** | `"use server"`, form actions | Standard: "Server action pattern" |
| **Parallel routes** | `@sidebar`, multiple slots | Standard: "Parallel routes pattern" |
