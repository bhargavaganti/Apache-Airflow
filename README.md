<h3><a href="https://airflow.apache.org/index.html">Apache Airflow</a></h3>
Helpful Scripts, Configs, and Commands
<br>
<br><b>Create Cloud Composer (Apache Airflow) Environment</b>
<br><code>gcloud composer environments create z-cloud-composer1 \
<br>  --location us-east1 \
<br>  --zone us-east1-b \
<br>  --machine-type n1-standard-1 \
<br>  --env-variables=gcp_project=zproject201807,gcs_bucket=gs://z-airflow-dags,gce_zone=us-east1-b</code>
<br>
<br>
<br><b>Delete Cloud Composer (Apache Airflow) Environment</b>
<br><code>gcloud composer environments delete z-cloud-composer1 \
<br>  --location us-east1</code>
<br>
<br>
<br><b>References:</b>
<br>
<br>
