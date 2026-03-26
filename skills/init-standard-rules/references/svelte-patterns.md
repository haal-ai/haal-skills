# Svelte Patterns

Detect Svelte-specific patterns: components, stores, actions, and reactivity.

## Search Patterns

### File Roles

```
# Components
*.svelte
*.svelte.ts
*.svelte.js

# Stores
*store.ts
*store.js
*Store.ts
stores/*.ts

# Routes
src/routes/**/*.svelte
src/routes/**/*.ts
+page.svelte
+layout.svelte
+error.svelte
+page.ts
+layout.ts
+page.server.ts

# Actions
*action.ts
actions/*.ts

# Utilities
*utils.ts
lib/*.ts
```

### Component Patterns

```
# Script section
<script lang="ts">
<script>
<script context="module">

# Template syntax
{#if}
{:else}
{/if}
{#each}
{/each}
{#await}
{:then}
{:catch}
{/await}
{#key}
{/key}

# Reactive statements
$: 
$: [variable] = [expression]

# Props
export let [prop]
export let [prop] = [default]

# Slots
<slot />
<slot name="..." />
{@render}

# Events
on:click
on:submit
on:input
on:change
on:[event]

# Bindings
bind:value
bind:checked
bind:this
bind:[property]
```

### Store Patterns

```
# Built-in stores
writable(*)
readable(*)
derived(*, *)
get(*)

# Store subscriptions
$[storeName]  // auto-subscription
[store].subscribe(
[store].set(
[store].update(

# Custom stores
create[Name]Store
function create[Name]Store()

# Store patterns
const [store] = writable(initialValue)
return {
    subscribe: store.subscribe,
    set: store.set,
    update: store.update,
    reset: () => store.set(initialValue)
}
```

### SvelteKit Patterns

```
# Load functions
export const load
export const prerender
export const ssr
export const csr
export const trailingSlash

# Server functions
export const actions
export const GET
export const POST

# Form actions
export const actions = {
    default: async ({ request }) => {}
}

# Hooks
hooks.server.ts
hooks.client.ts
handle
handleError
```

### TypeScript Integration

```
# Type definitions
interface [A-Z]*Props
type [A-Z]*Props

# Generic components
<script lang="ts" generics="T">
```

## Analysis Method

1. **Enumerate components**: Group by .svelte files
2. **Sample stores**: Read 3-5 store files
3. **Detect store patterns**: Check writable/derived/custom
4. **Analyze component structure**: Check props, events, slots
5. **Check SvelteKit patterns**: Routes, load functions, actions

## Reporting Threshold

Report only if:
- ≥3 components with similar props structure
- ≥2 stores with similar patterns
- Inconsistent reactive statement usage

## Insight Template

```
INSIGHT:
  id: SVELTE-[n]
  title: "SVELTE PATTERN: [Pattern] follows consistent structure"
  summary: "[N] [Pattern] files share [markers]."
  confidence: [high|medium|low]
  evidence:
    - path[:line-line] — shows [marker]
  template_markers:
    - props: [list]
    - events: [list]
    - store_type: [writable|derived|custom]
    - reactive_statements: [count]
```

## Command Template

When a Svelte pattern is detected, propose a command:

```yaml
name: "create-svelte-[pattern]"
summary: "Scaffold a new [Pattern] in Svelte"
whenToUse:
  - "Adding a new [pattern] to the codebase"
  - "Need consistent [pattern] structure"
contextValidationCheckpoints:
  - "What is the name of the new component?"
  - "Which route/directory should it belong to?"
steps:
  - name: "Create component"
    description: "Create .svelte file with standard structure"
    codeSnippet: |
      <script lang="ts">
        interface Props {
          // props
        }
        
        export let [prop]: Props['[prop]'];
      </script>
      
      <div class="[name]">
        <!-- template -->
      </div>
      
      <style>
        .[name] {
          /* styles */
        }
      </style>
  - name: "Create store (if needed)"
    description: "Create store for state management"
    codeSnippet: |
      import { writable } from 'svelte/store';
      
      interface [Name]State {
        // state
      }
      
      const initialState: [Name]State = {
        // initial values
      };
      
      function create[Name]Store() {
        const { subscribe, set, update } = writable(initialState);
        
        return {
          subscribe,
          reset: () => set(initialValue),
        };
      }
      
      export const [name]Store = create[Name]Store();
```

## Common Svelte Patterns

| Pattern | Indicators | Standard/Command |
|---------|------------|------------------|
| **Store pattern** | `writable`, `$store`, `subscribe` | Standard: "Svelte store pattern" |
| **Component props** | `export let`, `interface Props` | Command: "create-svelte-component" |
| **Form action** | `export const actions`, `enhance` | Command: "create-form-action" |
| **Load function** | `export const load`, `PageLoad` | Command: "create-page-load" |
| **Custom store** | `createStore`, `subscribe, set, update` | Standard: "Custom store pattern" |
