# Review Producer API As Consumer

Run:

```text
@[/review-producer-api-as-consumer]
demand_folder: <demand_folder>
```

You can optionally provide:
- `openapi_path`
- `functional_spec_path`
- `consumer_context`

The skill will:
- select the latest spec artifacts by default
- propose a review plan
- after approval, write a consumer review report under `09-consumer-review/`
