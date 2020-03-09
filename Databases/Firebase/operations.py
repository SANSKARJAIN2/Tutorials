from firebase_admin import credentials,db,initialize_app


#credentials of the firebase app has to be placed here ( the json data file that can be downloaded form the firebase app`s console )
cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "learn-ccd0a",
  "private_key_id": "0e9f8f4bb0fc12fd8ac80a433fc0ffc96c99c6cd",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDPJAToqKTbkMeE\n3pkU1akgn8UQigNPck2JdJsTJrzYR5Bf2VV6xJrgACeywK09LhTuJ4En3A86RtaB\nkUQrpxQFhYphJoy2xVWKOhJ8uf1xKGmtKci1V57upPaQJb9YJvla5uk/XDcapGCZ\n6oIAyW7Sj6LA7bIe+6JXABlgq3rWnhO2I/xOhmrk3xoimucVzyZvjF1R0ZmWjXqU\nbwY0nwussMe43mz4EkdAEwc+5DidwEdZNSMRvaogKTF4CZP8O+j42d1dWrwewWa8\nMQYARaEZDZxS1bAKHEZg+XPSazvcnqbLUguoDq5Aabjg8r1HkNRMGO4KQkYE3Pm4\nEXvMeNjzAgMBAAECggEAGNIbGHnkzz6I+d3mf/2eN3+NkI7JGML8kYT8dA4HQO9K\nWIHlYUGfwUmjeCLoX1VfQq5PJqSS2ovUdlAe2BA8MPEwhLWm1NvOhTKyNmne+ak7\nCHniSACI1dXEib9ML1b0ODVFK8dz/uhFfwv/qfJ5Khf2C6Iv3tCOQliLse66WG7/\ng29S3a3oqfja3DdL5k8vMuKkkf/bfSldjWJM8oBvE+beETg1gZz5VSVq5cpPtz4o\n11p573XYZhiXyjI6z7SgGyjPy92OFAWgf1j2TgdR3PhCayVhbTAsy7oZxjuq7ZYX\nnsAIumFo6UklxAV6fjzlZG95QpoRJB5bbfGRNMgeSQKBgQDnzlm693wMQpujgkPd\nM4KWqij1e+1pMv3eBDDVDVkEbGMBFwLLR30baB3GYclMYYrUthSQ13pAIq93/Do4\ngOo1l6aZuHsiniFWfRyFoUjb1I41p+AlkcX0n1/CGq21EW9k7P6SJP/6Zj9qtJv2\nUBUEbwng7zNwwKrs+qj7x2fTTQKBgQDkwqHroxnw2CH9Ww/fB3WN+dALEgXIXWeO\nhX10tHrikPz2xzUXmy6d1qEt2gi3TxZxgxrKsO5Nd8mH15uwC6+XjBIUc4HQabe+\n+litY/y901euy9NTbKWqdhq8wgb3g0VBQRRpn2oAuwgCcLDt5jGH6B093xCqwFD3\n5jjmkJy9PwKBgQCSJXhPN49fD3OfABcXVE2F/hw6wXpqM/r4yf2bpYG1FzzISCC7\n1wOajucO10IZxPnJqE6JD0GFRBkK9dwjGawQQ9+G1VfU+IueQt0Dpy8PYhCS5Zed\nOC3tT7oI39ca7LYllIHf1DILRgG/ncUi41SM6hD5XvY4pVBefp6htxPPlQKBgQCm\ncmuobVthn5FTrB9nMyE4tYzHkUx91mCUFdMLyIolMkOtN5MM4w/PLqzGFQAEiNoW\nq8Mhug0ads8/NQUF2erghL1e/hB1WYalwbgmKTtrz0vcVlgkOkhsOFUKBM9W5r/M\nVBMLKz/Q2kVgqShDYRum/J/SNe0FoLsJNQ0vzgcNtwKBgCEAgrmH+sjm3dp2PvU7\n9JzUo2b/4iuMR8MJ45GZSqhZaT/rrrdNOdw5xkqV6IuIz/fXAOWovw4PaZyjWstO\nRGRPv0CubmbojByvDfWc5NfSyhQuNmlHJfsnxDpiI+ioK4MjWPZmgMrS1VDK5nAp\nJmu4becoSjETzxPO0xXDlvtl\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-clwjy@learn-ccd0a.iam.gserviceaccount.com",
  "client_id": "115044363833263055668",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-clwjy%40learn-ccd0a.iam.gserviceaccount.com"
}
)

initialize_app(cred,{'databaseURL':'https://learn-ccd0a.firebaseio.com/'})
ref=db.reference("server/saving-data/fireblog")

def setmethod():
    user_ref=ref.child('users')    
    user_ref.set({
    'sanskar':{
        'date_of_birth':"sept 2, 1999",
        "full_name":"Sanskar Jain"
    },
    "shanu":{
        'date_of-birth':"Sept 1,1999",
        'Full_name':'Shanu Jain'
    }
    })
#direcly changing values of child

    user_ref.child('sanskar').set({
    "date-of-birth":"02/09/1999",
    "full_name":"Sanskar Jain"

    })
    user_ref.child('shanu').set({
    "date-of-birth":"01/09/1999",
    "full_name":"Shanu Jain"

    })
def updatemethod():
    #UPDATE METHOD
    user_ref=ref.child('users')
    user_ref=user_ref.child("sanskar")
    user_ref.update({
    'nickname':"Shanu"
    })


#.update({   "childnode/childnode/key":value   })
# Inthis secion we are actually chaging the cureent referency updating the value i.e we are going to child nodes then updateing their value because we are giving the path in keys whihc is actually modifying the current refernce of db
    user_ref=ref.child('users')
    user_ref.update({
    "sanskar/nickname":"shanu",
    "shanu/nickname":"sanskar"
    })

#in this as we are directly proving the value so the updation will be made in current refence instead of updating the child nodes.
#keys are main and if we provide the path in keys then updation will be done in the child nodes else the argument will be takes as value and update in users or current reference value is done directly.
    user_ref.update({
    'sanskar':{
        'nickname':'shanu'
    },
    'shanu':{
        'nickname':'neeraj'
    }

    })
def pushmethod():
#push lets multiple writes at the same time by providing unique key to each child so that none of the data is deleted and the data is stored in different child
    posts_ref=ref.child("post")
    posts_ref=posts_ref.push()
    posts_ref.set({
    'author':'sanskar',
    "title":'COBOL- A new programming language'
    })
    #Resetting the posts_ref becuase it was modified by .push method above
    posts_ref=ref.child("post")
    posts_ref.push().set({
        "author":'aman',
        'title':'History of Java'
    })

    posts_ref.push({
        'Author':"ROhit",
        "Titile":'God of programming languages'
    })


def increment_votes(current_value):
    print(current_value)
    return current_value +1 if current_value else 1
def transactionoperation():
    upvotes_ref=db.reference('server/saving-data/fireblog/post/-M1ywma0-tXjnqRvOBQT/upvotes')
    try:
        new_vote_count=upvotes_ref.transaction(increment_votes)
        print(type(new_vote_count))
        print("transaction completed")
    except db.TransactionAbortedError:
        print('Transaction failed to commit')