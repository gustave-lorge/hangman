





st = open("st.txt", "w")
st.write("hi from python, did this addition make it in?")
st.close()

             

with open("st.txt", "r") as f:
    print(f.read())
