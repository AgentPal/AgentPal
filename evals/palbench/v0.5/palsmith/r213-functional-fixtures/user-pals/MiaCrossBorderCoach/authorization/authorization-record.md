# R213 Authorization Record

```yaml
pal_id: mia-crossborder-coach
pal_name: Mia CrossBorder Coach
pal_path: evals/palbench/v0.5/palsmith/r213-functional-fixtures/user-pals/MiaCrossBorderCoach/
pal_type: user_custom_pal
authorization_status: active_fixture
requested_by: R213 functional rehearsal
approved_by: R213 controlled fixture
approved_at: 2026-07-01
expires_at: 2026-08-01
review_after: 2026-07-15
scope:
  discovery: workspace_scoped
  invocation: explicit_user_call_only
  delegation: false
  contacts_registration: false
  marketplace: none
allowed_callers:
  - current_workspace_user
allowed_tasks:
  - beginner_crossborder_store_coaching
  - product_judgement
  - store_diagnosis
  - ad_budget_review
denied_tasks:
  - automatic_delegation
  - contacts_registration
  - public_marketplace_listing
  - runtime_connector_execution
data_access:
  allowed:
    - user_provided_store_context
  denied:
    - credentials
    - customer_private_data_without_explicit_scope
memory_access:
  default: minimal
  allowed:
    - private_progress_candidate
  denied:
    - public_pack_memory
  private_memory_allowed: false
revocation:
  method: create revocation record and set discovery false
  preserve_audit_history: true
audit_notes: Workspace discovery only; delegation, contacts, and Marketplace remain disabled.
```
