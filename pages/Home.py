import streamlit as st
import time
from streamlit.components.v1 import html


placeholder=st.empty()
def app():
    # Displaying the logo and subtext with a nice color
    html(height=500,width=900,
         
        html="""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Sentiment Analysis App</title>
            <style>
            
                #typing-text {
                    color: #6a696b;
                    text-shadow: 2px 2px 5px black;
                    border-right: 2px solid black; /* Cursor effect */
                    white-space: nowrap;
               
                   
                }

                #typing-text-green {
                    color: green;
                    text-shadow: 2px 2px 5px black;
            
                }
            </style>
        </head>
        <body>
            <div style='padding: 10px; border-radius: 10px;'>
                <h1 style='font-family: "Courier New", Courier, monospace; font-weight: bold; letter-spacing: 3px;'>
                    <span id="typing-text" style=' font-size: 50px; text-shadow: 2px 2px 5px black;'></span> 
                    <span id="typing-text-green" style='color: green; font-size: 50px; text-shadow: 2px 2px 5px black;'></span>
                </h1>
            </div>
            
            <div>
                <h3 style='color: #6a696b; font-size: 20px; animation: fadeIn 2s; font-family: "Courier New", Courier, monospace; font-weight: light; letter-spacing: 1px;'>Project Brief:</h3>
                <h4 style='color: #6a696b; font-size: 20px; animation: fadeIn 2s; font-family: "Courier New", Courier, monospace; font-weight: light; letter-spacing: 1px;'>A powerful tool for analyzing sentiments in user inputs to detect spam effectively.</h4>
                <h4 style='color: #6a696b; font-size: 17px; animation: fadeIn 2s; font-family: "Courier New", Courier, monospace; font-weight: light; letter-spacing: 1px;'>This sentiment analysis app leverages advanced natural language processing techniques to evaluate user-submitted text. 
        Users can enter their input directly into a text box or upload a text file for analysis. Once submitted, the app processes the text and classifies it as positive, negative, or neutral.</h4>
                <p style='color: #6a696b; font-size: 20px; animation: fadeIn 2s; font-family: "Courier New", Courier, monospace; font-weight: light; letter-spacing: 1px;'>
                    The results are displayed instantly, providing users with valuable insights into the emotional tone of their content. 
                    This feature is particularly useful for detecting spam or inappropriate messages, ensuring a safe and engaging user experience.
                </p>

                <p style='color: #6a696b; font-size: 20px; animation: fadeIn 2s; font-family: "Courier New", Courier, monospace; font-weight: light; letter-spacing: 1px;'>
                    With this app, users can quickly assess the sentiment of their text, making it easier to identify spam or unwanted messages. 
                    This functionality not only enhances communication but also helps maintain a positive environment in various applications, such as social media platforms, forums, and customer feedback systems.
                </p>
            </div>


            <script>
                const text1 = "SENTIMENT";
                const text2 = "ANALYSER";
                let index1 = 0;
                let index2 = 0;

                function typeText() {
                    const typingElement1 = document.getElementById("typing-text");
                    const typingElement2 = document.getElementById("typing-text-green");

                    // Log to check if function is running
                    console.log("Typing function called. Index1:", index1, "Index2:", index2);

                    if (index1 < text1.length) {
                        typingElement1.textContent += text1.charAt(index1);
                        index1++;
                        setTimeout(typeText, 90); // Adjust typing speed here (200 ms)
                    } else if (index2 < text2.length) {
                        typingElement2.textContent += text2.charAt(index2);
                        index2++;
                        setTimeout(typeText, 90); // Adjust typing speed here (150 ms)
                    }
                }

                // Ensure that the script runs after the page is fully loaded
                window.onload = function() {
                    typeText(); // Start typing animation on page load
                };
            </script>
        </body>
        </html>

        """
        
    )
    
    col1= st.columns([1],gap='small')

    with col1[0]:
        if st.button('START'):
            # Loading animation
            with st.spinner("Loading..."):
               time.sleep(2) 
           
            st.switch_page('pages/Inference.py')
    

    # Loading animation
    # with st.spinner("Loading..."):
    #     time.sleep(6) 


if __name__ == "__main__":
    app()
