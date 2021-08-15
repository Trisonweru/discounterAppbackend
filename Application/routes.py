from flask import Flask, request, session
from Application import app, db
from model import DiscountCode

@app.route("/", methods=["POST"])
def discount_info():
    data=request.get_data()
    print(data)
    if data and request.method=="POST":
        try:
            discount=DiscountCode(title=data[0], code=data[1])
            db.session.add(discount)
            db.session.commit()
            print(discount)
            return "Successfully saved"
        except Exception as error:
            print(error)
            return f"There was an error trying to save data: {error}"        
    return "Method Not Allowed"