import React from 'react'
class Burger extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            burg: ''
        }
        this.update = this.update.bind(this)
    }
    update(){
        console.log("update is called(burger)")
        this.setState({
            burg: this.state.burg + 'burger\n'
        })
    }
    render(){
        return (
            <>
                <h1 className='Burger'>{this.state.burg}</h1>
            </>
        )
    }
}
export default Burger