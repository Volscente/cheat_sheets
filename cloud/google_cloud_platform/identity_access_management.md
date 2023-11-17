# Service Account
## GitHub Workflow GCP Authorization
Reference materials:
- [IAM - Grant Access to a Dataset](https://cloud.google.com/bigquery/docs/control-access-to-resources-iam#grant_access_to_a_dataset)

Steps:
1. Create a Service Account with the role `BigQuery Job User`
2. Go to the dataset that the Service Account needs to read
3. Click on dataset > shares > Add Principal
4. Add the Service Account ID
5. Select the Role `BigQuery Data Viewer` and click done
6. Go back to the Service Account and generate a JSON keys
7. Add those Service Account JSON keys as a GitHub secret
8. Add the following GitHub Action into your GitHub Workflow Code
```yaml
- name: Authenticate to GCP
  uses: google-github-actions/auth@v1
  with:
    credentials_json: ${{ secrets.<GITHUB_SECRET_NAME> }}
```
