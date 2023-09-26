import { useRef } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Pizza from './Pizza'
import Burger from './Burger'

function App() {
  const pizzaRef = useRef(null);
  const pizzaClick = () => {
    if (pizzaRef.current) {
      pizzaRef.current.update();
    }
  };
  
  const burgerRef = useRef(null);
  const burgerClick = () => {
    if (burgerRef.current) {
      burgerRef.current.update();
    }
  }

  return (
    <>
      <h1 className='vitee'>Vite + React</h1>
      <Pizza ref={pizzaRef} />
      <Burger ref={burgerRef} />
      <button className='btn btn-primary' onClick={pizzaClick}>Add Pizza</button>
      <button className='btn btn-secondary' onClick={burgerClick}>Add Burger</button>
    </>
  )
}

export default App
