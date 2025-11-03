# Changelog

All notable changes to this project will be documented in this file.

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
## [Unreleased]

### Added
- `query_transform` parameter in `BaseRAGQuestionAnswerer` and `AdaptiveRAGQuestionAnswerer` to support optional query rewriting before retrieval. Accept a `pw.UDF` or Python callable that can transform queries to improve retrieval quality.

### Fixed
- Endpoints created by `pw.io.http.rest_connector` now accept requests both with and without a trailing slash. For example, `/endpoint/` and `/endpoint` are now treated equivalently.
- Schemas that inherit from other schemas now automatically preserve all properties from their parent schemas.
- Fixed an issue where the persistence configuration failed when provided with a relative filesystem path.

## [0.26.4] - 2025-10-16

### Added
- New external integration with [Qdrant](https://qdrant.tech/).
- `pw.io.mysql.write` method for writing to MySQL. It supports two output table types: stream of changes and a realtime-updated data snapshot.

### Changed
- `pw.io.deltalake.read` now accepts the `start_from_timestamp_ms` parameter for non-append-only tables. In this case, the connector will replay the history of changes in the table version by version starting from the state of the table at the given timestamp. The differences between versions will be applied atomically.
- Asynchronous UDFs for connecting to API based llm and embedding models now have by default retry strategy set to `pw.udfs.ExponentialRetryStrategy()`
- `pw.io.postgres.write` method now supports two output table types: stream of changes and realtime-updated data snapshot. The output table type can be chosen with the `output_table_type` parameter.
- `pw.io.postgres.write_snapshot` method has been deprecated.

[... rest of changelog ...]