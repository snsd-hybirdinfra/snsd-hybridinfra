# Content Generator Tools

This directory contains tools that generate, repair, validate, and summarize repository documentation and scenario artifacts.

## Purpose

The content-generator layer keeps the operational scenario catalog structurally consistent and reviewable.

It supports:

- scenario metadata generation
- scenario README generation support
- evidence artifact maintenance
- related scenario mapping
- index generation
- repository quality validation
- portfolio health reporting
- repository summary reporting

## Primary Validation Entrypoint

The primary validation workflow is:

- run_repository_validation.py

This script coordinates the main repository validation sequence and should be used before committing significant repository changes.

## Generator Tools

Generator tools create or refresh repository artifacts such as scenario indexes, module indexes, adapter indexes, build indexes, repository reports, and portfolio health summaries.

These tools should preserve the platform positioning and avoid introducing implementation-centric or vendor-centric language where a reusable operational capability description is required.

## Validation Tools

Validation tools check:

- markdown links
- top-level repository structure
- root README alignment
- repository language policy
- poster template integrity
- artifact coverage
- scenario quality expectations

## Repair Tools

Repair tools are used to restore missing generated artifacts or repair repository baseline gaps.

Repair tools should be used carefully because they may modify many scenario directories at once.

## Operational Boundary

The content-generator tools maintain documentation and validation consistency. They should not be treated as proof of live production execution.

Generated content must remain reviewer-readable and must preserve the distinction between portfolio documentation evidence and live execution evidence.
