from google.cloud import storage
#importing storage from google.cloud

import datetime
#importing datetime inbuilt method for filtering

storage_client = storage.Client()
#to access cloud storage methods we need call Client
def copy_blob(
    bucket_name, blob_name, destination_bucket_name, destination_blob_name, move=False
):
    """Copies a blob from one bucket to another with a new name."""
    source_bucket = storage_client.bucket(bucket_name)
    #accessing source bucket 

    source_blob = source_bucket.blob(blob_name)
    #it will instantiate the blob
    
    destination_bucket = storage_client.bucket(destination_bucket_name)
    #accessing destination bucket

    blob_copy = source_bucket.copy_blob(
        source_blob, destination_bucket, destination_blob_name
    )
#copy_blob replaces the blob with destination_blob
    if move:
        source_bucket.delete_blob(blob_name)
#if move is true then original(source blob) will be deleted
    print(
        "Blob {} in bucket {} copied to blob {} in bucket {}.".format(
            source_blob.name,
            source_bucket.name,
            blob_copy.name,
            destination_bucket.name,
        )
    )


def filter_files(bucket_name, src_folder, dest_name,x):
    #filtering part is called from this method
    blobs = storage_client.list_blobs(bucket_name)
    #it will return all files in that particular bucket
    for blob in blobs:
#iterating over array of blobs
        if blob.name.split('/')[0] == src_folder and blob.name[-1] != '/':
#checking the path is matching with passed arguments (src) and last letter is / if it matches then it proceeds further
            file_name = blob.name.split('/')[-1]

            print(file_name)
#printing out file name which is splited from blob.name
            try:

                mytimestamp = datetime.datetime.fromtimestamp(
#fromtimestamp returns the date associated with passed timestamp
                    int(file_name.split('.')[1]))
#passing the unix value from the file name by using split
            except:

                mytimestamp = datetime.datetime.fromtimestamp(

                    int(file_name.split('.')[1])/1000)
#we can get particular date from timestamp by dividing unix value by 1000

            timedifference = datetime.datetime.now() - datetime.timedelta(days=x)
            epochtime=timedifference.strftime('%s')
            mytimestamp1 = datetime.datetime.fromtimestamp(int(epochtime)) 
            #print(mytimestamp,mytimestamp1) 
# timestamp of Nov27

            # print(mytimestamp.strftime( "%Y - %m - %d  %H : %M : %S")  )

            # print(mytimestamp1.strftime( "%Y - %m - %d  %H : %M : %S")  )

            if mytimestamp < mytimestamp1:
#if the file timestamp is less then Nov27 then only copy_blob method is called using passed arguments
                copy_blob(bucket_name=bucket_name, blob_name=blob.name,

                          destination_bucket_name=bucket_name, destination_blob_name=dest_name + '/' + file_name, move=True)


filter_files("karthikbucket", "sourcefolder", "destfolder",3)