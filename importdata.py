import pymongo

client = pymongo.MongoClient("mongodb+srv://kurso:kurso2020@cluster0.yxyww.mongodb.net/easywebshop?retryWrites=true&w=majority")
db = client.easywebshop
product_collection = db.products
products = [
        {
            "name": "Dog Shampoo",
            "brand": "Top Fin",
            "price": 14.24,
            "stock": 15,
            "image": "https://cdn0.woolworths.media/content/wowproductimages/large/892654.jpg"
        },
             {
            "name": "Dog Shampoo",
            "brand": "Top Fin",
            "price": 14.24,
            "stock": 15,
            "image": "https://cdn0.woolworths.media/content/wowproductimages/large/892654.jpg"
        },
             {
            "name": "Dog Shampoo",
            "brand": "Top Fin",
            "price": 14.24,
            "stock": 15,
            "image": "https://cdn0.woolworths.media/content/wowproductimages/large/892654.jpg"
        },
             {
            "name": "Dog Shampoo",
            "brand": "Top Fin",
            "price": 14.24,
            "stock": 15,
            "image": "https://cdn0.woolworths.media/content/wowproductimages/large/892654.jpg"
         },
    ]   
    
result = product_collection.insert_many(products)
print(result)

