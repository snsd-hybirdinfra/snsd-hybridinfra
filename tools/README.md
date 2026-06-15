# Repository Tooling

This directory contains the automation and validation tools used to keep the repository consistent and reviewable.

## Purpose

The tooling layer supports repository generation, validation, and maintenance tasks such as documentation updates, link checks, and inventory generation.

## Tool groups

- [content-generator](content-generator/) — documentation, index, and validation generation tools
- [diagram-renderer](diagram-renderer/) — poster and diagram rendering utilities

## Main entrypoint

- [content-generator/run_repository_validation.py](content-generator/run_repository_validation.py)

## Role in the repository

Tools help maintain structure and consistency, while the actual operational meaning stays in the scenarios, labs, modules, adapters, and docs.
