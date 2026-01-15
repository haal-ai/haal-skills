# BMS Introduction and Principles

## Summary
BMS (Build Management System) is Amadeus' C/C++ build tool that manages libraries, dependencies, compilations, unit tests, and delivery. This document covers core principles including component-based architecture, the Description.xml configuration file, and binary compatibility concepts. Understanding these principles is essential when working with BMS-based C++ projects, particularly for managing dependencies and ensuring efficient build times.

> BMS is used by 1,500+ Amadeus C++ developers and runs 2,000,000 times per week, making it a critical tool for large-scale modular C++ development.

---

## Key Concepts

- **Component-Based Architecture**: BMS enforces modular design where applications are split into small, reusable components with clear public APIs
- **1 Component = 1 Library/Binary**: Each BMS component is atomic and produces exactly one library or binary output
- **Description.xml**: The primary configuration file that describes a component, its dependencies, API, and build requirements
- **Binary Compatibility**: Critical optimization allowing dependent components to use new versions without recompiling
- **ComponentPack vs UnitTestPack**: Description.xml describes the main componentPack (required) and optionally a unitTestPack component
- **Time to Market**: Modularization and binary compatibility reduce compilation/testing times, accelerating delivery

---

## Historical Context

**Problems BMS Solved:**
- Long compilation times from monolithic designs
- Mass recompilation due to tightly coupled object models
- Interface breakage causing perpetual redesign
- Poor code reusability and costly maintenance
- Poor adaptability and long time to market

**Solution Approach:**
- Modularization into small, independent components
- Consistent dependency management
- Stable public APIs to minimize interface changes
- Component-level build and unit testing

---

## Description.xml Components

The Description.xml file contains:
- **Component Type**: Whether it produces a library or binary
- **Identity**: Library/binary name and version
- **Dependencies**: Direct dependencies on other components
- **Public API**: For libraries, defines the public interface (header files)
- **Internal Code**: The component's implementation files

---

## Binary Compatibility Strategy

**Definition:** A new component version is binary compatible if dependent components can use it without:
- Changing their source code
- Recompiling their code

**Benefits:**
- Shorter build times across the dependency tree
- Faster bug fixes and feature delivery
- Lower time to market for dependent projects

**Developer Responsibility:**
- Design architectures to maintain binary compatibility
- Allow bug fixes and new features without breaking APIs
- Minimize interface changes to dependent components

---

## Usage Context

**When to Consider BMS Principles:**
- Designing new C++ component architectures
- Managing dependencies between C++ libraries
- Planning API changes that might affect downstream components
- Optimizing build times in large C++ codebases
- Troubleshooting dependency or compilation issues

**Key Metrics:**
- 1,500+ developers using BMS
- 2,000,000 weekly executions
- Enterprise-scale C++ development at Amadeus
