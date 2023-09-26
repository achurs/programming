import React from 'react'

class Pizza extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            pizz: ''
        }
        this.update = this.update.bind(this)
    }
    update(){
        console.log("update is called(pizza)")
        this.setState({
            pizz: this.state.pizz + 'pizza\n'
        })
    }
    render(){
        return (
            <>
                <h1 className='Pizza'>{this.state.pizz}</h1>
            </>
        )
    }
}
export default Pizza