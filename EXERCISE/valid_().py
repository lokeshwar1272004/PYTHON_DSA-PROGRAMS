def valid_parenthese(s):
    st=[]
    d ={'(':')','[':']','{':'}'}
    for i in s:
        if i in d.keys():
            st.append(i)
        else:
            if st==[]:
              return False
            else:
                if d[st[-1]]==i:
                    st.pop()

    if st==[]:
        return True
    else:
        return False
s=input("enter your ans: ")
print(valid_parenthese(s))

