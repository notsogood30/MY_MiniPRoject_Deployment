import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('df_model1.pkl','rb'))


def predict_forest(score_hidden,link_id,downs,author,archived,parent_id,gilded,controversiality,subreddit_id,edited,body):
    input=np.array([[score_hidden,link_id,downs,author,archived,parent_id,gilded,controversiality,subreddit_id,edited,body]]).astype(np.int64)
    prediction=model.predict(input)
    #pred='{0:.{1}f}'.format(prediction[0][0], 2)
    return float(prediction)

def main():
    st.title("DEPLOYMNET PART : ")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">REDDIT COMMENTS POPULARITY PREDICTION ML APP</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    score_id = st.text_input("score_id","Type Here 0  or 1")
    link_id = st.text_input("link_id","Type Here an int(positive)")
    downs = st.text_input("downs","Type Here 0")
    author = st.text_input("author","Type Here an int(positive)")
    archived = st.text_input("archived","Type Here 0")
    parent_id = st.text_input("parent_id","Type Here an int(positive)")
    gilded = st.text_input("gilded","Type Here 0 , 1 or 2")
    controversiality = st.text_input("controversiality","Type Here 0")
    subreddit_id = st.text_input("subreddit_id","Type Here an int(positive)")
    edited = st.text_input("edited","Type Here an int(positive)")
    body = st.text_input("body","Type Here an int(positive or negative)")
    safe_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> Your forest is safe</h2>
       </div>
    """
    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> Your forest is in danger</h2>
       </div>
    """

    if st.button("Predict"):
        output=predict_forest(score_id,link_id,downs,author,archived,parent_id,gilded,controversiality,subreddit_id,edited,body)
        st.success('The number is {}'.format(output))
if __name__=='__main__':
    main()