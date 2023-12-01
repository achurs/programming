import React from "react";
import './Home.css'
class Home extends React.Component {
    render() {
        return (
            <>
            <Header />
            <Main />
            <Footer />
            </>
        )
    }
}
export default Home

function Header() {
    return (
        <>
        <p>Header</p>
        </>
    )
}
function Main() {
    return (
        <>
        <p>Main</p>
        </>
    )
}
function Footer() {
    return (
        <>
        <p>Footer</p>
        </>
    )
}