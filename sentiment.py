from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from tkinter import *
def clearAll():
    negativeField.delete(0, END)
    neutralField.delete(0, END)
    positiveField.delete(0, END)
    overallField.delete(0, END)
    textArea.delete(1.0, END)
def detect_sentiment():
    sentence = textArea.get("1.0", "end")
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    string = str(sentiment_dict['neg'] * 100) + "% Negative"
    negativeField.insert(10, string)
    string = str(sentiment_dict['neu'] * 100) + "% Neutral"
    neutralField.insert(10, string)
    string = str(sentiment_dict['pos'] * 100) + "% Positive"
    positiveField.insert(10, string)
    if sentiment_dict['compound'] >= 0.05:
        string = "Positive"
    elif sentiment_dict['compound'] <= - 0.05:
        string = "Negative"
    else:
        string = "Neutral"
    overallField.insert(10, string)
if __name__ == "__main__":
    gui = Tk()
    gui.config(background="light green")
    gui.title("Sentiment Detector")
    gui.geometry("500x400")
    enterText = Label(gui, text="Enter Your Sentence", bg="light green")
    textArea = Text(gui, height=5, width=25, font="lucida 13")
    check = Button(gui,	text="Check Sentiment", fg="Black",	bg="Red",               command=detect_sentiment)
    negative = Label(gui, text="Sentence was rated as: ", bg="light green")
    neutral = Label(gui, text="Sentence was rated as: ", bg="light green")
    positive = Label(gui, text="Sentence was rated as: ", bg="light green")
    overall = Label(gui, text="Sentence Overall Rated As: ", bg="light green")
    negativeField = Entry(gui)
    neutralField = Entry(gui)
    positiveField = Entry(gui)
    overallField = Entry(gui)
    clear = Button(gui, text="Clear", fg="Black", bg="Red", command=clearAll)
    Exit = Button(gui, text="Exit", fg="Black", bg="Red", command=exit)
    enterText.pack()
    textArea.pack()
    check.pack()
    negative.pack()
    negativeField.pack()
    neutral.pack()
    neutralField.pack()
    positive.pack()
    positiveField.pack()
    overall.pack()
    overallField.pack()
    clear.pack()
    Exit.pack()
    gui.mainloop()
