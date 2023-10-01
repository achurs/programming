import React from "react";
import "./Quote.css";

class Quote extends React.Component {
    constructor(props) {
        super(props);
        this.quotes ={
            "The best way to predict the future is to invent it":"Albert Einstein",
            "Never confuse a single defeat with a final defeat." : "Vince Lombardi",
            "You miss 100% of the shots you don't take." : "Wayne Gretzky",
            "Be yourself; everyone else is already taken." : "Oscar Wilde",
            "Life is what happens when you're busy making other plans." : "John Lennon",
            "You only live once, but if you do it right, once is enough." : "Mae West",
            "If you tell the truth, you don't have to remember anything." : "Mark Twain",
            "If you want to live a happy life, tie it to a goal, not to people or things." : "Albert Einstein",
            "You only live once, but if you do it right, once is enough." : "Mae West",
        }
        this.state = {
            quote: '',
            author: ''
        }
        this.state.quote = this.getRandomQuote();
        this.state.author = this.quotes[this.state.quote];
    }
    getRandomQuote = () => {
        const keys = Object.keys(this.quotes);
        const randomIndex = Math.floor(Math.random() * keys.length);
        const randomKey = keys[randomIndex];
        return randomKey;
    };

    render() {
        return (
            <div className="quote-box">
                <div className="quote">
                    <p>{this.state.quote}</p>
                </div>
                <div className="author">
                    <p><span className="fas fa-quote-left"></span>{this.state.author}<span className="fas fa-quote-right"></span></p>
                </div>
                <span className="set-right"></span><button onClick={() => this.setState({quote: this.getRandomQuote(), author: this.quotes[this.state.quote]})} className="btn bg-transparent">new quote</button>
            </div>
        );
    }
}
export default Quote;