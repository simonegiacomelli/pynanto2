This project make use of the webidls from https://github.com/rustwasm/wasm-bindgen/tree/main/crates/web-sys.
Find their licences under folder 'webdils'

# Structure

There are the main phases:

- ingest
- merge
- stringify

## Ingest

The idl is parsed and it returns data-model class instances

## Merge

Webidl can declare entities like 'partial interface' so the ing

## Stringify

It takes data-model instances and turns them in pieces of python source code strings
