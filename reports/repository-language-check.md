# Repository Language Check

## Summary

```text
scanned_extensions: .json, .md, .ps1, .py, .txt, .yaml, .yml
bad_patterns: 10
bad_pattern_hits: 4
```

## Scan Scope

```text
included: reviewer-facing markdown, metadata, scripts, reports, and repository documentation
excluded: generated evidence artifacts, checker self-pattern definitions, legacy placeholder artifact generator
```

## Pattern Hits

| File | Line | Pattern | Text |
|---|---:|---|---|
| `internal/scenario-quality-model.md` | 13 | `flagship` | * flagship scenario criteria |
| `internal/scenario-quality-model.md` | 236 | `flagship` | # Flagship Scenario Criteria |
| `internal/scenario-quality-model.md` | 238 | `flagship` | A flagship scenario should demonstrate: |
| `internal/scenario-quality-model.md` | 250 | `flagship` | Flagship scenarios should represent the repository’s best operational design and realization quality. |
