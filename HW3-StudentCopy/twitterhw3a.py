# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.
from TwitterAPI import TwitterAPI


access_token_key = "2473973030-dT9wJ0O4EedtLjdwr17JmDlsriHZVFK9rKofDs7"
access_token_secret = "XYfbm1JgHP4MG0yW7H4NmDKHuGjJ6M3R7iiaXICIasWIW"
consumer_key = "4S5UioS8r18Dg9q5KeFjRWssx"
consumer_secret = "	IaqTNMBtYWC9UUijpgnBX3DJoA1JlCZFckVEIysonM3hDCsfel"

api = TwitterAPI(consumer_key,
                 consumer_secret,
                 access_token_key,
                 access_token_secret)

# STEP 1 - upload image
file = open('pic.jpg', 'rb')
data = file.read()
r = api.request('media/upload', None, {'media': data})
print('UPLOAD MEDIA SUCCESS' if r.status_code == 200 else 'UPLOAD MEDIA FAILURE1')

# STEP 2 - post tweet with reference to uploaded image
if r.status_code == 200:
        media_id = r.json()['media_id']
        r = api.request('statuses/update', {'status':'I found pizza!', 'media_ids':media_id})
        print('UPDATE STATUS SUCCESS' if r.status_code == 200 else 'UPDATE STATUS FAILURE2')