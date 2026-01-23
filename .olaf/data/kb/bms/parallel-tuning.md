# BMS Parallel Build Tuning

## Summary
This document explains how to optimize BMS parallel build performance by tuning `forest.parallel` and `build.parallel` settings based on available memory resources. It addresses the tradeoffs between component-level parallelism (forest.parallel) and compilation-level parallelism (build.parallel) to achieve optimal build times.

> **Context**: When building large BMS forests with many components and translation units, proper parallel tuning prevents memory exhaustion while maximizing CPU utilization. Understanding the interaction between these two parameters is critical for efficient CI/CD builds and developer workflows.

---

## Key Concepts

### Core Parameters
- **`build.parallel`**: Maximum number of Make jobs (gcc compilations) running simultaneously within a single component (equivalent to Make's `-j` flag)
- **`forest.parallel`**: Maximum number of BMS components being built simultaneously across the forest
- **Memory Constraint**: `forest.parallel * build.parallel * compilation_memory ≤ available_memory`
- **Dependency Constraint**: Forest parallelism limited by component dependency graph width

### Build Phases (Non-Overlapping)
1. **Code Generation**: Generators run sequentially (gen1, gen2, ...)
2. **Dependency Analysis**: Preprocessor analysis creates `.d` files
3. **Compilation**: Translation units compiled in parallel (`gcc -c`)
4. **Linking**: Final linking phase (`ld`)

### Memory Consumption Model
- Per-component memory: `max(cc.size * build.parallel, ld.size, gen1.size, gen2.size)`
- Total BMS memory: `forest.parallel * max(cc.size * build.parallel, ld.size, gen.size)`
- **Critical**: Linker and generator memory can exceed compilation memory

### Tradeoff Factors
- **High `forest.parallel`, Low `build.parallel`**: Risk of bottlenecks when few components remain, each building slowly
- **Low `forest.parallel`, High `build.parallel`**: Underutilization when dependency graph is wide
- **Dependency Graph Width**: Natural upper limit for effective `forest.parallel` value
- **Translation Unit Count**: Natural upper limit for effective `build.parallel` value

---

## Usage

### Basic Configuration

```bash
# In .bmsrc or component configuration
[forest]
parallel = 6

[build]
parallel = 7
```

### Memory-Based Calculation

**Determine optimal forest.parallel:**
```bash
# Calculate based on largest memory phase
forest.parallel = memtotal / max(cc.size, ld.size, gen1.size, gen2.size)
```

**Derive build.parallel from forest.parallel:**
```bash
# Calculate remaining parallelism for compilations
build.parallel = memtotal / (forest.parallel * cc.size)

# Alternative formula prioritizing forest.parallel:
build.parallel = max(cc.size, ld.size, gen.size) / cc.size
```

### Scenario-Based Guidelines

**Many small components (few .cpp files each):**
- Prioritize `forest.parallel` (e.g., `forest.parallel=20, build.parallel=2`)
- Component count dominates parallelism opportunity

```bash
[forest]
parallel = 20
[build]
parallel = 2
```

**Few large components (many .cpp files each):**
- Prioritize `build.parallel` (e.g., `forest.parallel=2, build.parallel=20`)
- Translation unit count dominates parallelism opportunity

```bash
[forest]
parallel = 2
[build]
parallel = 20
```

**Linear dependency chain:**
- `forest.parallel` has minimal effect (components must build sequentially)
- Maximize `build.parallel` for each component

```bash
[forest]
parallel = 1
[build]
parallel = 42  # Use all available parallelism
```

**Wide dependency graph with balanced components:**
- Use balanced distribution (open question - optimal ratio unknown)
- Example for 42 total parallel jobs:

```bash
# Option 1: Balanced
[forest]
parallel = 6
[build]
parallel = 7

# Option 2: Prioritize component completion
[forest]
parallel = 3
[build]
parallel = 14
```

### Advanced Tuning with Linker Options

**When using lld or mold:**
```bash
# build.parallel also sets --threads=COUNT for linker
[build]
parallel = 8  # Affects both gcc -j and linker threading
```

---

## Common Patterns

### Recommended Tuning Strategy
1. **Prioritize `build.parallel`**: Finish each component quickly to unblock dependents
2. **Use remaining capacity for `forest.parallel`**: Start additional components when resources available
3. **Measure actual memory consumption**: Use process-watcher to profile build phases
4. **Consider linker memory**: Large projects may have `ld.size` >> `cc.size`

### Empirical Starting Points
- **Typical workstation (64GB RAM)**: `forest.parallel=4-8, build.parallel=8-12`
- **Build server (256GB RAM)**: `forest.parallel=12-16, build.parallel=16-20`
- **CI/CD container (16GB RAM)**: `forest.parallel=2-3, build.parallel=4-6`

### Calculation Constraints
```bash
# Upper bounds (don't exceed these)
forest.parallel ≤ dependency_graph_width
build.parallel ≤ translation_unit_count

# Lower bounds (minimum useful values)
forest.parallel ≥ 1
build.parallel ≥ 1

# Combined constraint
forest.parallel * build.parallel ≤ total_parallel_capacity
```

---

## Troubleshooting

### Memory Exhaustion During Build
- **Symptom**: OOM killer terminating gcc/ld processes
- **Diagnosis**: Monitor memory with process-watcher
- **Solution**: Reduce `forest.parallel * build.parallel` product, measure linker memory

### Underutilized CPU Resources
- **Symptom**: Low CPU usage during build
- **Diagnosis**: Check dependency graph bottlenecks, small component sets
- **Solution**: 
  - If many components: Increase `forest.parallel`
  - If few large components: Increase `build.parallel`
  - If linear dependencies: Maximize `build.parallel`, minimize `forest.parallel`

### Build Bottlenecks at End
- **Symptom**: Single slow component blocking completion
- **Cause**: Low `build.parallel` preventing fast component completion
- **Solution**: Increase `build.parallel` at expense of `forest.parallel`

### Inconsistent Build Times
- **Symptom**: Build time varies significantly between runs
- **Cause**: Dependency graph shape causing variable parallelism
- **Solution**: Profile with `bms --statistics`, adjust based on widest graph section

---

## References

- **Related Topics**: Component Build Process, Forest Dependencies, Memory Management, Process Watcher
- **BMS Documentation**: Process Watcher (memory profiling), BMS Statistics (build analysis)
- **Open Questions**: Optimal distribution formula for balanced forests remains under discussion
- **Measurement**: Use process-watcher to measure actual memory consumption per build phase
