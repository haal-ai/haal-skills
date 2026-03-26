# Angular Patterns

Detect Angular-specific patterns: components, services, modules, directives, pipes, and dependency injection.

## Search Patterns

### File Roles

```
# Components
*.component.ts
*.component.html
*.component.scss
*.component.css
*.component.spec.ts

# Services
*.service.ts
*.service.spec.ts

# Modules
*.module.ts
app.module.ts
feature.module.ts

# Directives
*.directive.ts
*.directive.spec.ts

# Pipes
*.pipe.ts
*.pipe.spec.ts

# Guards
*.guard.ts
*.guard.spec.ts

# Interceptors
*.interceptor.ts

# Models
*.model.ts
*.interface.ts
*.type.ts
*.dto.ts

# Resolvers
*.resolver.ts
```

### Component Patterns

```
# Component decorator
@Component({
  selector: '...',
  templateUrl: '...',
  styleUrls: ['...'],
  standalone: true
})

# Lifecycle hooks
ngOnInit()
ngOnChanges()
ngOnDestroy()
ngAfterViewInit()
ngAfterContentInit()

# Input/Output
@Input()
@Input({ required: true })
@Output()
EventEmitter<*>

# View queries
@ViewChild()
@ViewChildren()
@ContentChild()
@ContentChildren()

# Host bindings
@HostBinding()
@HostListener()
```

### Service Patterns

```
# Service decorator
@Injectable({
  providedIn: 'root'
})

# HTTP patterns
HttpClient
http.get<*>
http.post<*>
http.put<*>
http.delete<*>

# RxJS patterns
Observable<*>
BehaviorSubject<*>
ReplaySubject<*>
Subject<*>
of(*)
from(*)
map(
switchMap(
mergeMap(
catchError(
tap(
finalize(
takeUntil(
```

### Module Patterns

```
# NgModule decorator
@NgModule({
  imports: [...],
  declarations: [...],
  providers: [...],
  exports: [...],
  bootstrap: [...]
})

# Standalone components (Angular 14+)
imports: [CommonModule, RouterModule]
standalone: true

# Feature modules
[Feature]Module
forRoot()
forChild()
```

### Directive Patterns

```
# Directive decorator
@Directive({
  selector: '[...]'
})

# Structural directives
*ngIf
*ngFor
*ngSwitch

# Attribute directives
[ngClass]
[ngStyle]
[class.*]
[style.*]
```

### Routing Patterns

```
# Router configuration
RouterModule.forRoot([])
RouterModule.forChild([])

# Route guards
CanActivate
CanActivateChild
CanDeactivate
Resolve
CanLoad

# Router patterns
router.navigate()
router.navigateByUrl()
ActivatedRoute
snapshot.params
params.subscribe(
```

### Dependency Injection

```
# Constructor injection
constructor(
  private [service]: [Service]
)

# InjectionToken
InjectionToken<*>
provide: [Token]
useValue:
useFactory:
useClass:

# Provider patterns
providedIn: 'root'
providedIn: [Module]
providers: [[Service]]
```

## Analysis Method

1. **Enumerate files by role**: Group by component, service, module, etc.
2. **Sample components**: Read 3-5 components per feature
3. **Detect DI patterns**: Check providedIn vs providers
4. **Analyze RxJS usage**: Check Observable patterns
5. **Check standalone vs NgModule**: Angular version patterns

## Reporting Threshold

Report only if:
- ≥3 components with similar structure
- Inconsistent DI registration patterns
- Mixed standalone/NgModule patterns

## Insight Template

```
INSIGHT:
  id: ANGULAR-[n]
  title: "ANGULAR PATTERN: [Pattern] follows consistent structure"
  summary: "[N] [Pattern] files share [markers]."
  confidence: [high|medium|low]
  evidence:
    - path[:line-line] — shows [marker]
  template_markers:
    - decorator: [@Component|@Injectable|@Directive]
    - standalone: [true|false]
    - inputs: [list]
    - outputs: [list]
    - lifecycle_hooks: [list]
```

## Command Template

When an Angular pattern is detected, propose a command:

```yaml
name: "create-angular-[pattern]"
summary: "Scaffold a new [Pattern] in Angular"
whenToUse:
  - "Adding a new [pattern] to the codebase"
  - "Need consistent [pattern] structure"
contextValidationCheckpoints:
  - "What is the name of the new component/service?"
  - "Which module/feature should it belong to?"
steps:
  - name: "Create component"
    description: "Create component files"
    codeSnippet: |
      @Component({
        selector: 'app-[name]',
        templateUrl: './[name].component.html',
        styleUrls: ['./[name].component.scss'],
        standalone: true,
        imports: [CommonModule]
      })
      export class [Name]Component implements OnInit {
        @Input() [prop]: [Type];
        @Output() [event] = new EventEmitter<[Type]>();
        
        constructor(private [service]: [Service]) {}
        
        ngOnInit(): void {}
      }
  - name: "Create service (if needed)"
    description: "Create service with HttpClient"
    codeSnippet: |
      @Injectable({ providedIn: 'root' })
      export class [Name]Service {
        constructor(private http: HttpClient) {}
        
        get[Items](): Observable<[Item][]> {
          return this.http.get<[Item][]>('/api/[items]');
        }
      }
```

## Common Angular Patterns

| Pattern | Indicators | Standard/Command |
|---------|------------|------------------|
| **Smart/Dumb components** | `@Input`, `@Output`, no services | Standard: "Component hierarchy pattern" |
| **Reactive service** | `BehaviorSubject`, `Observable` | Standard: "Reactive state pattern" |
| **HTTP interceptor** | `HttpInterceptor`, `intercept()` | Command: "create-interceptor" |
| **Route guard** | `CanActivate`, `inject()` | Command: "create-guard" |
| **Facade service** | Multiple services injected | Standard: "Facade pattern" |
