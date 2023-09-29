import React from 'react'
import './Font.css'
class Font extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            text: ''
        }
        this.update = this.update.bind(this)
    }
    update(event) {
        console.log("update is called");
        this.setState({
            text: event.target.value
        })
    }
    render() {
        return (
            <>
                <textarea type="text" placeholder='Enter text' onChange={this.update} value={this.state.input} />
                <h1 className='Font'>{this.state.text}</h1>
            </>
        )
    }
}
export default Font