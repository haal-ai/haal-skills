# Angular Compatibility Matrix Reference

This document provides comprehensive compatibility information for Angular migrations.

## Official Angular Version Support

**Source**: [https://angular.dev/reference/versions](https://angular.dev/reference/versions)

### Angular 13
- **Node.js**: 16.14.0 - 16.x
- **npm**: 8.x
- **TypeScript**: 4.4 - 4.5
- **RxJS**: 7.4+
- **Status**: No longer supported

### Angular 14
- **Node.js**: 14.20.0 - 16.x
- **npm**: 8.x
- **TypeScript**: 4.6 - 4.8
- **RxJS**: 7.4+
- **Status**: No longer supported

### Angular 15
- **Node.js**: 14.20.0, 16.13.0 - 16.x, 18.10.0 - 18.x
- **npm**: 8.x
- **TypeScript**: 4.8 - 4.9
- **RxJS**: 7.5+
- **Status**: No longer supported

### Angular 16
- **Node.js**: 16.14.0 - 16.x, 18.10.0 - 18.x
- **npm**: 8.x - 9.x
- **TypeScript**: 4.9 - 5.0
- **RxJS**: 7.5+
- **Status**: No longer supported

### Angular 17 ⚠️ Critical Node.js Upgrade
- **Node.js**: **18.19.1+ - 18.x**, 20.11.1 - 20.x
- **npm**: 9.x - 10.x
- **TypeScript**: 5.2 - 5.3
- **RxJS**: 7.8+
- **Status**: No longer supported
- **CRITICAL**: Node.js 16 no longer supported - upgrade required

### Angular 18
- **Node.js**: 18.19.1 - 18.x, 20.11.1 - 20.x
- **npm**: 9.x - 10.x
- **TypeScript**: 5.4 - 5.5
- **RxJS**: 7.8+
- **Status**: No longer supported

### Angular 19
- **Node.js**: 18.19.1 - 18.x, 20.11.1 - 20.x, 22.11.0 - 22.x
- **npm**: 9.x - 10.x
- **TypeScript**: 5.4 - 5.6
- **RxJS**: 7.8+
- **Status**: Active LTS

### Angular 20 ⚠️ Critical Node.js Upgrade
- **Node.js**: **20.19.0+ - 20.x**, 22.12.0 - 22.x
- **npm**: 10.x
- **TypeScript**: 5.7+
- **RxJS**: 7.8+
- **Status**: Active
- **CRITICAL**: Node.js 18 no longer supported - upgrade required

## Key Migration Upgrade Points

### Node.js Upgrade Requirements
1. **Angular 13-16**: Node.js 16.14.0+
2. **Angular 17-19**: Node.js 18.19.1+ (CRITICAL UPGRADE)
3. **Angular 20+**: Node.js 20.19.0+ or 22.12.0+ (CRITICAL UPGRADE)

### Angular Material MDC Migration
- **Angular 17+**: Material Design Components (MDC) migration required
- Use: `ng generate @angular/material:mdc-migration`
- Breaking changes in component structure and styling

### Standalone Components
- **Angular 15**: Standalone components introduced
- **Angular 17**: Standalone APIs are default in new projects
- **Angular 19**: Full standalone migration recommended

### Build System Changes
- **Angular 16**: esbuild-based builds (experimental)
- **Angular 17**: esbuild + Vite dev server (default)
- **Angular 18**: Build system improvements
- **Angular 19**: Incremental hydration improvements

## Third-Party Library Compatibility

Refer to [angular-dependency-matrix.csv](angular-dependency-matrix.csv) for exact compatible versions of:
- Design Factory
- Bootstrap CSS
- Ng-Bootstrap
- Ng-select
- Ag-grid
- ngx-slider
- AgnosUI

## Breaking Changes Resources

### Official Angular Update Guide
- Template: `https://angular.dev/update-guide?v=[current]-[next]&l=1`
- Example: `https://angular.dev/update-guide?v=13-14&l=1`

### Angular LLM Documentation
- Source: `https://angular.dev/llms.txt`
- Comprehensive API reference optimized for AI consumption

## Common Migration Patterns

### Incremental Migration Strategy
Always migrate incrementally through each major version:
```
Example: Angular 13 → 20
Path: 13→14→15→16→17→18→19→20
```

### Environment Upgrade Timing
- **Before Angular 17**: Upgrade to Node.js 18.19.1+
- **Before Angular 20**: Upgrade to Node.js 20.19.0+ or 22.12.0+

### Material Migration Timing
- Execute MDC migration immediately after reaching Angular 17
- Commit before and after MDC migration
- Perform visual validation of all Material components

## Research Protocol

### GitHub Compatibility Research
For ALL third-party libraries:
1. Search: `[library-name] angular [target-version]`
2. Check last commit date (flag if >6 months)
3. Review open issues for Angular compatibility
4. Identify breaking changes in release notes

### npm Registry Verification
```bash
npm view [package-name] versions
npm view [package-name]@[version] peerDependencies
```

## Dependency Matrix Usage

**CRITICAL RULES**:
1. ALWAYS use EXACT versions from dependency matrix
2. NEVER use "latest" or "^" version ranges
3. Consult matrix in Phase 0 pre-flight validation
4. Update matrix if newer compatible versions discovered through research
5. Validate each third-party library update against matrix

## Unmaintained Package Protocol

If a package has no updates >6 months:
1. Search for actively maintained alternatives
2. Document replacement options with migration effort estimates
3. Flag as HIGH RISK in migration plan
4. Consider forking or replacing before migration

## Version Selection Priority

1. **First Priority**: Exact version from dependency matrix
2. **Second Priority**: Version from GitHub compatibility research
3. **Third Priority**: Version from npm peerDependencies analysis
4. **Never**: "latest" or numerically matching versions without research
