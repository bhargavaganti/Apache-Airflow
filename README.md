<h3>Google (GCP) Cloud Composer (<a href="https://airflow.apache.org/index.html">Apache Airflow</a>)</h3>
Helpful Scripts, Configs, and Commands
<br>
<br><b>Create Cloud Composer (Apache Airflow) Environment</b>
<br><pre><code>gcloud composer environments create z-cloud-composer1 \
  --location us-east1 \
  --zone us-east1-b \
  --machine-type n1-standard-1 \
  --env-variables=gcp_project=zproject201807,gcs_bucket=gs://z-airflow-dags,gce_zone=us-east1-b</code></pre>
<br>
<br><b>Delete Cloud Composer (Apache Airflow) Environment</b>
<br><pre><code>gcloud composer environments delete z-cloud-composer1 \
  --location us-east1</code></pre>
<br>
<br><b>References:</b>
<br>&nbsp;&nbsp;&nbsp;&nbsp;&bull;&nbsp;<a href="https://cloud.google.com/composer/docs/quickstart">Google (GCP) Cloud Composer</a>
<br>
