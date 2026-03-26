# Spring Boot Patterns

Detect Spring Boot-specific patterns: controllers, services, repositories, Spring Data, and dependency injection.

## Search Patterns

### File Roles

```
# Controllers
*Controller.java
*RestController.java

# Services
*Service.java
*ServiceImpl.java
*Facade.java

# Repositories
*Repository.java
*Dao.java

# Entities
*Entity.java
*Model.java
*Domain.java

# Configuration
application.yml
application.properties
application-*.yml
Application.java
*Application.java
```

### Structure Markers

```
# Spring MVC annotations
@RestController
@Controller
@RequestMapping("/...")
@GetMapping
@PostMapping
@PutMapping
@DeleteMapping
@PatchMapping

# Request/Response
@RequestParam
@PathVariable
@RequestBody
@ResponseBody
@ResponseStatus
@ExceptionHandler

# Service annotations
@Service
@Component
@Facade

# Repository annotations
@Repository

# Configuration
@Configuration
@Bean
@ComponentScan
@EnableAutoConfiguration
@SpringBootApplication
```

### Dependency Injection

```
# Constructor injection
@Autowired
constructor(
    private final [Type]

# Field injection (legacy)
@Autowired
private [Type]

# Lombok + DI
@RequiredArgsConstructor
private final [Type]

# Qualifiers
@Qualifier("...")
@Primary
```

### Spring Data Patterns

```
# Repository interfaces
extends Repository<*>
extends CrudRepository<*>
extends JpaRepository<*>
extends PagingAndSortingRepository<*>

# Query methods
findBy*
findBy*And*
findBy*Or*
findBy*OrderBy*
findBy*Between
findBy*In
findBy*NotIn
findBy*IsNull
findBy*IsNotNull
findBy*Like
findBy*Containing
findBy*StartingWith
findBy*EndingWith

# Custom queries
@Query("...")
@Query(value = "...", nativeQuery = true)
@Modifying
@Transactional
```

### Entity Patterns

```
# JPA annotations
@Entity
@Table(name = "...")
@Id
@GeneratedValue
@Column
@OneToMany
@ManyToOne
@ManyToMany
@OneToOne
@JoinColumn
@JoinTable

# Lombok
@Data
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
```

### Testing Patterns

```
# Test annotations
@SpringBootTest
@WebMvcTest
@DataJpaTest
@MockBean
@SpyBean
@AutoConfigureMockMvc

# Test classes
@ExtendWith(SpringExtension.class)
@TestConfiguration
```

### Security Patterns

```
# Spring Security
@EnableWebSecurity
@Configuration
 SecurityFilterChain
@PreAuthorize
@PostAuthorize
@Secured
@RolesAllowed

# Authentication
@AuthenticationPrincipal
UserDetails
UserDetailsService
```

## Analysis Method

1. **Enumerate controllers**: Group by `@RestController` classes
2. **Sample services**: Read 3-5 `@Service` classes
3. **Detect repository patterns**: Check `JpaRepository` vs `CrudRepository`
4. **Analyze DI style**: Check constructor vs field injection
5. **Check Lombok usage**: Look for `@Data`, `@Builder`

## Reporting Threshold

Report only if:
- ≥3 controllers with similar structure
- Inconsistent DI patterns (constructor vs field)
- Mixed repository types

## Insight Template

```
INSIGHT:
  id: SPRING-[n]
  title: "SPRING BOOT PATTERN: [Pattern] follows consistent structure"
  summary: "[N] [Pattern] files share [markers]."
  confidence: [high|medium|low]
  evidence:
    - path[:line-line] — shows [marker]
  template_markers:
    - controller_style: [@RestController|@Controller]
    - di_style: [constructor|field]
    - repository_type: [JpaRepository|CrudRepository]
    - lombok_usage: [true|false]
```

## Command Template

When a Spring Boot pattern is detected, propose a command:

```yaml
name: "create-spring-[pattern]"
summary: "Scaffold a new [Pattern] in Spring Boot"
whenToUse:
  - "Adding a new REST controller"
  - "Creating a new service"
contextValidationCheckpoints:
  - "What is the resource path?"
  - "What HTTP methods are needed?"
steps:
  - name: "Create controller"
    description: "Create REST controller"
    codeSnippet: |
      @RestController
      @RequestMapping("/api/[resource]")
      @RequiredArgsConstructor
      public class [Name]Controller {
          
          private final [Name]Service service;
          
          @GetMapping
          public List<[Entity]> list() {
              return service.findAll();
          }
      }
  - name: "Create service"
    description: "Create service with repository"
    codeSnippet: |
      @Service
      @RequiredArgsConstructor
      public class [Name]Service {
          
          private final [Name]Repository repository;
          
          public List<[Entity]> findAll() {
              return repository.findAll();
          }
      }
  - name: "Create repository"
    description: "Create Spring Data repository"
    codeSnippet: |
      public interface [Name]Repository extends JpaRepository<[Entity], Long> {
      }
```

## Common Spring Boot Patterns

| Pattern | Indicators | Standard/Command |
|---------|------------|------------------|
| **REST Controller** | `@RestController`, `@GetMapping` | Command: "create-spring-controller" |
| **Service layer** | `@Service`, `@RequiredArgsConstructor` | Command: "create-spring-service" |
| **Repository** | `extends JpaRepository`, query methods | Command: "create-spring-repository" |
| **Constructor DI** | `@RequiredArgsConstructor`, `private final` | Standard: "Constructor injection pattern" |
| **DTO mapping** | `@Mapper`, MapStruct, manual mapping | Standard: "DTO mapping pattern" |
