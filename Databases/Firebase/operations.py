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


