#put and delete
##working with API {APPLICATION PROGRAM INTERFACE}

from flask import Flask ,request ,redirect,jsonify

app = Flask(__name__)

#initial data in my to do list
items =[
     {'id':1,'name':'Soap','description':'This item is used to clean'},
     {'id':2,'name':'Detergent','description':'This item is used to wash'}
]

@app.route('/')
def home():
     return 'Welcome to simple to do list'

#reteiving all the data item
@app.route('/getitem')
def get_item():
     return jsonify(items)

##reteiving specific items by their id

@app.route('/getitem/<int:item_id>',methods=['GET'])
def get_items(item_id):
     item = next(( item for item in items if item['id'] == item_id),None)
     if item is None:
          return jsonify({'error':'Items not found'})

     return jsonify(item)


#create a new item
@app.route('/items',methods=['POST'])
def create_item():
     if not request.json or not 'name' in request.json:
          return jsonify({'error':'Items not found'})
     new_item={
          'id':items[-1]['id'] + 1 if items else 1,
          'name':request.json['name'],
          'description':request.json['description']
     }
     items.append(new_item)
     return jsonify(new_item)


#PUT: updating a specific item
@app.route('/items/<int:item_id>',methods=['PUT'])
def updtate_item(item_id):
      item = next(( item for item in items if item['id'] == item_id),None)
      if item is None:
           return jsonify({'error':'item not found'})
      item['name']=request.json.get('name',item['name']), 
      item['description']=request.json.get('description',item['description']) 
      return jsonify(item)
#Delete :Delete na item 
@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
     global items
     items=[item for item in items if item['id'] !=item_id ]
     return jsonify({'result':"item deletd successfully"})


if __name__ =='__main__':
     app.run(debug=True)