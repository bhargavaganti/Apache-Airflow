

###################################################################################################
#
#   Cloud Composer Demo - Startup Script
#
###################################################################################################


############################################################
#
#   Cloud Composer (Apache Airflow)
#
############################################################

# Create Cloud Composer (Apache Airflow) Environment
gcloud composer environments create z-cloud-composer1 \
  --location us-east1 \
  --zone us-east1-b \
  --machine-type n1-standard-1


# NOTE: Make sure to create MySQL Conection with Airflow UI (Admin >> Connections)


# Clone "airflow_dags" Repo from Google Cloud Source Repo
cd /tmp
rm -rf /tmp/airflow_dags
gcloud source repos clone airflow_dags


# Upload DAG(s) from Google Source Repository
gcloud composer environments storage dags import \
     --environment z-cloud-composer1 \
     --location us-east1 \
     --source /tmp/airflow_dags/airflow_demo1.py


# Upload DAG(s) from Google Source Repository
gcloud composer environments storage dags import \
     --environment z-cloud-composer1 \
     --location us-east1 \
     --source /tmp/airflow_dags/airflow_demo_mysql.py


# Upload DAG(s) from Google Cloud Storage (or other specified source)
#gcloud composer environments storage dags import \
#     --environment z-cloud-composer1 \
#     --location us-east1 \
#     --source gs://mybucket/my_airflow_dag.py


############################################################
#
#   GCE Instance (General VM)
#
############################################################



############################################################
#
#   MySQL
#
############################################################

# NOTE: Make sure to create MySQL Conection with Airflow UI (Admin >> Connections)


# Create Cloud SQL (MySQL) Instance
# https://cloud.google.com/sql/docs/mysql/create-instance
gcloud sql instances create z-mysql-1 \
    --database-version=MYSQL_5_7 \
    --tier=db-n1-standard-1 \
    --region=us-east1


# Create Database
gcloud sql databases create zdatabase --instance z-mysql-1


# Set the password for the "root@%" MySQL user:
gcloud sql users set-password root % --instance z-mysql-1 --password mysql_123


# Connect to Cloud SQL (MySQL) Instance
gcloud sql connect z-mysql-1 --user=root


# Create MySQL Dummy Data
'''

CREATE DATABASE zdatabase;

USE zdatabase;

CREATE TABLE banking (
  transaction_id INT NOT NULL,
  customer_id INT NOT NULL,
  name VARCHAR(50) NOT NULL,
  state CHAR(2),
  transaction FLOAT,
  calls INT,
  at_risk INT,
  PRIMARY KEY (transaction_id)
);

INSERT INTO banking 
    (transaction_id, customer_id, name, state, transaction, calls, at_risk) 
VALUES 
    (100001, 1001, "Danny", "NC", 100.00, 0, 0),
    (100002, 1002, "Rusty", "NV", 200.00, 1, 1),
    (100003, 1003, "Linus", "IL", 300.00, 2, 0),
    (100004, 1004, "Terry", "NV", 400.00, 3, 1),
    (100005, 1005, "Tess",  "NV", 500.00, 4, 0),
    (100006, 1001, "Danny", "NC", 200.00, 0, 0),
    (100007, 1001, "Danny", "NC", 300.00, 0, 0),
    (100008, 1002, "Rusty", "NV", 400.00, 3, 1)    
    ;

SELECT * FROM banking;

SELECT customer_id, count(*) as number_of_transactions, avg(transaction) as avg_transaction 
FROM banking 
GROUP BY customer_id;





CREATE DATABASE catalog;

USE catalog; 

CREATE TABLE delivereddatafiles (
  DeliveredDataFileID int NOT NULL AUTO_INCREMENT,
  Filename VARCHAR(100),
  RegisterDateTime DATETIME,
  TimeFrameOfFile CHAR(1),
  DateOfFile VARCHAR(12),
  IsReprocess INT,
  TypeOfFile VARCHAR(5),
  IsReissue INT,
  PRIMARY KEY (DeliveredDataFileID)
);

INSERT INTO delivereddatafiles 
    (Filename, RegisterDateTime, TypeOfFile) 
VALUES 
    ("dummyfile.txt", "2018-08-01 12:01:02", "TXT"),
    ("dummydata.csv", "2018-08-02 13:02:03", "CSV");


'''



#ZEND
