import streamlit as st
import streamlit.components.v1 as components

# Define the HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Streamlit Loader</title>
  <style>
    @font-face {
        font-family: Chana;
        src: url('https://example.com/Fonts/chaney-ultraextended-webfont.ttf'); /* Update with the correct URL */
    }

    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    html, body {
        width: 100%;
        height: 100%;
        overflow: hidden;
    }

    #main {
        width: 100%;
        min-height: 100vh;
        position: relative;
    }

    .loader {
        position: absolute;
        width: 100%;
        height: 100vh;
        background-color: rgb(250,195,8);
        animation: pulse 3s infinite;
        z-index: 9;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }

    .scramble {
        font-family: Chana;
        font-size: 7vw; /* Larger font size for title */
        color: #fff;
        animation: rotate-scale 5s infinite;
        z-index: 10;
        margin-bottom: 5%; /* Reduced space below the title */
    }

    .loading-bar {
        position: absolute;
        width: 70%; /* Adjust to match the width of the text */
        height: 10px;
        background: #f1f1f1;
        border-radius: 5px;
        top: 20%; /* Adjusted to position it slightly above the middle */
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
    }

    .loading-bar:after {
        content: "";
        position: absolute;
        height: 100%;
        border-radius: 5px;
        animation: load 3s infinite;
        background: #FFC0CB; /* Pink color for the loading bar */
    }

    .loading-text-top {
        position: absolute;
        width: 70%; /* 70% of the viewport width */
        text-align: center;
        font-family: Chana;
        font-weight: bold;
        z-index: 15; /* Increased z-index to be above loading bar */
        top: 10%; /* Adjusted to be above the loading bar */
        font-size: 7vw; /* Adjust font size to cover about 70% of the page width */
        animation: color-zoom 3s infinite; /* Apply color-zoom animation */
        color: #00FF00; /* Initial color */
    }

    .Loading {
        position: absolute;
        bottom: 25px; /* Adjust position to be slightly above the bottom with a 25px gap */
        width: 400%; /* Increase width to make the loading bar even longer */
        height: 15px; /* Increase height for better visibility */
        background: #f1f1f1;
        border-radius: 4px;
        overflow: hidden;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
        z-index: 1;
    }

    .Loading:after {
        content: "";
        position: absolute;
        height: 100%;
        border-radius: 4px;
        animation: load 3s infinite;
        background: #FFC0CB; /* Pink color for the loading bar */
    }

    .loading-text-bottom {
        position: absolute;
        width: 80%; /* Increase width to accommodate larger text */
        text-align: center;
        font-family: Chana;
        font-weight: bold;
        z-index: 5;
        bottom: 50px; /* Positioning at the bottom with 25px gap from the loading bar */
        font-size: 6vw; /* Adjust font size to fit text in a single line */
        color: #fff;
        animation: fire 2s infinite;
    }

    @keyframes load {
        0% {
            width: 0;
            background: #FFC0CB; /* Pink color */
        }
        25% {
            width: 25%;
            background: #FFC0CB; /* Pink color */
        }
        50% {
            width: 50%;
            background: #FFC0CB; /* Pink color */
        }
        75% {
            width: 75%;
            background: #FFC0CB; /* Pink color */
        }
        100% {
            width: 100%;
            background: #FFC0CB; /* Pink color */
        }
    }

    @keyframes pulse {
        0% {
            background: #a28089;
        }
        25% {
            background: #a0d2eb;
        }
        50% {
            background: #d0bdf4;
        }
        75% {
            background: #d2d2d2;
        }
        100% {
            background: rgb(250, 195, 8);
        }
    }

    @keyframes rotate-scale {
        0% {
            transform: rotate(0deg) scale(1);
            opacity: 0.5;
        }
        50% {
            transform: rotate(180deg) scale(1.5);
            opacity: 1;
        }
        100% {
            transform: rotate(360deg) scale(1);
            opacity: 0.5;
        }
    }

    @keyframes color-zoom {
        0% {
            color: #FFFF00; /* Yellow */
            transform: scale(1);
        }
        25% {
            color: #00FF00; /* Green */
            transform: scale(1.2);
        }
        50% {
            color: #800080; /* Purple */
            transform: scale(1);
        }
        75% {
            color: #FFC0CB; /* Pink */
            transform: scale(1.2);
        }
        100% {
            color: #FFFF00; /* Yellow */
            transform: scale(1);
        }
    }

    @keyframes glow {
        0% {
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.5), 0 0 20px rgba(255, 255, 255, 0.4);
        }
        50% {
            text-shadow: 0 0 20px rgba(255, 255, 255, 1), 0 0 30px rgba(255, 255, 255, 0.7);
        }
        100% {
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.5), 0 0 20px rgba(255, 255, 255, 0.4);
        }
    }

    @keyframes fire {
        0% {
            color: #fff;
            text-shadow: 0 0 5px rgba(255, 165, 0, 0.7), 0 0 10px rgba(255, 69, 0, 0.7);
        }
        50% {
            color: #ff4500;
            text-shadow: 0 0 10px rgba(255, 140, 0, 1), 0 0 20px rgba(255, 69, 0, 0.7);
        }
        100% {
            color: #fff;
            text-shadow: 0 0 5px rgba(255, 165, 0, 0.7), 0 0 10px rgba(255, 69, 0, 0.7);
        }
    }
  </style>
</head>
<body>
  <div id="main">
    <div class="loader">
      <h1 class="scramble">IBN ADAM</h1>
      <div class="loading-text-top">SHAHAN NAFEES</div>
      <div class="loading-bar"></div> <!-- Small loading bar below the text -->
      <div class="Loading"></div>
      <div class="loading-text-bottom">GENERATIVE AI MECHANICAL ENGINEER</div>
    </div>
  </div>
</body>
</html>
"""

# Create a Streamlit app
st.title("LOADING MAIN PAGE")
components.html(html_content, height=700, scrolling=True)
