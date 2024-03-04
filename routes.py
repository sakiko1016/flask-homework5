@app.route('/books', methods=['GET', 'POST'])
@jwt_required()
def books():
    if request.method == 'GET':
        # Get all books
    elif request.method == 'POST':
        # Create book
        
@app.route('/books/<int:book_id>', methods=['GET', 'PUT', 'DELETE']) 
@jwt_required()
def book(book_id):
    # CRUD for single book
    
if __name__ == '__main__':
    app.run()