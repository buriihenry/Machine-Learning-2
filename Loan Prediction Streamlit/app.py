import pickle
import streamlit as st

#loading the trained model
pickle_in = open('cassifier.pk1', 'rb') 
classifier = pickle.load(pickle_in)

@st.cache()

# defining the function which will make the prediction using the data which the user inputs 
def prediction(Gender,  Married, ApplicantIncome, LoanAmount, Credit_History):

    #preprocessing user input
    if Gender =="Male":
        Gender = 0
    else:
        Gender = 1
    if Married =="Unmarried":
        Married = 0
    else:
        Married = 1
    if Credit_History =="Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1
    LoanAmount = LoanAmount / 1000

    #Making predictions
    prediction = classifier.predict(
        [[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

    if prediction ==0:
        pred = 'Rejected'
    else:
        pred ='Approved'
    return pred                             

# this is the main functon in which we define our webpage

def main():
    html_temp = """
    <div style ="background-color:blue;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Loan Prediction ML App</h1> 
    </div> 
    """
    # display the front end aspect

    st.markdown(html_temp, unsafe_allow_html =True)
    
    #following line creates boxes in which the user can enter date required to make predictions

    Gender = st.selectbox('Gender',("Male","Female"))
    Married = st.selectbox('Marital Status',("Unmarried", "Married"))
    ApplicantIncome =st.number_input("pplicants monthly income")
    LoanAmount = st.number_input("Total loan amount")
    Credit_History = st.selectbox('Credit_History',("Unclear Debts","No Unclear Debts"))
    result = ""

    # when 'Predict' is clicked, make the prediction and store it 

    if st.button("Predict"):
        result = prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History)
        st.success('Your Loan is{}'.format(result))
        print(LoanAmount)
if __name__=='__main__':
    main()        