

###################################################################################################
#
#   Cloud Composer (Apache Airflow)
#
#   Google Cloud Platform (GCP)
#
#   References:
#   https://cloud.google.com/composer/docs/quickstart
#   https://cloud.google.com/composer/docs/how-to/managing/creating
#
###################################################################################################



# Create Cloud Composer (Apache Airflow) Environment
gcloud composer environments create z-cloud-composer1 \
  --location us-east1 \
  --zone us-east1-b \
  --machine-type n1-standard-1 \
  #--env-variables=gcp_project=project123,gcs_bucket=gs://mybucket,gce_zone=us-east1-b



# Upload Dag(s) from Google Cloud Storage (or other specified source)
sleep 300  # Wait 5 minutes before uploading
gcloud composer environments storage dags import \
     --environment z-cloud-composer1 \
     --location us-east1 \
     --source gs://z-airflow-dags 



# Delete Cloud Composer (Apache Airflow) Environment
gcloud composer environments delete z-cloud-composer1 \
  --location us-east1



#ZEND
