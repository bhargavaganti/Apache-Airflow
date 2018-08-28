<h3>Google (GCP) Cloud Composer (<a href="https://airflow.apache.org/index.html">Apache Airflow</a>)</h3>
This repo contains helpful Scripts, Configs, and Commands
<br>
<br>
<br><b>Create Cloud Composer (Apache Airflow) Environment</b>
<br><pre><code>gcloud composer environments create z-cloud-composer1 \
  --location us-east1 \
  --zone us-east1-b \
  --machine-type n1-standard-1 \
  --env-variables=gcp_project=project123,gcs_bucket=gs://mybucket,gce_zone=us-east1-b</code></pre>

<br><b>Delete Cloud Composer (Apache Airflow) Environment</b>
<br><pre><code>gcloud composer environments delete z-cloud-composer1 \
  --location us-east1</code></pre>

<br><b>Upload DAG from source (source could be local, gcs path, url, etc. It could also be a path to directory with multiple DAGs.</b>
<br><pre><code>gcloud composer environments storage dags import \
     --environment z-cloud-composer1 \
     --location us-east1 \
     --source /tmp/airflow_dags/airflow_demo1.py</code></pre>

<br><b>Remove/Delete DAG from Cloud Composer</b>
<br><pre><code>gcloud composer environments storage dags delete \
     --environment z-cloud-composer1 \
     --location us-east1 \
     my_dag_name</code></pre>

<br><b>References:</b>
<br>&nbsp;&nbsp;&nbsp;&nbsp;&bull;&nbsp;<a href="https://cloud.google.com/composer/docs/quickstart">Google (GCP) Cloud Composer</a>
<br>&nbsp;&nbsp;&nbsp;&nbsp;&bull;&nbsp;<a href="https://github.com/apache/incubator-airflow">Apache Airflow Github</a>
<br>&nbsp;&nbsp;&nbsp;&nbsp;&bull;&nbsp;<a href="https://airflow.apache.org/">Apache Airflow Docs</a>
<br>
