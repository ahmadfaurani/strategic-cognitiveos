# Information Classification

## Sensitivity Levels

| Level | Description | Storage | Replication |
|-------|-------------|---------|-------------|
| public | Approved for public release | Any platform | Freely replicated |
| internal | Internal organisational information | GitHub (private), Notion, Obsidian | May be copied across platforms |
| confidential | Sensitive business or stakeholder information | GitHub (private) with access controls | Requires owner approval before copying |
| restricted | Sensitive intelligence, legal authority, protected stakeholder info | GitHub (private, access-controlled) only | Must not be replicated without explicit approval |
| controlled | Highest sensitivity; legally or operationally sensitive | Local encrypted storage only | No replication permitted |

## Rules

1. Every record must have a sensitivity classification.
2. Records classified as `restricted` or `controlled` must not be replicated to Notion or external platforms without explicit approval from the record owner.
3. Records classified as `confidential` require CVS validation for claims involving this data.
4. Records classified as `restricted` or `controlled` require mandatory CVS validation.
5. All access and changes to `controlled` records must be logged and reviewed.
6. When in doubt, classify upward — it's easier to declassify than to recover from a leak.
