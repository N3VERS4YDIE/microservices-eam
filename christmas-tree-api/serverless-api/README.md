# Serverless Christmas Tree

A christmas tree endpoint with Serverless Framework Python HTTP API

### Usage

```bash
serverless offline
```

After running, you should see output similar to:

```bash
⠸ Initializingerror resolving aws account id
Starting Offline at stage dev (us-east-1)

   ┌──────────────────────────────────────────────────┐
   │                                                  │
   │   Sponsored by Arccode, the RPG for developers   │
   │   https://arccode.dev?ref=so                     │
   │   Disable with --noSponsor                       │
   │                                                  │
   └──────────────────────────────────────────────────┘

Offline [http for lambda] listening on http://localhost:3002
Function names exposed for local invocation by aws-sdk:
   * hello: christmas-tree-dev-hello

   ┌─────────────────────────────────────────────────────────────────────────┐
   │                                                                         │
   │   GET  | http://localhost:3000/                                         │
   │   POST | http://localhost:3000/2015-03-31/functions/hello/invocations   │
   │                                                                         │
   └─────────────────────────────────────────────────────────────────────────┘

Server ready: http://localhost:3000 🚀
```
