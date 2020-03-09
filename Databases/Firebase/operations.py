from firebase_admin import credentials,db,initialize_app


#credentials of the firebase app has to be placed here ( the json data file that can be downloaded form the firebase app`s console )
cred = credentials.Certificate({
  #place json security credentials here
}
)

initialize_app(cred,{'databaseURL':'URL here'})
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


