import sys

# [START storage_create_bucket]
from google.cloud import storage


def create_bucket(udin):
    """Creates a new bucket."""
    # bucket_name = "your-new-bucket-name"

    storage_client = storage.Client()

    bucket = storage_client.create_bucket(udin)

    print("Bucket {} created".format(udin))


# [END storage_create_bucket]

if __name__ == "__main__":
    create_bucket(udin=sys.argv[1])


