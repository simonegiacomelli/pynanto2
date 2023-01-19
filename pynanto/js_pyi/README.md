This project make use of the webidls from https://github.com/rustwasm/wasm-bindgen/tree/main/crates/web-sys.
Find their licences under folder 'webdils'

# Structure

There are three phases: ingest, stringify and produce

## Ingest

The idl is parsed and it returns data-model class instances

## Stringify

It takes data-model instances and turns them in pieces of python source code strings

## Produce

It produces the assembled output