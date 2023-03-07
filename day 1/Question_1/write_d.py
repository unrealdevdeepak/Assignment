
def write_f():
    user_input=input("Enter data to Write ..... ")
    with open('./data.txt','w') as f:
        f.write(user_input)
    import app
    app.menu()
    
    