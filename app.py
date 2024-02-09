from flask import Flask, render_template, Response
import requests
import camera
from camera import Video, choice, total_headgears

app=Flask(__name__)

#rendering the HTML page which has the button
#@app.route('/index')
#def json():
 #   return render_template('json.html')

#background process happening without any refreshing

camera.choice = 0

@app.route('/')
def index():
    """"""
    
    #global ch
    return render_template('index.html')

@app.route('/culturalNews.html')
def culturalNews():
    """Function:
    def culturalNews():
        Retrieves news articles related to festivals from the News API and renders them on a web page.
        Parameters:
            None
        Returns:
            - dict: A dictionary containing a list of articles from the News API.
        Processing Logic:
            - Uses the News API to retrieve articles.
            - Renders the articles on a web page.
        url = ('https://newsapi.org/v2/everything?'
    'q=festival&'
    'from=2022-10-26&'
    'sortBy=popularity&'
    'language=en&'
    'apiKey=8d9dec18335e4d82b8d31756136ebc10')
        r = requests.get(url, timeout=60).json(timeout=60)
        case = {
            'articles' : r['articles']
        }
        return render_template("culturalNews.html", cases = case)"""
    
    url = ('https://newsapi.org/v2/everything?'
           'q=festival&'
           'from=2022-10-26&'
           'sortBy=popularity&'
           'language=en&'
           'apiKey=8d9dec18335e4d82b8d31756136ebc10')
    r = requests.get(url, timeout=60).json(timeout=60)
    case = {
        'articles' : r['articles']
    }
    return render_template("culturalNews.html", cases = case)

@app.route('/start.html')
def start_the_quiz():
    """"Renders the start.html template to begin the quiz."
    Parameters:
        - None
    Returns:
        - render_template: Renders the start.html template.
    Processing Logic:
        - Renders start.html template.
        - No parameters needed.
        - No additional processing logic needed.
        - Simple function to start the quiz."""
    
    return render_template("start.html")

@app.route('/quiz.html')
def quiz_live():
    """"Renders the quiz template for the user to take the quiz.
    Parameters:
        None.
    Returns:
        - template: Renders the quiz template for the user to take the quiz.
    Processing Logic:
        - Renders the quiz template.
        - No parameters needed.
        - Returns the rendered template.
        - Can be used to display the quiz for the user to take.""""
    
    return render_template("quiz.html")

@app.route('/end.html')
def quiz_end():
    """"Renders the end.html template for the quiz application."
    Parameters:
        - None.
    Returns:
        - None.
    Processing Logic:
        - Renders the end.html template.
        - Used to display the end of the quiz.
        - Called when the quiz is completed."""
    
    return render_template("end.html")


@app.route('/background_process_test')
def background_process_test():
    """Function: background_process_test
    Parameters:
        - None
    Returns:
        - str: "nothing"
    Processing Logic:
        - Increment camera choice by 1.
        - Reset camera choice to 0 if it exceeds total headgears.
        - Return "nothing"."""
    
    camera.choice = (camera.choice+1) % camera.total_headgears
    #global ch
    #ch = (ch + 1) % camera.total_headgears
    return ("nothing")


def gen(camera):
    """This function generates a frame from the camera.
    Parameters:
        - camera (object): Camera object used to capture frames.
    Returns:
        - frame (bytes): Frame captured by the camera.
    Processing Logic:
        - Infinite loop.
        - Get frame from camera.
        - Yield frame.
        - End of loop."""
    
    #choice = 1
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
       b'Content-Type:  image/jpeg\r\n\r\n' + frame +
         b'\r\n\r\n')

@app.route('/video')

def video():
    """Function to generate a video response.
    Parameters:
        - gen (function): Function that generates video.
        - Video (class): Class that contains video.
    Returns:
        - Response (class): Class that contains video response.
    Processing Logic:
        - Generate video response.
        - Set response mimetype.
        - Set response boundary.
        - Return video response."""
    
    return Response(gen(Video()),
    mimetype='multipart/x-mixed-replace; boundary=frame')

#app.run(debug=True)
