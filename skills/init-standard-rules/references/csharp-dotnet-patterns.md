# C# / .NET Patterns

Detect C#/.NET-specific patterns: controllers, services, interfaces, dependency injection, and Entity Framework.

## Search Patterns

### File Roles

```
# Controllers
*Controller.cs
*Controllers.cs

# Services
*Service.cs
*Services.cs
*Repository.cs
*Repositories.cs

# DTOs / Models
*Dto.cs
*DTO.cs
*Request.cs
*Response.cs
*Model.cs
*ViewModel.cs

# Interfaces
I*.cs (interface naming convention)
I*Service.cs
I*Repository.cs

# Domain
*Entity.cs
*Aggregate.cs
*ValueObject.cs

# Infrastructure
*DbContext.cs
*Configuration.cs
*Mapping.cs
*Profile.cs (AutoMapper)
```

### Structure Markers

```
# Class declarations
public class
public sealed class
public abstract class
public static class
public partial class

# Interface declarations
public interface I*
interface I*

# Records (C# 9+)
public record
public record struct

# Inheritance
: Controller
: ControllerBase
: DbContext
: IDisposable
: I*

# Generics
where T :
class
struct
new()
```

### Attributes / Decorators

```
# MVC / Web API
[ApiController]
[Route("...")]
[HttpGet]
[HttpPost]
[HttpPut]
[HttpDelete]
[FromBody]
[FromQuery]
[FromRoute]

# Dependency Injection
[Inject]
[FromServices]
IServiceCollection

# Entity Framework
[Key]
[Required]
[MaxLength]
[Column]
[Table]
[NotMapped]
[ForeignKey]
[Index]

# Validation
[Required]
[StringLength]
[Range]
[RegularExpression]

# AutoMapper
[AutoMap]
[IgnoreMap]
```

### Dependency Injection Patterns

```
# Constructor injection
public [A-Z]*(
    private readonly I*

# Service registration
services.AddScoped<I*, *>()
services.AddTransient<I*, *>()
services.AddSingleton<I*, *>()
services.AddHostedService<*>

# Service patterns
IService
IRepository
IUnitOfWork
ILogger<*>
IConfiguration
IOptions<*>
```

### Async Patterns

```
# Async methods
async Task<*>
async Task
async ValueTask<*>

# Async suffix convention
*Async

# CancellationToken
CancellationToken cancellationToken = default
```

### Entity Framework Patterns

```
# DbContext
DbContext
DbSet<*>

# LINQ queries
from * in
where
select
Include(
ThenInclude(
AsNoTracking(
FirstOrDefaultAsync(
ToListAsync(

# Migrations
Add-Migration
Update-Database
HasDbFunction
HasConversion
```

## Analysis Method

1. **Enumerate files by role**: Group by Controller, Service, Repository, etc.
2. **Sample interfaces**: Read 3-5 interfaces per category
3. **Detect DI patterns**: Check constructor injection consistency
4. **Analyze EF patterns**: Check DbContext, DbSet, migrations
5. **Check naming conventions**: Interface I-prefix, Async suffix

## Reporting Threshold

Report only if:
- ≥3 files with same role pattern
- Inconsistent DI registration patterns
- Mixed async/sync patterns in same layer

## Insight Template

```
INSIGHT:
  id: DOTNET-[n]
  title: "DOTNET PATTERN: [Pattern] follows consistent structure"
  summary: "[N] [Pattern] files share [markers]."
  confidence: [high|medium|low]
  evidence:
    - path[:line-line] — shows [marker]
  template_markers:
    - base_class: [name or none]
    - attributes: [list]
    - di_pattern: [constructor/method]
    - async: [true|false]
```

## Command Template

When a C# pattern is detected, propose a command:

```yaml
name: "create-[pattern]"
summary: "Scaffold a new [Pattern] in C#"
whenToUse:
  - "Adding a new [pattern] to the codebase"
  - "Need consistent [pattern] structure"
contextValidationCheckpoints:
  - "What is the name of the new [pattern]?"
  - "Which namespace should it belong to?"
steps:
  - name: "Create interface"
    description: "Create I[Name] interface"
    codeSnippet: |
      public interface I[Name]
      {
          // methods
      }
  - name: "Create implementation"
    description: "Create [Name] class implementing interface"
    codeSnippet: |
      public class [Name] : I[Name]
      {
          private readonly I[Dependency] _dependency;
          
          public [Name](I[Dependency] dependency)
          {
              _dependency = dependency;
          }
      }
  - name: "Register service"
    description: "Add DI registration"
    codeSnippet: |
      services.AddScoped<I[Name], [Name]>();
```

## Common C# Patterns

| Pattern | Indicators | Standard/Command |
|---------|------------|------------------|
| **Repository pattern** | `IRepository`, `DbSet`, `ToListAsync` | Command: "create-repository" |
| **CQRS** | `ICommandHandler`, `IQueryHandler` | Standard: "CQRS pattern" |
| **Unit of Work** | `IUnitOfWork`, `SaveChangesAsync` | Command: "create-unit-of-work" |
| **DTO mapping** | `AutoMapper`, `Profile`, `Map` | Standard: "DTO mapping pattern" |
| **Middleware** | `IMiddleware`, `InvokeAsync` | Command: "create-middleware" |
