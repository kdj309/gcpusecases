# gcpusecases

In google cloud we came across scenarios where lot of unwanted files needs to be processed. In such common scenario came where we need to use files stored in gcs in DAG process but unnecessarily we are processing all files to avoid that we used Unix time condition only specific files whose Unix time less then specific date only those files are moved to bucket using python
