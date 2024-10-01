# Christmas Tree - Serverless API

A christmas tree endpoint with Serverless Framework Python HTTP API

### Usage

To run the API locally:

```bash
serverless offline
```

You can generate a tree by sending a GET request to the endpoint:

```bash
curl http://localhost:3000/?n={height}
```

> [!NOTE]
> Replace `{height}` with the height of the tree you want to generate.
> Also remember that the port may change if you have other services running on your machine.
